from unittest import mock
import datetime
from app.main import outdated_products


@mock.patch("datetime.date")
def test_outdated_products(mock_date: mock) -> None:
    class CustomDate(datetime.date):
        @classmethod
        def today(cls) -> datetime:
            return datetime.date(2025, 1, 2)

    mock_date.side_effect = CustomDate
    products = [
        {"name": "Milk", "expiration_date": datetime.date(2024, 12, 31)},
        {"name": "Eggs", "expiration_date": datetime.date(2025, 1, 5)},
        {"name": "Cheese", "expiration_date": datetime.date(2025, 1, 1)},
    ]

    expected_result = ["Milk", "Cheese"]
    result = outdated_products(products)

    assert result == expected_result
