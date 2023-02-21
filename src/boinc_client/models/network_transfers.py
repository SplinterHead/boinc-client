import datetime as dt

from marshmallow import Schema, fields, post_load, pre_load


def _epoch_to_date(epoch_days: str) -> str:
    epoch = dt.date(1970, 1, 1)
    delta = dt.timedelta(days=int(epoch_days))
    return (epoch + delta).strftime("%Y-%m-%d")


class Transfer(Schema):
    when = fields.Int()
    up = fields.Float()
    down = fields.Float()

    @post_load
    def _remove_date(self, data, **kwargs):
        del data["when"]
        return data


class DailyTransfers(Schema):
    network_transfers = fields.Dict(
        fields.Str(), fields.Nested(Transfer()), data_key="daily_xfers"
    )

    @pre_load
    def _convert_none_to_empty_dict(self, data, **kwargs):
        data["daily_xfers"] = (
            {} if not data["daily_xfers"] else data["daily_xfers"]["dx"]
        )
        return data

    @pre_load
    def _create_dict_keys(self, data, **kwargs):
        data["daily_xfers"] = {
            _epoch_to_date(dx["when"]): dx for dx in data["daily_xfers"]
        }
        return data
