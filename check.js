const Migrate = require('@radiantearth/stac-migrate');
const StacFields = require('@radiantearth/stac-fields');
const fs = require("node:fs");

function stac_fields() {
    const item = fs.readFileSync("examples/simple-item.json");
    StacFields.formatItemProperties(item)
    return {
        "name": "stac-fields",
        "url": "https://github.com/stac-utils/stac-fields",
        "description": "A minimal STAC library that contains a list of STAC fields with some metadata and helper functions for styling as HTML.",
        "language": "Javascript",
        "version": "1.5.0",
        "read": true,
        "write": null,
        "notes": "",
    }
}

function stac_migrate() {
    const item = fs.readFileSync("examples/simple-item.json");
    const migrated_item = Migrate.stac(item);
    const write = migrated_item["stac_version"] == "1.1.0";
    return {
        "name": "stac-migrate",
        "url": "https://github.com/stac-utils/stac-migrate",
        "description": "A tool to migrate Items, Catalogs and Collections from old versions to the most recent one.",
        "language": "Javascript",
        "version": "2.0.0",
        "read": true,
        "write": write,
        "notes": "",
    }
}

const repositories = [
    stac_fields(),
    stac_migrate()
];

fs.writeFileSync("checks/js.json", JSON.stringify(repositories));
