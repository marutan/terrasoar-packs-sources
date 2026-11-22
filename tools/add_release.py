#!/usr/bin/env python3
"""Adds a release's record to this repository: sources/<release>/ and its
entry in sources.json.

Usage: add_release.py <release.json> --data <dir> --configs <terrasoar>/tools/packager/packs
                      [--configs <file or dir> ...]

<release.json> describes the release:

    {"release": "gshhg-2.3.7", "title": "…", "publisher": "…",
     "page": "https://…", "licence": "…", "credit": "…",
     "retrieved": "2026-11-22", "terms": "Markdown for SOURCE.md's Terms",
     "licenceFiles": ["/path/LICENSE.TXT", …],
     "files": ["gshhg-shp-2.3.7.zip", …]}

Each file must be in --data, and named by a source of a Terra Soar pack
configuration (--configs: configuration files or directories of them)
with the same SHA-256: its upstream URL, mirror, name, version and the
packs that use it come from there. The licence files are copied into
sources/<release>/, SOURCE.md is written and sources.json updated (an
entry of the same release is replaced). Nothing is uploaded: the command
to create the release is printed.
"""

import argparse
import glob
import hashlib
import json
import os
import shlex
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPOSITORY = "marutan/terrasoar-packs-sources"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def configured_sources(paths):
    """file name -> (source entry, set of pack ids)"""
    found = {}
    files = []
    for path in paths:
        files += sorted(glob.glob(os.path.join(path, "*.json"))) \
            if os.path.isdir(path) else [path]
    for path in files:
        with open(path, encoding="utf-8") as handle:
            config = json.load(handle)
        for source in config.get("sources", []):
            entry = found.setdefault(source["file"], (source, set()))
            entry[1].add(config["id"])
    return found


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("release")
    parser.add_argument("--data", required=True)
    parser.add_argument("--configs", action="append", required=True)
    args = parser.parse_args(argv)
    with open(args.release, encoding="utf-8") as handle:
        meta = json.load(handle)
    tag = meta["release"]
    sources = configured_sources(args.configs)
    entries = []
    for name in meta["files"]:
        path = os.path.join(args.data, name)
        if name not in sources:
            sys.exit(f"{name}: no pack configuration names it")
        source, packs = sources[name]
        digest = sha256_of(path)
        if digest != source["sha256"].lower():
            sys.exit(f"{name}: SHA-256 {digest}, configured {source['sha256']}")
        mirror = f"https://github.com/{REPOSITORY}/releases/download/{tag}/{name}"
        if source.get("mirror") != mirror:
            sys.exit(f"{name}: the configuration's mirror is not {mirror}")
        entries.append({
            "file": name, "bytes": os.path.getsize(path), "sha256": digest,
            "upstream": source["url"], "mirror": mirror,
            "name": source["name"], "version": source["version"],
            "packs": sorted(packs)})
    directory = os.path.join(ROOT, "sources", tag)
    os.makedirs(directory, exist_ok=True)
    licence_names = []
    for licence in meta["licenceFiles"]:
        target = os.path.join(directory, os.path.basename(licence))
        if os.path.abspath(licence) != os.path.abspath(target):
            shutil.copyfile(licence, target)
        licence_names.append(os.path.basename(licence))
    lines = [
        f"# {tag}", "", meta["title"] + ".", "",
        f"- **Publisher**: {meta['publisher']}",
        f"- **Project page**: {meta['page']}",
        f"- **Licence**: {meta['licence']}",
        f"- **Credit**: \"{meta['credit']}\"",
        f"- **Downloaded from upstream**: {meta['retrieved']}, each file "
        "checked against the SHA-256 Terra Soar's pack configurations pin",
        f"- **Release**: https://github.com/{REPOSITORY}/releases/tag/{tag}",
        "", "## Terms", "", meta["terms"], "",
        "Licence and terms files, here and attached to the release: " +
        ", ".join(f"`{n}`" for n in licence_names) + ".", "",
        "## Files", "",
        "| File | Bytes | SHA-256 | Downloaded from | Used by |",
        "| --- | --- | --- | --- | --- |"]
    for e in entries:
        lines.append(f"| `{e['file']}` | {e['bytes']} | `{e['sha256']}` | "
                     f"{e['upstream']} | "
                     + ", ".join(f"`{p}`" for p in e["packs"]) + " |")
    with open(os.path.join(directory, "SOURCE.md"), "w", encoding="utf-8") as out:
        out.write("\n".join(lines) + "\n")
    catalogue_path = os.path.join(ROOT, "sources.json")
    with open(catalogue_path, encoding="utf-8") as handle:
        catalogue = json.load(handle)
    record = {k: meta[k] for k in ("title", "publisher", "page", "licence",
                                   "credit", "retrieved")}
    record = {"release": tag, **record, "licenceFiles": licence_names,
              "files": entries}
    releases = [r for r in catalogue["releases"] if r["release"] != tag]
    releases.append(record)
    catalogue["releases"] = releases
    with open(catalogue_path, "w", encoding="utf-8") as out:
        out.write(json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n")
    assets = [os.path.join(args.data, n) for n in meta["files"]] + \
        [os.path.join(directory, n) for n in licence_names + ["SOURCE.md"]]
    notes = (f"{meta['title']}.\n\nLicence: {meta['licence']}. Credit: "
             f"\"{meta['credit']}\".\n\nSee sources/{tag}/SOURCE.md for where "
             "each file was downloaded from, its SHA-256 and the packs that "
             "use it. The licence and terms files are attached alongside the "
             "data.")
    print("gh release create " + shlex.quote(tag) + f" --repo {REPOSITORY} "
          f"--target main --title {shlex.quote(tag)} --notes "
          + shlex.quote(notes) + " " + " ".join(shlex.quote(a) for a in assets))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
