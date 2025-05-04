from src.read_transact import get_read_csv_transact, get_read_excel_transact
import unittest
from unittest.mock import patch, mock_open


@patch('builtins.open', new_callable=mock_open)
@patch("csv.DictReader")
def test_get_external_csv(mock_csv, mock_file):
    mock_csv.return_value = [{"test": "test"}]
    assert get_read_csv_transact("test") == [{"test": "test"}]
    mock_file.assert_called_once_with("test", encoding='utf-8')
    mock_csv.assert_called_once()


