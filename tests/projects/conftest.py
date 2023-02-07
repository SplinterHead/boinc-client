from pytest import fixture


@fixture
def single_project_single_platform_xml() -> str:
    return """<projects>
            <project>
                <name>test_project</name>
                <url>test_url</url>
                <general_area>test_area</general_area>
                <specific_area>test_s_area</specific_area>
                <description>test_desc</description>
                <home>test_home</home>
                <platforms>
                    <name>test_platform</name>
                </platforms>
                <summary>test_summary</summary>
            </project>
        </projects>"""


@fixture
def single_project_single_platform_json() -> dict:
    return {
        "project": [
            {
                "name": "test_project",
                "url": "test_url",
                "general_area": "test_area",
                "specific_area": "test_s_area",
                "description": "test_desc",
                "home": "test_home",
                "platforms": {"name": "test_platform"},
                "summary": "test_summary",
            }
        ]
    }


@fixture
def single_project_single_platform_dict() -> dict:
    return {
        "projects": [
            {
                "name": "test_project",
                "url": "test_url",
                "general_area": "test_area",
                "specific_area": "test_s_area",
                "description": "test_desc",
                "home": "test_home",
                "platforms": [
                    {"name": "test_platform"},
                ],
                "summary": "test_summary",
            }
        ]
    }


@fixture
def single_project_multi_platform_xml() -> str:
    return """<projects>
            <project>
                <name>test_project</name>
                <url>test_url</url>
                <general_area>test_area</general_area>
                <specific_area>test_s_area</specific_area>
                <description>test_desc</description>
                <home>test_home</home>
                <platforms>
                    <name>test_platform</name>
                    <name>test_platform2</name>
                    <name>test_platform3</name>
                </platforms>
                <summary>test_summary</summary>
            </project>
        </projects>"""


@fixture
def single_project_multi_platform_json() -> dict:
    return {
        "project": [
            {
                "name": "test_project",
                "url": "test_url",
                "general_area": "test_area",
                "specific_area": "test_s_area",
                "description": "test_desc",
                "home": "test_home",
                "platforms": {
                    "name": ["test_platform", "test_platform2", "test_platform3"]
                },
                "summary": "test_summary",
            }
        ]
    }


@fixture
def single_project_multi_platform_dict() -> dict:
    return {
        "projects": [
            {
                "name": "test_project",
                "url": "test_url",
                "general_area": "test_area",
                "specific_area": "test_s_area",
                "description": "test_desc",
                "home": "test_home",
                "platforms": [
                    {"name": "test_platform"},
                    {"name": "test_platform2"},
                    {"name": "test_platform3"},
                ],
                "summary": "test_summary",
            }
        ]
    }


@fixture
def multi_project_single_platform_xml() -> str:
    return """<projects>
            <project>
                <name>test_project</name>
                <url>test_url</url>
                <general_area>test_area</general_area>
                <specific_area>test_s_area</specific_area>
                <description>test_desc</description>
                <home>test_home</home>
                <platforms>
                    <name>test_platform</name>
                </platforms>
                <summary>test_summary</summary>
            </project>
            <project>
                <name>test_project_2</name>
                <url>test_url_2</url>
                <general_area>test_area_2</general_area>
                <specific_area>test_s_area_2</specific_area>
                <description>test_desc_2</description>
                <home>test_home_2</home>
                <platforms>
                    <name>test_platform_2</name>
                </platforms>
                <summary>test_summary_2</summary>
            </project>
        </projects>"""


@fixture
def multi_project_single_platform_json() -> dict:
    return {
        "project": [
            {
                "name": "test_project",
                "url": "test_url",
                "general_area": "test_area",
                "specific_area": "test_s_area",
                "description": "test_desc",
                "home": "test_home",
                "platforms": {"name": "test_platform"},
                "summary": "test_summary",
            },
            {
                "name": "test_project_2",
                "url": "test_url_2",
                "general_area": "test_area_2",
                "specific_area": "test_s_area_2",
                "description": "test_desc_2",
                "home": "test_home_2",
                "platforms": {"name": "test_platform_2"},
                "summary": "test_summary_2",
            },
        ]
    }


@fixture
def multi_project_single_platform_dict() -> dict:
    return {
        "projects": [
            {
                "name": "test_project",
                "url": "test_url",
                "general_area": "test_area",
                "specific_area": "test_s_area",
                "description": "test_desc",
                "home": "test_home",
                "platforms": [
                    {"name": "test_platform"},
                ],
                "summary": "test_summary",
            },
            {
                "name": "test_project_2",
                "url": "test_url_2",
                "general_area": "test_area_2",
                "specific_area": "test_s_area_2",
                "description": "test_desc_2",
                "home": "test_home_2",
                "platforms": [
                    {"name": "test_platform_2"},
                ],
                "summary": "test_summary_2",
            },
        ]
    }
