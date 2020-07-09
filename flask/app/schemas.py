import datetime

from marshmallow import Schema, fields

class DeadlineSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    date = fields.DateTime(required=True)
    status = fields.Str()

class DeadlineUpdateSchema(Schema):
    name = fields.Str()
    date = fields.DateTime()
    status = fields.Str()

deadline_schema = DeadlineSchema()
deadlines_schema = DeadlineSchema(many=True)
deadline_update_schema = DeadlineUpdateSchema()
