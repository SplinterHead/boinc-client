from marshmallow import Schema, fields


class Version(Schema):
    major = fields.Int()
    minor = fields.Int()
    patch = fields.Int(data_key="release")


class ClientVersion(Schema):
    version = fields.Nested(Version(), data_key="server_version")
