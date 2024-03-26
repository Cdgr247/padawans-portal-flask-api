from marshmallow import Schema, fields

# class UserSchema(Schema):
#     id = fields.Str(dump_only=True)
#     username = fields.Str(required=True)
#     email = fields.Str(required=True)
#     password = fields.Str(required=True, load_only = True)
#     first_name= fields.Str()
#     last_name= fields.Str()

# class PostSchema(Schema):
#     id = fields.Str(dump_only=True)
#     title = fields.Str()
#     body = fields.Str(required=True)
#     author = fields.Int(required=True)

class CarSchema(Schema):
    id = fields.Str(dump_only=True)
    model = fields.Str(required=True)
    make = fields.Str(required=True)

class SaleReceiptsSchema(Schema):
    id = fields.Str(dump_only=True)
    color = fields.Str(required=True)
    model = fields.Str(required=True)
    make = fields.Str(required=True)
    salesman = fields.Str(required=True)
    sale = fields.Int(required=True)