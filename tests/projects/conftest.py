from pytest import fixture


@fixture
def empty_project_list_xml() -> str:
    return ""


@fixture
def empty_project_list_dict() -> dict:
    return {"projects": []}


@fixture
def single_project_single_platform_xml(test_files) -> str:
    return open(f"{test_files}/projects/single_project_single_platform.xml").read()


@fixture
def single_project_single_platform_dict() -> dict:
    return {
        "projects": [
            {
                "id": 51,
                "name": "SIDock@home",
                "url": "https://www.sidock.si/sidock/",
                "web_url": "https://www.sidock.si/sidock/",
                "general_area": "Biology and Medicine",
                "specific_area": "Biomedicine",
                "description": "Study drugs to fight SARS-CoV-2",
                "home": "The COVID.SI project and the Karelian Research Center of the Russian Academy of Sciences",
                "platforms": [
                    {"name": "x86_64-pc-linux-gnu"},
                ],
                "image": "https://boinc.berkeley.edu/images/sidock.png",
                "summary": "Study drugs to fight SARS-CoV-2",
                "keywords": "9 13 64 20 44",
            }
        ]
    }


@fixture
def single_project_multi_platform_xml(test_files) -> str:
    return open(f"{test_files}/projects/single_project_multi_platform.xml").read()


@fixture
def single_project_multi_platform_dict() -> dict:
    return {
        "projects": [
            {
                "id": 51,
                "name": "SIDock@home",
                "url": "https://www.sidock.si/sidock/",
                "web_url": "https://www.sidock.si/sidock/",
                "general_area": "Biology and Medicine",
                "specific_area": "Biomedicine",
                "description": "Study drugs to fight SARS-CoV-2",
                "home": "The COVID.SI project and the Karelian Research Center of the Russian Academy of Sciences",
                "platforms": [
                    {"name": "windows_x86_64"},
                    {"name": "x86_64-pc-linux-gnu"},
                    {"name": "arm-unknown-linux-gnueabihf"},
                    {"name": "x86_64-openwrt-linux-musl"},
                ],
                "image": "https://boinc.berkeley.edu/images/sidock.png",
                "summary": "Study drugs to fight SARS-CoV-2",
                "keywords": "9 13 64 20 44",
            }
        ]
    }


@fixture
def multi_project_single_platform_xml(test_files) -> str:
    return open(f"{test_files}/projects/multi_project_multi_platform.xml").read()


@fixture
def multi_project_single_platform_dict() -> dict:
    return {
        "projects": [
            {
                "id": 51,
                "name": "SIDock@home",
                "url": "https://www.sidock.si/sidock/",
                "web_url": "https://www.sidock.si/sidock/",
                "general_area": "Biology and Medicine",
                "specific_area": "Biomedicine",
                "description": "Study drugs to fight SARS-CoV-2",
                "home": "The COVID.SI project and the Karelian Research Center of the Russian Academy of Sciences",
                "platforms": [
                    {"name": "windows_x86_64"},
                    {"name": "x86_64-pc-linux-gnu"},
                    {"name": "arm-unknown-linux-gnueabihf"},
                    {"name": "x86_64-openwrt-linux-musl"},
                ],
                "image": "https://boinc.berkeley.edu/images/sidock.png",
                "summary": "Study drugs to fight SARS-CoV-2",
                "keywords": "9 13 64 20 44",
            },
            {
                "id": 4,
                "name": "DENIS@Home",
                "url": "https://denis.usj.es/denisathome/",
                "web_url": "https://denis.usj.es/denisathome/",
                "general_area": "Biology and Medicine",
                "specific_area": "Medical physiology",
                "description": "DENIS@Home does cardiac electrophysiological simulations, studying the electrical activity of the heart.",
                "home": "San Jorge University, Zaragoza, Spain",
                "platforms": [
                    {"name": "windows_x86_64"},
                    {"name": "x86_64-pc-linux-gnu"},
                    {"name": "x86_64-apple-darwin"},
                    {"name": "aarch64-unknown-linux-gnu"},
                    {"name": "arm64-apple-darwin"},
                ],
                "summary": "Study the physiology of the heart",
                "keywords": "9 20 30",
            },
        ]
    }


@fixture
def mock_project_url() -> str:
    return "https://mockprojectgrid.org/"


@fixture
def mock_project_key() -> str:
    return "mock_1234567890"


@fixture
def project_attach_poll_success_xml(test_files) -> str:
    return open(f"{test_files}/project_attach/poll_success.xml").read()


@fixture
def project_attach_poll_success_dict() -> dict:
    return {"project_attach_reply": {"error_num": 0}}


@fixture
def project_attach_poll_failure_xml(test_files) -> str:
    return open(f"{test_files}/project_attach/poll_failure.xml").read()


@fixture
def project_attach_poll_failure_dict() -> dict:
    return {"project_attach_reply": {"messages": ["Failed to connect"], "error_num": 1}}
