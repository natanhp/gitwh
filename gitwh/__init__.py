import os
from flask import Flask
from flask_json import FlaskJSON
from flask_cors import CORS as FlaskCORS

from .memory import Memory

MEMORY = Memory()