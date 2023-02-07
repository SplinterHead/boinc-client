from pydantic import BaseModel, Field


class SemanticVersion(BaseModel):
    major: int
    minor: int
    patch: int = Field(alias="release")


class ClientVersion(BaseModel):
    version: SemanticVersion = Field(alias="server_version")

    def sem_ver(self) -> str:
        return f"v{self.version.major}.{self.version.minor}.{self.version.patch}"
