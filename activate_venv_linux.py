"""
Activate virtualenv for current interpreter:

import runpy
runpy.run_path(this_file)

This can be used when you must use an existing Python interpreter
"""  # noqa: D415

from __future__ import annotations

import os
import site
import sys

try:
    abs_file = os.path.abspath(__file__)
except NameError as exc:
    msg = "You must use import runpy; runpy.run_path(this_file)"
    raise AssertionError(msg) from exc

__BIN_NAME__ = "bin"
__VIRTUAL_PROMPT__ = None
__LIB_FOLDERS__ = "lib/python3.10/site-packages"
__DECODE_PATH__ = False

venv_dir = os.path.join(os.path.dirname(abs_file), ".venv")
if not os.path.isdir(venv_dir):
    # Fallback: Suche nach venv im Parent-Verzeichnis
    venv_dir = os.path.join(os.path.dirname(os.path.dirname(abs_file)), ".venv")
    if not os.path.isdir(venv_dir):
        raise RuntimeError("Konnte das venv-Verzeichnis nicht finden.")

bin_dir = os.path.join(venv_dir, __BIN_NAME__)
base = venv_dir

# prepend bin to PATH (this file is inside the bin directory)
os.environ["PATH"] = os.pathsep.join([bin_dir, *os.environ.get("PATH", "").split(os.pathsep)])
os.environ["VIRTUAL_ENV"] = base  # virtual env is right above bin directory
os.environ["VIRTUAL_ENV_PROMPT"] = __VIRTUAL_PROMPT__ or os.path.basename(base)

# add the virtual environments libraries to the host python import mechanism
prev_length = len(sys.path)
for lib in __LIB_FOLDERS__.split(os.pathsep):
    path = os.path.realpath(os.path.join(bin_dir, lib))
    site.addsitedir(path.decode("utf-8") if __DECODE_PATH__ else path)
sys.path[:] = sys.path[prev_length:] + sys.path[0:prev_length]

sys.real_prefix = sys.prefix
sys.prefix = base

### print information about the activated virtual environment

print(f"INFO:  Activated virtualenv: {base!r} with {len(sys.path)- prev_length} new paths")
print("INFO:  $VIRTUAL_ENV: ",os.popen("echo $VIRTUAL_ENV").read())