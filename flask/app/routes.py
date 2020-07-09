import datetime
import markdown
import os

from flask import request

from app import app, db
from .models import DeadlineModel
from .schemas import deadline_schema, deadlines_schema,\
    deadline_update_schema

@app.route('/')
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as docs:
        content = docs.read()
        return markdown.markdown(content)

