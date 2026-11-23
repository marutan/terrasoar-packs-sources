# gebco-2026

The GEBCO_2026 Grid, ice surface elevation, Data GeoTIFF: a 15 arc-second terrain model for ocean and land, as eight 90° tiles in one zip.

- **Publisher**: GEBCO Compilation Group (IHO and IOC), distributed by the British Oceanographic Data Centre
- **Project page**: https://www.gebco.net/data-products/gridded-bathymetry-data
- **Licence**: Public domain (GEBCO)
- **Credit**: "GEBCO Compilation Group (2026) GEBCO 2026 Grid"
- **Downloaded from upstream**: 2026-11-23, each file checked against the SHA-256 Terra Soar's pack configurations pin
- **Release**: https://github.com/marutan/terrasoar-packs-sources/releases/tag/gebco-2026

## Terms

Placed in the public domain; the source must be acknowledged, no official status or endorsement implied, and not for navigation. See `TERMS.md` and GEBCO's own `GEBCO_Grid_terms_of_use.pdf` and `GEBCO_Grid_documentation.pdf` (from the zip). The zip is larger than a release asset may be (4.2 GB), so it is kept in three parts, joined by Terra Soar's `fetch_sources.py`; it was downloaded on a GitHub runner by the "Mirror a large source" workflow, as GEBCO's host does not answer every network.

Licence and terms files, here and attached to the release: `TERMS.md`, `GEBCO_Grid_terms_of_use.pdf`, `GEBCO_Grid_documentation.pdf`.

## Files

| File | Bytes | SHA-256 | Downloaded from | Used by |
| --- | --- | --- | --- | --- |
| `gebco_2026_geotiff.zip` (in 3 parts, `.part00` to `.part02`) | 4241629269 | `39bb6eb45a785101da606749a00cf0ec3217f32160d25859b48fd5db9c6d9368` | https://dap.ceda.ac.uk/bodc/gebco/global/gebco_2026/ice_surface_elevation/geotiff/gebco_2026_geotiff.zip | `gebco-0-e90`, `gebco-e90-e180`, `gebco-w180-w90`, `gebco-w90-0` |
