"""Contains tests for user routes."""

import pytest
from httpx import AsyncClient
from src.repositories import UserRepository
from src.schemas.user import UserFilters

from tests.fixtures import testing_cases
from tests.utils import RequestTestCase, prepare_payload


class TestUserRouter:

    @staticmethod
    @pytest.mark.usefixtures('setup_companies')
    @pytest.mark.parametrize('case', testing_cases.TEST_USER_ROUTE_CREATE_PARAMS)
    async def test_create(
        case: RequestTestCase,
        async_client: AsyncClient,
    ) -> None:
        with case.expected_error:
            response = await async_client.post(case.url, json=case.data, headers=case.headers)
            assert response.status_code == case.expected_status
            assert prepare_payload(response, ['id']) == case.expected_data

    @staticmethod
    @pytest.mark.usefixtures('setup_users')
    @pytest.mark.parametrize('case', testing_cases.TEST_USER_ROUTE_GET_PARAMS)
    async def test_get(
        case: RequestTestCase,
        async_client: AsyncClient,
    ) -> None:
        with case.expected_error:
            response = await async_client.get(case.url, headers=case.headers)
            assert response.status_code == case.expected_status
            assert prepare_payload(response) == case.expected_data

    @staticmethod
    @pytest.mark.usefixtures('setup_users')
    async def test_get_filters_delegates_filters_contract(
        async_client: AsyncClient,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        captured_filters: UserFilters | None = None

        async def _get_users_by_filters_stub(self: UserRepository, filters: UserFilters) -> list:
            nonlocal captured_filters
            captured_filters = filters
            return []

        monkeypatch.setattr(UserRepository, 'get_users_by_filters', _get_users_by_filters_stub)

        response = await async_client.get('/api/user/filters/?first_name=Ivan&last_name=Ivanov')

        assert response.status_code == 200
        assert prepare_payload(response) == []
        assert isinstance(captured_filters, UserFilters)
        assert captured_filters.first_name == ['Ivan']
        assert captured_filters.last_name == ['Ivanov']
        assert captured_filters.ids is None
