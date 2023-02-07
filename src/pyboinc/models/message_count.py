from pydantic import BaseModel, Field


class MessageCount(BaseModel):
    count: int = Field(alias="seqno")
