import time
import test_element
import pytest
from modules import get_element_value
from modules import type_in_element
from modules import click_element
from modules import change_language
from modules import clear_input
import test_data

@pytest.mark.parametrize(
    "test_input, expected_output", 
    [test_data.test_data_A_5])
def test_A_2_language_verify(browser, test_input, expected_output):
    # change between two language
    change_language(browser, test_data.test_data_A_4[0])
    change_language(browser, test_input)
    result = get_element_value(browser, test_element.get_info_button)

    assert result == expected_output, 'The button translation is not correct.'