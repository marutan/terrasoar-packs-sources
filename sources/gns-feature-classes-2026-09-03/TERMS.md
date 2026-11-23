# Terms: GEOnet Names Server (GNS)

The GEOnet Names Server is the US National Geospatial-Intelligence
Agency's database of foreign geographic names, the names the US Board on
Geographic Names approves for use outside the United States. It is a work
of the US government, which in the United States is not subject to
copyright (17 U.S.C. § 105). NGA states no licence for the files; each
comes with `disclaimer.txt` (included, the same in every file):

> The geographic names in this database are provided for the guidance of
> and use by the Federal Government and for the information of the general
> public. The names, variants, and associated data may not reflect the
> views of the United States Government on the sovereignty over geographic
> features. NGA is not responsible for third party uses of GNS feature
> coordinates.

The GNS website asks visitors to accept its Terms of Service before
entering; that page could not be read when these files were taken
(2026-11-22), as NGA's server (geonames.nga.mil) did not answer.
`GNS_User_Guide.txt` (included) is NGA's guide that comes with the files.

**How the files were obtained.** NGA's server did not answer from the
network these files were mirrored from, so they were taken from the
Internet Archive's captures of NGA's own files of 2026-09-03 (for example
https://web.archive.org/web/20260903061713id_/https://geonames.nga.mil/geonames/GNSData/fc_files/Populated_Places.zip).
Each file's SHA-1 matches the digest the archive recorded when it captured
it:

| File | Capture | SHA-1 |
| --- | --- | --- |
| `Populated_Places.zip` | 20260903061713 | `b5d65a183e38e1ea13d36d936a91800c8ced71d3` |
| `Hypsographic.zip` | 20260903061805 | `89b628f086279070fd6eba4fc4653c5572278611` |
| `Hydrographic.zip` | 20260903061628 | `66c78e3ffeda4da1b97cfe4d59b71b05feba8f90` |
| `Undersea.zip` | 20260903061525 | `7c41edc17cef5a93375e46780bbbaf270204cfd3` |

Terra Soar credits it as "Names: NGA GNS".
