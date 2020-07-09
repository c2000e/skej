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

@app.route('/deadlines', methods=['GET'])
def get_deadlines():
    deadlines = DeadlineModel.query.all()
    result = deadlines_schema.dump(deadlines)
    return {'message': 'Found all deadlines.', 'deadlines': result}, 200

@app.route('/deadlines', methods=['POST'])
def create_deadline():
    json_data = request.get_json()

    # ensure data actually exists
    if not json_data:
        return {'message': 'No input data provided.'}, 400

    # validate and deserialize input
    try:
        data = deadline_schema.load(json_data)
    except ValidationError as e:
        return e.messages, 422

    # check if deadline already exists
    name, date = data['name'], data['date']
    deadline = DeadlineModel.query.filter_by(name=name).first()

    if deadline is None:
        deadline = DeadlineModel(name, date)

        db.session.add(deadline)
        db.session.commit()

        result = deadline_schema.dump(deadline);
        return {'message': 'Created new deadline', 'deadline': result}, 201

    result = deadline_schema.dump(deadline);
    return {'message': 'Deadline already exists', 'deadline': result}, 422
    
@app.route('/deadlines/<string:name>', methods=['GET'])
def get_deadline(name):
    deadline = DeadlineModel.query.filter_by(name=name).first()
    if deadline is None:
        return {'message': 'Deadline could not be found.'}, 404
    result = deadline_schema.dump(deadline)
    return {'message': 'Deadline found.', 'deadline': result}, 200

@app.route('/deadlines/<string:name>', methods=['PATCH'])
def update_deadline(name):
    json_data = request.get_json()

    # ensure data actually exists
    if not json_data:
        return {'message:': 'No input data provided.'}, 400

    # validate and deserialize input
    try:
        data = deadline_update_schema.load(json_data)
    except ValidationError as e:
        return e.messages, 422

    # ensure deadline exists
    deadline = DeadlineModel.query.filter_by(name=name).first()
    if deadline is None:
        return {'message': 'Deadline could not be found.'}, 404

    if 'name' in data: 
        deadline.name = data['name']
    if 'date' in data:
        deadline.date = data['date']
    if 'status' in data:
        deadline.status = data['status']

    db.session.commit()

    result = deadline_schema.dump(deadline)
    return {'message': 'Updated deadline.', 'deadline': result}, 200

@app.route('/deadlines/<string:name>', methods=['DELETE'])
def delete_deadline(name):
    deadline = DeadlineModel.query.filter_by(name=name).first()
    if deadline is None:
        return {'message': 'Deadline could not be found.'}, 404
    db.session.delete(deadline)
    db.session.commit()
    return {'message': 'Deadline deleted.'}, 204

