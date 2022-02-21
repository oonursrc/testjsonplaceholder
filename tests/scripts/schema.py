import json
import os
from os.path import dirname

import jsonschema
from jsonschema import validate

ROOT_DIR = os.path.dirname(dirname(dirname(__file__)))  # Project root dir


def get_schema():
    """Loads the given schema"""
    with open(ROOT_DIR + '/config/user_schema.json', 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data):
    """Validates given json

    Parameters:
        json_data: json data to be checked

    Return:
        True if json data matched with schema otherwise False
    """
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError:
        return False

    return True
