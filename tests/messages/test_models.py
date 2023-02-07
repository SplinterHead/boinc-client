from pytest import mark

from pydantic import BaseModel, Field, validator

from pyboinc.models.message_count import MessageCount


@mark.model
def test_message_count_model_can_parse_data():
    test_json = {"seqno": "2"}
    test_model = MessageCount.parse_obj(test_json)

    assert test_model
    assert test_model.dict() == {"count": 2}


class MessageContent(BaseModel):
    body: str
    pri: str
    project: str
    time: int


class Message(BaseModel):
    __root__: dict[int, MessageContent]

    @validator('__root__', pre=True)
    def create_indexes(cls, val):
        print({val["seqno"]: val})
        return {val["seqno"]: val}


class MessageList(BaseModel):
    messages: list[Message] = Field(alias="msg")


@mark.model
def test_message_model_can_parse_data(single_messages_json, single_messages_dict):
    test_model = MessageList.parse_obj(single_messages_json)

    assert test_model
    assert test_model.dict() == single_messages_dict
