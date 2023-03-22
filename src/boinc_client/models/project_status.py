from marshmallow import Schema, fields, post_load, pre_load

from boinc_client.models.helpers import (
    create_lists,
    flatten_data,
    normalise_none_to_list,
    replace_none_string,
    set_bools,
)


class RscBackoffTime(Schema):
    name = fields.Str()
    value = fields.Float()


class RscBackoffInterval(Schema):
    name = fields.Str()
    value = fields.Float()


class GuiUrl(Schema):
    name = fields.Str()
    description = fields.Str()
    url = fields.Url()


class ProjectState(Schema):
    master_url = fields.Str()
    project_name = fields.Str()
    symstore = fields.Str(allow_none=True)
    user_name = fields.Str(allow_none=True)
    team_name = fields.Str(allow_none=True)
    host_venue = fields.Str(allow_none=True)
    email_hash = fields.Str(allow_none=True)
    cross_project_id = fields.Str(allow_none=True)
    external_cpid = fields.Str(allow_none=True)
    cpid_time = fields.Float()
    user_total_credit = fields.Float()
    user_expavg_credit = fields.Float()
    user_create_time = fields.Float()
    rpc_seqno = fields.Int()
    userid = fields.Int()
    teamid = fields.Int()
    hostid = fields.Int()
    host_total_credit = fields.Float()
    host_expavg_credit = fields.Float()
    host_create_time = fields.Float()
    nrpc_failures = fields.Int()
    master_fetch_failures = fields.Int()
    min_rpc_time = fields.Float()
    next_rpc_time = fields.Float()
    rec = fields.Float()
    rec_time = fields.Float()
    resource_share = fields.Float()
    disk_usage = fields.Float()
    disk_share = fields.Float()
    desired_disk_usage = fields.Float()
    duration_correction_factor = fields.Float()
    sched_rpc_pending = fields.Int()
    send_time_stats_log = fields.Int()
    send_job_log = fields.Int()
    njobs_success = fields.Int()
    njobs_error = fields.Int()
    elapsed_time = fields.Float()
    last_rpc_time = fields.Float()
    dont_use_dcf = fields.Bool()
    master_url_fetch_pending = fields.Bool()
    scheduler_rpc_in_progress = fields.Bool()
    rsc_backoff_time = fields.Nested(RscBackoffTime())
    rsc_backoff_interval = fields.Nested(RscBackoffInterval())
    gui_urls = fields.Nested(GuiUrl(many=True))
    sched_priority = fields.Float()
    project_files_downloaded_time = fields.Float()
    project_dir = fields.Str()

    @pre_load
    def _a_create_keys(self, data, **kwargs):
        return create_lists(data, ["gui_urls"])

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "gui_urls", "gui_url")

    @pre_load
    def _c_set_bools(self, data, **kwargs):
        return set_bools(
            data,
            ["dont_use_dcf", "master_url_fetch_pending", "scheduler_rpc_in_progress"],
        )

    @post_load
    def _a_replace_none_string(self, data, **kwargs):
        return replace_none_string(data)


class ProjectStatus(Schema):
    project_status = fields.Nested(ProjectState(many=True), data_key="projects")

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "projects")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "projects", "project")
