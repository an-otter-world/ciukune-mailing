"""Settings package, including splitted settings files."""
from split_settings.tools import optional, include

include(
    '../third-party/ciukune/ciukune/settings/__init__.py',
)
