from marshmallow import Schema, fields, pre_load

from boinc_client.models.helpers import flatten_data, normalise_none_to_list


class ProjectPlatform(Schema):
    name = fields.Str()


class Project(Schema):
    name = fields.Str()
    id = fields.Int()
    url = fields.Url()
    web_url = fields.Url()
    general_area = fields.Str()
    specific_area = fields.Str()
    description = fields.Str()
    home = fields.Str()
    platforms = fields.Nested(ProjectPlatform(many=True))
    image = fields.Str()
    summary = fields.Str()
    keywords = fields.Str()

    @pre_load
    def _convert_platform_dict_to_list(self, data, **kwargs):
        data["platforms"] = (
            [{"name": d} for d in data["platforms"]["name"]]
            if type(data["platforms"]["name"]) == list
            else [data["platforms"]]
        )
        return data


class Projects(Schema):
    projects = fields.Nested(Project(many=True))

    @pre_load
    def _a_normalise_none(self, data, **kwargs):
        return normalise_none_to_list(data, "projects")

    @pre_load
    def _b_flatten_data(self, data, **kwargs):
        return flatten_data(data, "projects", "project")
