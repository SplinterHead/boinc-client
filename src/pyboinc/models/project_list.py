from pydantic import BaseModel, Field, validator


class PlatformName(BaseModel):
    name: str


class Project(BaseModel):
    name: str
    url: str
    general_area: str
    specific_area: str
    description: str
    home: str
    platforms: list[PlatformName]
    summary: str

    @validator("platforms", pre=True)
    def platform_name_list_to_dict(cls, val):
        ret = [{"name": n} for n in val["name"]] if type(val["name"]) == list else val
        return ret

    @validator("platforms", pre=True)
    def to_list(cls, val):
        ret = [val] if type(val) == dict else val
        return ret


class ProjectList(BaseModel):
    projects: list[Project] = Field(alias="project")
