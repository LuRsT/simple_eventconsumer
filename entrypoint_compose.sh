#!/bin/ash

set -e

sleep 5

python3 init_streams.py
python3 main.py config.yaml
