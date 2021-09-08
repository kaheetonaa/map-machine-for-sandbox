"""
Tests for Map Machine project.
"""
from pathlib import Path

from map_machine.icon import ShapeExtractor
from map_machine.scheme import Scheme
from map_machine.workspace import Workspace

__author__ = "Sergey Vartanov"
__email__ = "me@enzet.ru"

workspace: Workspace = Workspace(Path("temp"))

SCHEME: Scheme = Scheme(workspace.DEFAULT_SCHEME_PATH)
SHAPE_EXTRACTOR: ShapeExtractor = ShapeExtractor(
    workspace.ICONS_PATH, workspace.ICONS_CONFIG_PATH
)