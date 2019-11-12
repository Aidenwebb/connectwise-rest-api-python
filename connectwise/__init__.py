import logging
import os.path
import sys

from connectwise.client import Client
from connectwise import exceptions

my_path = os.path.dirname(__file__)
path = os.path.join(my_path, "../")

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __build__, __license__

# Use null logger since we always run with a logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__ = ["Client"]
