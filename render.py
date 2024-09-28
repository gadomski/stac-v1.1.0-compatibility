import json
import subprocess
from pathlib import Path
from typing import Any, Generator

import jinja2
from jinja2 import Environment, PackageLoader

root = Path(__file__).parent
checks = root / "checks"

subprocess.check_call(["python", "check.py"])
subprocess.check_call(["node", "check.js"])


def read(file_name: str) -> Generator[dict[str, Any], None, None]:
    with open(checks / file_name) as f:
        r = json.load(f)
        assert isinstance(r, list)
        for repository in r:
            yield repository
    return None


repositories = []
repositories.extend(read("python.json"))
repositories.extend(read("js.json"))


def emoji(value: bool | None) -> str:
    if value is True:
        return "✅"
    elif value is None:
        return "—"
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
