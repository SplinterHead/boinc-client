from pydantic import BaseModel, Field


class Update(BaseModel):
    version: str = Field(alias="newer_version")
    url: str = Field(alias="download_url")


class ClientUpdate(BaseModel):
    update: Update
