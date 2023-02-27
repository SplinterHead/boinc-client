from marshmallow import Schema, fields, pre_load

from boinc_client.models.helpers import flatten_data, normalise_none_to_list


class PersistentFileTransfer(Schema):
    num_retries = fields.Str()
    first_request_time = fields.Str()
    next_request_time = fields.Str()
    time_so_far = fields.Str()
    last_bytes_xferred = fields.Str()
    is_upload = fields.Str()


class FileTransferDetail(Schema):
    bytes_xferred = fields.Str()
    file_offset = fields.Str()
    xfer_speed = fields.Str()
    url = fields.Str()


class FileTransfer(Schema):
    project_url = fields.Str()
    project_name = fields.Str()
    name = fields.Str()
    nbytes = fields.Str()
    max_nbytes = fields.Str()
    status = fields.Str()
    persistent_file_xfer = fields.Nested(PersistentFileTransfer())
    file_xfer = fields.Nested(FileTransferDetail())


class FileTransfers(Schema):
    file_transfers = fields.Nested(FileTransfer(many=True))

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "file_transfers")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "file_transfers", "file_transfer")
