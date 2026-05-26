import os
import sys

# Allow tests under playwright/ to import local workspace modules as top-level packages.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "playwright"))
