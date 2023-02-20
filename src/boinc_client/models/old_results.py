from marshmallow import Schema, fields, pre_load


class OldResult(Schema):
    project_url = fields.Url()
    result_name = fields.Str()
    app_name = fields.Str()
    exit_status = fields.Int()
    elapsed_time = fields.Float()
    cpu_time = fields.Float()
    completed_time = fields.Float()
    create_time = fields.Float()


class OldResultList(Schema):
    old_results = fields.Nested(OldResult(many=True))

    @pre_load
    def _convert_none_to_empty_list(self, data, **kwargs):
        data["old_results"] = (
            data["old_results"]["old_result"] if data["old_results"] else []
        )
        return data
