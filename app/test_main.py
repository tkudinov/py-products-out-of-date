from unittest import mock
from app.main import outdated_products
import datetime
import pytest


@pytest.fixture()
def products() -> list:
    yield [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

def test_outdated_products(products) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = datetime.date(2022, 2, 2)
        outdated_products(products)
        mocked_date.assert_called_once()
