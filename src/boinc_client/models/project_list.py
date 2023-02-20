from marshmallow import Schema, fields, pre_load


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


class ProjectList(Schema):
    projects = fields.Nested(Project(many=True))

    @pre_load
    def _convert_none_to_empty_list(self, data, **kwargs):
        data["projects"] = data["projects"]["project"] if data["projects"] else []
        return data
