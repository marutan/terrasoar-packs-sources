# Terra Soar pack sources

The raw source data of [Terra Soar](https://github.com/marutan/terrasoar)'s
data packs: every file the base pack and the extra packs are built from,
unchanged, with where it was downloaded from and the licence or terms it
was distributed under.

Terra Soar's packager downloads its sources from here, not from the sites
that first published them. Sites move, close, change files under the same
name, and limit automated downloads. Keeping a copy here means every pack
can be rebuilt exactly, from one place, with each file's terms kept next
to it. The built packs are in
[marutan/terrasoar-packs](https://github.com/marutan/terrasoar-packs).

## Layout

- **Releases** hold the data, one release per dataset (`vmap0-5.0`,
  `gshhg-2.3.7`, …). Each has the source files and their licence and terms
  files attached. The files are release assets rather than git files
  because several are larger than git's 100 MB limit.
- **`sources/<release>/`** holds each release's `SOURCE.md` (what it is,
  who publishes it, the licence, the credit asked for, and each file's
  size, SHA-256, upstream URL and the packs that use it) and the same
  licence and terms files.
- **`sources.json`** catalogues it all for scripts: per release its
  licence, credit and licence files, and per file its size, SHA-256,
  upstream URL, the URL it is downloaded from here (`mirror`) and the packs
  that use it.

| Release | What | Licence |
| --- | --- | --- |
| [`gshhg-2.3.7`](sources/gshhg-2.3.7/SOURCE.md) | GSHHG shoreline shapefiles | LGPL-3.0-or-later |
| [`bmng-2004-07-full`](sources/bmng-2004-07-full/SOURCE.md) | Blue Marble, July 2004, full resolution | Public domain (NASA) |
| [`bmng-2004-monthly`](sources/bmng-2004-monthly/SOURCE.md) | Blue Marble, each month of 2004 | Public domain (NASA) |
| [`naturalearth-admin0-countries-5.1.2`](sources/naturalearth-admin0-countries-5.1.2/SOURCE.md) | Natural Earth countries | Public domain |
| [`etopo-2022-v1-60s-surface`](sources/etopo-2022-v1-60s-surface/SOURCE.md) | ETOPO 2022 relief, 60″ | CC0-1.0 (NOAA) |
| [`egm2008-2.5min`](sources/egm2008-2.5min/SOURCE.md) | EGM2008 geoid, 2.5′ (PROJ) | Public domain |
| [`egm96-15min`](sources/egm96-15min/SOURCE.md) | EGM96 geoid, 15′ (PROJ) | Public domain |
| [`uk-os-osgm15-ostn15`](sources/uk-os-osgm15-ostn15/SOURCE.md) | OSGM15 geoid and OSTN15 (PROJ) | BSD-2-Clause |
| [`vmap0-5.0`](sources/vmap0-5.0/SOURCE.md) | Vector Map Level 0, edition 5 | US government work; ESRI's features non-commercial only |
| [`naturalearth-10m-vectors-5.1.2`](sources/naturalearth-10m-vectors-5.1.2/SOURCE.md) | Natural Earth rivers, lakes, places, roads, railways, airports, ports, time zones, state borders, peaks | Public domain |
| [`naturalearth-10m-rasters-2.0.0`](sources/naturalearth-10m-rasters-2.0.0/SOURCE.md) | Natural Earth raster maps (relief, hypsometric, shaded relief) | Public domain |
| [`blackmarble-3km-2012-2016`](sources/blackmarble-3km-2012-2016/SOURCE.md) | Black Marble, the Earth at night, 2012 and 2016 | Public domain (NASA) |
| [`ourairports-2026-11-22`](sources/ourairports-2026-11-22/SOURCE.md) | OurAirports airports, runways, navaids | Public domain (the Unlicense) |
| [`gnis-domestic-names-2026-11-02`](sources/gnis-domestic-names-2026-11-02/SOURCE.md) | US place and feature names (USGS GNIS) | Public domain |

**Using the data yourself**: each file is under its own terms, given in its
`SOURCE.md`, not under Terra Soar's licence. Mostly they are public domain
or open licences. The exception is VMAP0's ESRI-owned features, which may
be used and redistributed for non-commercial purposes only.

## Adding a source

A new pack, or a new version of a source, follows Terra Soar's
[docs/design/packs.md](https://github.com/marutan/terrasoar/blob/main/docs/design/packs.md#where-the-source-data-is-kept),
"Where the source data is kept":

1. In Terra Soar, pin the file in the pack's configuration with `"url"`
   (upstream) and `"sha256"`. Download it with
   `tools/packager/fetch_sources.py --upstream`.
2. Check that its licence or terms allow it to be redistributed. A file
   whose terms don't allow that can't be kept here, and so can't be a
   pack's source.
3. Describe the release in a JSON file (see `tools/add_release.py`) and
   run `tools/add_release.py <release.json> --data <downloads> --configs
   <terrasoar>/tools/packager/packs`: it checks each file against the
   configurations, writes `sources/<tag>/` (`SOURCE.md` and the licence and
   terms files) and its entry in `sources.json`, and prints the `gh release
   create` command that uploads the files with them. Commit, push, and run
   that command.
4. In Terra Soar, add `"mirror"` to the configuration and build as usual.

A file here is never replaced: a changed upstream file is a new version,
and gets a new release.
