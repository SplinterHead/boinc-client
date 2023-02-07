from pytest import fixture


@fixture
def single_messages_xml() -> str:
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
def single_messages_json() -> dict:
    return {
        "msg": [
            {
                "project": "Project A",
                "pri": "proja",
                "seqno": "1",
                "body": "This is a Message",
                "time": "1672531200",
            }
        ]
    }


@fixture
def single_messages_dict() -> dict:
    return {
        "messages": {
            1: {
                "project": "Project A",
                "pri": "proja",
                "body": "This is a Message",
                "time": 1672531200,
            }
        }
    }


@fixture
def multi_messages_xml() -> str:
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


@fixture
def single_notice_xml() -> str:
    return """<notices>
        <notice>
            <title>Notice A</title>
            <description>This is a notice</description>
            <create_time>123</create_time>
            <arrival_time>124</arrival_time>
            <is_private>false</is_private>
            <project_name>proja</project_name>
            <category>test</category>
            <link>https://linky.link</link>
            <seqno>1</seqno>
        </notice>
    </notices>
"""


@fixture
def single_notice_dict() -> dict:
    return {
        "notices": {
            "1": {
                "title": "Notice A",
                "description": "This is a notice",
                "create_time": 123,
                "arrival_time": 124,
                "is_private": False,
                "project_name": "proja",
                "category": "test",
                "link": "https://linky.link",
            }
        }
    }


@fixture
def multi_notice_xml() -> str:
    return """<notices>
        <notice>
            <title>Notice A</title>
            <description>This is a notice</description>
            <create_time>123</create_time>
            <arrival_time>124</arrival_time>
            <is_private>false</is_private>
            <project_name>proja</project_name>
            <category>test</category>
            <link>https://linky.link</link>
            <seqno>1</seqno>
        </notice>
        <notice>
            <title>Notice B</title>
            <description>This is another notice</description>
            <create_time>456</create_time>
            <arrival_time>457</arrival_time>
            <is_private>false</is_private>
            <project_name>projb</project_name>
            <category>test2</category>
            <link>https://linky2.link</link>
            <seqno>2</seqno>
        </notice>
    </notices>
"""


@fixture
def multi_notice_dict() -> dict:
    return {
        "notices": {
            "1": {
                "title": "Notice A",
                "description": "This is a notice",
                "create_time": 123,
                "arrival_time": 124,
                "is_private": False,
                "project_name": "proja",
                "category": "test",
                "link": "https://linky.link",
            },
            "2": {
                "title": "Notice B",
                "description": "This is another notice",
                "create_time": 456,
                "arrival_time": 457,
                "is_private": False,
                "project_name": "projb",
                "category": "test2",
                "link": "https://linky2.link",
            },
        }
    }
