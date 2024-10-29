from http.client import responses
from lesson1.api_tests.case.pom.case import create_case
from lesson1.api_tests.case.data.case import create_case_dict
from lesson1.api_tests.case.models.case import Case
from lesson1.api_tests.utils.api_client import client

def test_create_case():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 0,
            "name": "string",
            "description": "string",
            "steps": ["string"],
            "expected_result": "string",
            "priority": "низкий"
        }
    )

    response.status_code_should_be_eq(200)


def test_delete_case():
    response = client.make_request(
        handle="/testcases/0",
        method="DELETE"
    )
    response.status_code_should_be_eq(200)