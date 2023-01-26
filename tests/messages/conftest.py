from pytest import fixture


@fixture
def single_messages_list() -> str:
    return """<msgs>
      <msg>
          <project>Project A</project>
          <pri>proja</pri>
          <seqno>1</seqno>
          <body>This is a Message</body>
          <time>1672531200</time>
      </msg>
  </msgs>"""


@fixture
def single_messages_dict() -> dict:
    return {
        "messages": {
            "1": {
                "project": "Project A",
                "pri": "proja",
                "body": "This is a Message",
                "time": 1672531200,
            }
        }
    }
