import pathlib
from src import utils
import pytest


def test_edited_the_information_from_the_transfer():
    assert utils.edited_the_information_from_the_transfer("V G 3654412434951162") == 'V G 3654 41** **** 1162'
    assert utils.edited_the_information_from_the_transfer("Счет 49304996510329747621") == 'Счет **7621'
    assert utils.edited_the_information_from_the_transfer(None) == ""


def test_edited_the_information_from_the_transfer_error():
    with pytest.raises(AttributeError):
        utils.edited_the_information_from_the_transfer(1234)


def test_sorted_operations_list_by_datetime():
    data = [{"date": "2018-12-22T02:02:49.564873"},
            {"date": "2020-12-22T02:02:49.564873"},
            {"date": "2011-12-22T02:02:49.564873"},
            {"date": "2023-12-22T02:02:49.564873"}
            ]
    expected = [{"date": "2023-12-22 02:02:49.564873"},
                {"date": "2020-12-22 02:02:49.564873"},
                {"date": "2018-12-22 02:02:49.564873"},
                {"date": "2011-12-22 02:02:49.564873"},
                ]
    assert utils.sorted_operations_list_by_datetime(data) == expected


def test_sorted_operations_list_by_datetime_error():
    with pytest.raises(ValueError):
        utils.sorted_operations_list_by_datetime([{"date": "2018-12-22T02:02:49"},
                                                  {"date": "2020-12-22"},
                                                  {"date": "02:02:49.564873"},
                                                  {"date": ""}
                                                  ])
    with pytest.raises(KeyError):
        utils.sorted_operations_list_by_datetime([{"data": "2018-12-22T02:02:49"},
                                                  {"date": "2020-12-22"},
                                                  {"date": "02:02:49.564873"},
                                                  {"date": ""}
                                                  ])


def test_formatted_the_date():
    assert utils.formatted_the_date("2019-09-06 00:48:01.081967") == '06.09.2019'
    assert utils.formatted_the_date("2023-11-09 00:48:01.081967") == '09.11.2023'


@pytest.fixture
def test_dict():
    return {
        "id": 736942989,
        "state": "EXECUTED",
        "date": "2019-09-06 00:48:01.081967",
        "operationAmount": {
            "amount": "6357.56",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 3654412434951162",
        "to": "Счет 59986621134048778289"
    }


def test_formatted_the_operation(test_dict):
    assert utils.formatted_the_operation(test_dict) == (f'06.09.2019 Перевод организации\n'
                                                        f'Visa Gold 3654 41** **** 1162 -> Счет **8289\n'
                                                        f'6357.56 USD\n')


def test_load_operations():
    test_file_path = pathlib.Path(__file__).parent.joinpath('data_for_test.json')
    assert utils.load_operations(test_file_path) == [1, 2, 3]
