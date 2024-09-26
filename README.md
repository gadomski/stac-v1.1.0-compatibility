# STAC v1.1.0 compatibility

[STAC v1.1.0](https://github.com/radiantearth/stac-spec/releases/tag/v1.1.0) was released September 2024.
This repository tracks the software ecosystem's update of the new release.

**NOTE**: As of 2024-09-25 this repo is under construction as new repositories are added.
If you'd like to see a repository added, please open [an issue](https://github.com/gadomski/stac-v1.1.0-compatability/issues).

## Repository

| Name | Version | Description | Read | Write | Notes |
| -- | -- | -- | -- | -- | -- |
| [pystac](https://github.com/stac-utils/pystac) | 1.10.1 | Python library for working with any SpatioTemporal Asset Catalog (STAC) | ✅ | ❌ | On write, STAC version is 1.0.0 |
| [stac-server](https://github.com/stac-utils/stac-server) | 3.8.0 | A Node-based STAC API, AWS Serverless, OpenSearch | ✅ | ✅ |  |

## Usage

```shell
pip install -r requirements.txt
python render.py
```

**stac-server** was more trouble than it was worth to automate, but since it passed on first test, that's ok.