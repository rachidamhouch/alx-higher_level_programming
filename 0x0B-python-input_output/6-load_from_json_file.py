#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(filename) as f:
        return json.load(f)
