import importlib

import pytest


@pytest.mark.parametrize(
    "module_name",
    [
        "squadds",
        "squadds.calcs",
        "squadds.core",
        "squadds.database",
        "squadds.interpolations",
        "squadds.core.utils",
        "squadds.core.design_patterns",
        "squadds.core.analysis",
        "squadds.database.utils",
        "squadds.interpolations.interpolator",
        "squadds.calcs.qubit",
        "squadds.calcs.transmon_cross",
    ],
)
def test_import(module_name):
    imported_module = importlib.import_module(module_name)
    assert imported_module.__name__ == module_name, f"Failed to import {module_name}"
