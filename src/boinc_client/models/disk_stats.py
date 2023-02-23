from marshmallow import Schema, fields


class ProjectDiskStats(Schema):
    master_url = fields.Str()
    disk_usage = fields.Float()


class DiskStats(Schema):
    projects = fields.Nested(
        ProjectDiskStats(many=True),
        data_key="project",
        allow_none=True,
        load_default=[],
    )
    d_total = fields.Float()
    d_free = fields.Float()
    d_boinc = fields.Float()
    d_allowed = fields.Float()


class DiskUsage(Schema):
    disk_stats = fields.Nested(DiskStats(), data_key="disk_usage_summary")
