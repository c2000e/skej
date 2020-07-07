import markdown
import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as docs:
        content = docs.read()
        return markdown.markdown(content)
