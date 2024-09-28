import dataclasses
import importlib.metadata
import json
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory

import pystac.version

root = Path(__file__).parent
examples = root / "examples"
item = examples / "simple-item.json"
checks = root / "checks"


class Result:
    pass


@dataclass
class Repository:
    name: str
    url: str
    description: str
    language: str
    version: str
    read: bool
    write: bool
    notes: str


def pgstac() -> Repository:
    # Another manual one
    return Repository(
        "pgstac",
        "https://github.com/stac-utils/pgstac",
        "Schema, functions and a python library for storing and accessing STAC collections and items in PostgreSQL",
        "PostgreSQL",
        version="0.9.1",
        read=True,
        write=True,
        notes="",
    )


def pystac() -> Repository:
    import pystac

    pystac_item = pystac.read_file(item)
    read = True
    d = pystac_item.to_dict()
    write = d["stac_version"] == "1.1.0"

    if write:
        notes = None
    else:
        notes = f"On write, STAC version is {d['stac_version']}"

    return Repository(
        "pystac",
        "https://github.com/stac-utils/pystac",
        "Python library for working with any SpatioTemporal Asset Catalog (STAC)",
        "Python",
        version=importlib.metadata.version("pystac"),
        read=read,
        write=write,
        notes=notes,
    )


def stac_rs() -> Repository:
    # We test the python bindings, but that checks out the whole repo well 'nuff
    import stacrs

    item = stacrs.read(str(examples / "simple-item.json"))
    with TemporaryDirectory() as directory:
        path = f"{directory}/item.json"
        stacrs.write(path, item)
        with open(path) as f:
            item = json.load(f)
            write = item["stac_version"] == "1.1.0"
    return Repository(
        "stac-rs",
        "https://github.com/stac-utils/stac-rs",
        "Tools and libraries for the SpatioTemporal Asset Catalog (STAC) specification, written in Rust",
        "Rust",
        version="0.10.1",  # FIXME report this from the Python package
        read=True,
        write=write,
        notes="",
    )


def stac_server() -> Repository:
    # This was manual, but we only have to do it once so :shrug:
    return Repository(
        "stac-server",
        "https://github.com/stac-utils/stac-server",
        "A Node-based STAC API, AWS Serverless, OpenSearch",
        "Javascript",
        version="3.8.0",
        read=True,
        write=True,
        notes="",
    )


def stac_browser() -> Repository:
    return Repository(
        "stac-browser",
        "https://github.com/radiantearth/stac-browser/",
        "A full-fledged UI in Vue for browsing and searching static STAC catalogs and STAC APIs",
        "Javascript",
        version="3.2.0",
        read=True,
        write=None,
        notes="",
    )


repositories = [
    dataclasses.asdict(d)
    for d in [pgstac(), pystac(), stac_browser(), stac_rs(), stac_server()]
]

with open(checks / "python.json", "w") as f:
    json.dump(repositories, f)
