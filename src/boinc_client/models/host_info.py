from marshmallow import Schema, fields, post_load, pre_load

from boinc_client.models.helpers import normalise_none_to_list


class CoProc(Schema):
    name: fields.Str()


class Host(Schema):
    timezone = fields.Int()
    domain_name = fields.Str()
    ip_addr = fields.Str()
    host_cpid = fields.Str()
    p_ncpus = fields.Int()
    p_vendor = fields.Str(allow_none=True, load_default="")
    p_model = fields.Str(allow_none=True, load_default="")
    p_features = fields.Str()
    p_fpops = fields.Float()
    p_iops = fields.Float()
    p_membw = fields.Float()
    p_calculated = fields.Float()
    p_vm_extensions_disabled = fields.Bool()
    m_nbytes = fields.Float()
    m_cache = fields.Float()
    m_swap = fields.Float()
    d_total = fields.Float()
    d_free = fields.Float()
    os_name = fields.Str()
    os_version = fields.Str()
    n_usable_coprocs = fields.Int()
    coprocs = fields.Nested(CoProc(many=True))
    wsl_available = fields.Bool()

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "coprocs")

    @post_load
    def _a_replace_none_string(self, data, **kwargs):
        for field in data:
            data[field] = data[field] if data[field] is not None else ""
        return data


class HostInfo(Schema):
    host_info = fields.Nested(Host())
