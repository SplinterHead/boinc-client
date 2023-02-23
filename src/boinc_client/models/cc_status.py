from marshmallow import Schema, fields


class Status(Schema):
    network_status = fields.Int()
    ams_password_error = fields.Int()
    task_suspend_reason = fields.Int()
    task_mode = fields.Int()
    task_mode_perm = fields.Int()
    task_mode_delay = fields.Float()
    gpu_suspend_reason = fields.Int()
    gpu_mode = fields.Int()
    gpu_mode_perm = fields.Int()
    gpu_mode_delay = fields.Float()
    network_suspend_reason = fields.Int()
    network_mode = fields.Int()
    network_mode_perm = fields.Int()
    network_mode_delay = fields.Float()
    disallow_attach = fields.Int()
    simple_gui_only = fields.Int()
    max_event_log_lines = fields.Int()


class CCStatus(Schema):
    cc_status = fields.Nested(Status())
