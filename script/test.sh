#!/bin/bash
source ~/.bashrc
source venv/bin/activate
pip3 show coverage
python3 -m coverage run -m pytest test/testing.py
python3 -m coverage report -m