#!/bin/bash

VENV=venv
DEPS=requirements.txt

[ -d $VENV ] || virtualenv $VENV
source $VENV/bin/activate
pip install -r $DEPS
