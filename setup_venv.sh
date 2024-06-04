#!/bin/bash
set -x
sDir="$( cd "$( dirname "$0" )" && pwd )"
rm -rf "$sDir/.venv"
python3 -m venv "$sDir/.venv"
#source "$sDir/.venv/bin/activate"
# . "$sDir/.venv/bin/activate"
. .venv/bin/activate

which python3
pip install -r requirements.txt