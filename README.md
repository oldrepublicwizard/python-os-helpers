# python-os-helpers

Odds and ends for finding things on disk: frozen-app resource dirs, path helpers, font discovery, a few misc OS utilities.

Nothing fancy. If you're shipping a PyInstaller/cx_Freeze build and need "where's my data folder?", start here.

## Install

```bash
pip install git+https://github.com/oldrepublicwizard/python-os-helpers.git
```

```python
from python_os_helpers import get_app_dir  # names vary; check the package
```

## License

LGPL-3.0-or-later
