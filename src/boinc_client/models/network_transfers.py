import datetime as dt

from marshmallow import Schema, fields, post_load, pre_load

from boinc_client.models.helpers import (
    create_indexes,
    flatten_data,
    normalise_none_to_list,
    remove_key,
)


def _epoch_to_date(epoch_days: str) -> str:
    epoch = dt.date(1970, 1, 1)
    delta = dt.timedelta(days=int(epoch_days))
    return (epoch + delta).strftime("%Y-%m-%d")


class Transfer(Schema):
    down = fields.Float()
    up = fields.Float()
    when = fields.Int()

    @post_load
    def _a_remove_when(self, data, **kwargs):
        return remove_key(data, "when")


class DailyTransfers(Schema):
    network_transfers = fields.Dict(
        fields.Str(), fields.Nested(Transfer()), data_key="daily_xfers"
    )

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "daily_xfers")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "daily_xfers", "dx")

    @pre_load
    def _c_create_dict_keys(self, data, **kwargs):
        data["daily_xfers"] = {
            _epoch_to_date(dx["when"]): dx for dx in data["daily_xfers"]
        }
        return data
