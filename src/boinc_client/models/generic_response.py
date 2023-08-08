from marshmallow import Schema, fields, pre_load


class GenericResponse(Schema):
    error = fields.Str(allow_none=True)
    success = fields.Bool()

    @pre_load
    def _fill_success(self, data, **kwargs):
        data["success"] = "success" in data
        return data
