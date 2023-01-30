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


@fixture
def multi_messages_list() -> str:
    return """<msgs>
      <msg>
          <project>Project A</project>
          <pri>proja</pri>
          <seqno>1</seqno>
          <body>This is a Message</body>
          <time>1672531200</time>
      </msg>
      <msg>
          <project>Project B</project>
          <pri>projb</pri>
          <seqno>2</seqno>
          <body>This is another Message</body>
          <time>1672531300</time>
      </msg>
  </msgs>"""


@fixture
def multi_messages_dict() -> dict:
    return {
        "messages": {
            "1": {
                "project": "Project A",
                "pri": "proja",
                "body": "This is a Message",
                "time": 1672531200,
            },
            "2": {
                "project": "Project B",
                "pri": "projb",
                "body": "This is another Message",
                "time": 1672531300,
            },
        }
    }
