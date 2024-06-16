from marshmallow import Schema,fields


class ChessProblemRequest(Schema):
    n = fields.Int(required = True)
    k = fields.Int(required = True)
    rq = fields.Int(required = True)
    cq = fields.Int(required = True)
    obstacles = fields.List(fields.List(fields.Int()),required = True)

class StringProblemRequest(Schema):
    t = fields.Str(required=True)    

class ChessProblemResponse(Schema):
    possible_targets = fields.Int(required = True)

class StringProblemResponse(Schema):
    maximum_value = fields.Int(required = True)