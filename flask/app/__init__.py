import markdown
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import Deadline

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as docs:
        content = docs.read()
        return markdown.markdown(content)

