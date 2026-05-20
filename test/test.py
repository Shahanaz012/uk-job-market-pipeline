import pytest
import os
from src.extract import extract_data, save_data, extract_start

def test_something():
    result = extract_data("data engineer")
    assert result is not None


def test_extract_data():
    result = extract_data("Data Engineer")
    assert result is not None
    assert type(result) == dict
    assert "results" in result

def test_spaces_replaced():
    keyword = "Data engineer"
    result = keyword.replace(" ", "_")
    assert result == "Data_engineer"