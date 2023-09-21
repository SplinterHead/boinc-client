from marshmallow import Schema, fields


class Status(Schema):
    ams_password_error = fields.Int()
    disallow_attach = fields.Int()
    gpu_mode = fields.Int()
    gpu_mode_delay = fields.Float()
    gpu_mode_perm = fields.Int()
    gpu_suspend_reason = fields.Int()
    max_event_log_lines = fields.Int()
    network_mode = fields.Int()
    network_mode_delay = fields.Float()
    network_mode_perm = fields.Int()
    network_status = fields.Int()
    network_suspend_reason = fields.Int()
    simple_gui_only = fields.Int()
    task_mode = fields.Int()
    task_mode_delay = fields.Float()
    task_mode_perm = fields.Int()
    task_suspend_reason = fields.Int()


class CCStatus(Schema):
    cc_status = fields.Nested(Status())
