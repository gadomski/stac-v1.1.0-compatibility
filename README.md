# STAC v1.1.0 compatibility

[STAC v1.1.0](https://github.com/radiantearth/stac-spec/releases/tag/v1.1.0) was released September 2024.
This repository tracks the software ecosystem's update of the new release.
If you'd like to see a repository added, please open [an issue](https://github.com/gadomski/stac-v1.1.0-compatability/issues).

## Repository

| Name | Version | Description | Read | Write | Notes |
| -- | -- | -- | -- | -- | -- |
| [pgstac](https://github.com/stac-utils/pgstac) | 0.9.1 | Schema, functions and a python library for storing and accessing STAC collections and items in PostgreSQL | ✅ | ✅ |  |
| [pystac](https://github.com/stac-utils/pystac) | 1.10.1 | Python library for working with any SpatioTemporal Asset Catalog (STAC) | ✅ | ❌ | On write, STAC version is 1.0.0 |
| [stac-rs](https://github.com/stac-utils/stac-rs) | v0.10.1 | Tools and libraries for the SpatioTemporal Asset Catalog (STAC) specification, written in Rust | ✅ | ✅ |  |
| [stac-server](https://github.com/stac-utils/stac-server) | 3.8.0 | A Node-based STAC API, AWS Serverless, OpenSearch | ✅ | ✅ |  |

## Usage

```shell
pip install -r requirements.txt
pre-commit run --all-files
```

**stac-server** and **pgstac** were tested manually, but the rest of the packages are updated dynamically on a `render.py` run.
