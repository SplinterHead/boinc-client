from marshmallow import Schema, fields

from boinc_client.models.result import Result


class ScreensaverTask(Schema):
    results = fields.Nested(Result(many=True), data_key="result", load_default=[])
    suspend_reason = fields.Int()


class ScreensaverTasks(Schema):
    screensaver_tasks = fields.Nested(
        ScreensaverTask(), data_key="handle_get_screensaver_tasks"
    )
