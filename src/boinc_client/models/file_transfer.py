from marshmallow import Schema, fields, pre_load

from boinc_client.models.helpers import flatten_data, normalise_none_to_list


class PersistentFileTransfer(Schema):
    first_request_time = fields.Str()
    is_upload = fields.Str()
    last_bytes_xferred = fields.Str()
    next_request_time = fields.Str()
    num_retries = fields.Str()
    time_so_far = fields.Str()


class FileTransferDetail(Schema):
    bytes_xferred = fields.Str()
    file_offset = fields.Str()
    url = fields.Str()
    xfer_speed = fields.Str()


class FileTransfer(Schema):
    file_xfer = fields.Nested(FileTransferDetail())
    max_nbytes = fields.Str()
    name = fields.Str()
    nbytes = fields.Str()
    persistent_file_xfer = fields.Nested(PersistentFileTransfer())
    project_name = fields.Str()
    project_url = fields.Str()
    status = fields.Str()


class FileTransfers(Schema):
    file_transfers = fields.Nested(FileTransfer(many=True))

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "file_transfers")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "file_transfers", "file_transfer")
