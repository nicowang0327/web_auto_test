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
    [(test_data.test_data_B_1[0], test_data.test_data_B_1[1][0])])
def test_B_3_invalid_feedback_and_valid_input(browser, test_input, expected_output):
    # move the scroll bar to warranty area
    click_element(browser, test_element.do_you_have_question_field)
    type_in_element(browser,test_element.serial_number_column, test_data.test_data_B_2_3[0])
    click_element(browser, test_element.get_info_button)
    time.sleep(2)
    # clear the invalid seriel number
    clear_input(browser, test_element.serial_number_column)
    # input the valid seriel number
    type_in_element(browser,test_element.serial_number_column, test_input)
    click_element(browser, test_element.get_info_button)
    result = get_element_value(browser, test_element.warranty_result)

    assert result == expected_output, 'result is not equal to warrenty'