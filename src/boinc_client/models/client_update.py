from marshmallow import Schema, fields


class Update(Schema):
    download_url = fields.Url()
    newer_version = fields.Str(allow_none=True)


class ClientUpdate(Schema):
    update = fields.Nested(Update())
