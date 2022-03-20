from contextlib import suppress
from importlib import metadata

__author__ = "Peter Yuen"
__email__ = "ppeetteerrsx@gmail.com"
__version__ = "test"
with suppress(Exception):
    __version__ = metadata.version("simple_pypackage")
