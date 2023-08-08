from datetime import datetime

from marshmallow import Schema, fields, post_load, pre_load

from boinc_client.models.helpers import flatten_data, normalise_none_to_list, remove_key


def _convert_epoch(epoch: str):
    epoch_date = datetime.fromtimestamp(float(epoch))
    return epoch_date.strftime("%Y-%m-%d")


class DailyStats(Schema):
    day = fields.Float()
    host_expavg_credit = fields.Float()
    host_total_credit = fields.Float()
    user_expavg_credit = fields.Float()
    user_total_credit = fields.Float()

    @post_load
    def _remove_day(self, data, **kwargs):
        return remove_key(data, "day")


class Project(Schema):
    daily_statistics = fields.Dict(fields.Str(), fields.Nested(DailyStats()))
    master_url = fields.Str()

    @pre_load
    def _create_dict_keys(self, data, **kwargs):
        data["daily_statistics"] = {
            _convert_epoch(day["day"]): day for day in data["daily_statistics"]
        }
        return data


class ProjectStats(Schema):
    project_stats = fields.Nested(Project(many=True), data_key="statistics")

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "statistics")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "statistics", "project_statistics")
