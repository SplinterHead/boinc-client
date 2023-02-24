from marshmallow import Schema, fields, pre_load

from boinc_client.models.helpers import flatten_data, normalise_none_to_list


class OldResult(Schema):
    project_url = fields.Url()
    result_name = fields.Str()
    app_name = fields.Str()
    exit_status = fields.Int()
    elapsed_time = fields.Float()
    cpu_time = fields.Float()
    completed_time = fields.Float()
    create_time = fields.Float()


class OldResults(Schema):
    old_results = fields.Nested(OldResult(many=True))

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "old_results")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "old_results", "old_result")
