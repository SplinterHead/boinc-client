from dataclasses import dataclass
from pytest import mark

from pyboinc.models.project_list import ProjectList


@dataclass
class TestCase:
    __test__ = False

    description: str
    test_data: str
    output: str


test_cases = [
    TestCase(
        description="Single Project, Single Platform",
        test_data="single_project_single_platform_json",
        output="single_project_single_platform_dict",
    ),
    TestCase(
        description="Single Project, Multiple Platform",
        test_data="single_project_multi_platform_json",
        output="single_project_multi_platform_dict"
    ),
    TestCase(
        description="Multiple Project, Single Platform",
        test_data="multi_project_single_platform_json",
        output="multi_project_single_platform_dict"
    ),
]


@mark.model
@mark.parametrize("test_case", test_cases, ids=[tc.description for tc in test_cases])
def test_project_model_can_parse_data(test_case, request):
    test_model = ProjectList.parse_obj(request.getfixturevalue(test_case.test_data))

    assert test_model
    assert test_model.dict() == request.getfixturevalue(test_case.output)
