import dataclasses
import importlib.metadata
from dataclasses import dataclass
from pathlib import Path

import jinja2
import pystac.version
from jinja2 import Environment, PackageLoader

root = Path(__file__).parent
examples = root / "examples"
item = examples / "simple-item.json"


class Result:
    pass


@dataclass
class Repository:
    name: str
    url: str
    description: str
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
        version=importlib.metadata.version("pystac"),
        read=read,
        write=write,
        notes=notes,
    )


def stac_server() -> Repository:
    # This was manual, but we only have to do it once so :shrug:
    return Repository(
        "stac-server",
        "https://github.com/stac-utils/stac-server",
        "A Node-based STAC API, AWS Serverless, OpenSearch",
        version="3.8.0",
        read=True,
        write=True,
        notes="",
    )


repositories = [dataclasses.asdict(d) for d in [pgstac(), pystac(), stac_server()]]


def emoji(value: bool) -> str:
    if value:
        return "✅"
    else:
        return "❌"


environment = Environment(
    loader=PackageLoader("render"),
    autoescape=jinja2.select_autoescape(),
    keep_trailing_newline=True,
)
environment.filters["emoji"] = emoji
template = environment.get_template("README.md.jinja2")
with open(root / "README.md", "w") as f:
    f.write(template.render({"repositories": repositories}))
