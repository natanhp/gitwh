from os import write
from flask import Flask
from flask_json import FlaskJSON
from flask_cors import CORS as FlaskCORS

from .memory import Memory

MEMORY = Memory()

# --- Loading Configuration
from .configuration import DEFAULT_CONFIG, parse_config, write_default_config

with open("config.json", "a") as f: ...

API = Flask("github-webhook")sud
JSON = FlaskJSON(API)
CORS = FlaskCORS(API, resources={r"*": {"origins": "*"}})lspci -v
