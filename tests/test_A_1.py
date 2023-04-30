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
    [test_data.test_data_A_1, 
     test_data.test_data_A_2, 
     test_data.test_data_A_3, 
     test_data.test_data_A_4])
def test_A_1_language_verify(browser, test_input, expected_output):
    change_language(browser, test_input)
    click_element(browser, test_element.do_you_have_question_field)
    result = get_element_value(browser, test_element.get_info_button)

    assert result == expected_output, 'The button translation is not correct.'
