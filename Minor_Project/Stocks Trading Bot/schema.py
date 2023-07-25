from marshmallow import Schema, fields

class PlainUserSignupSchema(Schema):
    username = fields.Str(required=True, unique=True)
    first_name = fields.Str(required=True)
    last_name=fields.Str(required=True)
    password = fields.Str(required=True)
    conf_password = fields.Str(required=True)
    age=fields.Int(required=True)
    balance=fields.Int(required=True,dump_only=True)
    isSuspended=fields.Boolean(required=True,dump_only=True)


class PlainLoginSchema(Schema):
    username=fields.String(required=True,unique=True)
    password=fields.String(required=True)

class InfoSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    age=fields.Int(required=True)
    balance=fields.Int(required=True)
    username=fields.Str(required=True)

class AdminDetailSchema(Schema):
    id=fields.Int(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    age=fields.Int(required=True)
    balance=fields.Int(required=True)
    username=fields.Str(required=True)

class ChangeRoleSchema(Schema):
    username=fields.Str(required=True)

class  SingleUserSchema(Schema):
    username=fields.Str(required=True)

class StockSchema(Schema):
    name=fields.Str(required=True)
    token=fields.Str(required=True)

class UserSignupSchema(PlainUserSignupSchema):
    role=fields.List(fields.Nested(lambda:PlainUserSignupSchema()),dump_only=True)


class BuySchema(Schema):
    stock=fields.Str(required=True)
    quantity=fields.Int(required=True)

class MoneySchema(Schema):
    balance=fields.Int(required=True)




    """first_name = db.Column(db.String(80),nullable=False)
    last_name=db.Column(db.String(80),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    balance=db.Column(db.Float,nullable=False)
    isSuspended=db.Column(db.Boolean,nullable=False)"""