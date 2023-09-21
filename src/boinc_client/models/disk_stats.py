from marshmallow import Schema, fields


class ProjectDiskStats(Schema):
    disk_usage = fields.Float()
    master_url = fields.Str()


class DiskStats(Schema):
    d_allowed = fields.Float()
    d_boinc = fields.Float()
    d_free = fields.Float()
    d_total = fields.Float()
    projects = fields.Nested(
        ProjectDiskStats(many=True),
        data_key="project",
        allow_none=True,
        load_default=[],
    )


class DiskUsage(Schema):
    disk_stats = fields.Nested(DiskStats(), data_key="disk_usage_summary")
