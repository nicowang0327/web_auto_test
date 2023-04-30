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
    [test_data.test_data_B_2_1, test_data.test_data_B_2_2, test_data.test_data_B_2_3])
def test_B_2_invalid_feedback(browser,test_input, expected_output):
    # move the scroll bar to warranty area
    click_element(browser, test_element.do_you_have_question_field)
    type_in_element(browser,test_element.serial_number_column, test_input)
    click_element(browser, test_element.get_info_button)
    time.sleep(2)
    warnning_value = get_element_value(browser, test_element.invalid_feedback)

    assert warnning_value == expected_output, 'invalid feedback is incorrect'