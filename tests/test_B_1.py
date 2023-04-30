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
    [test_data.test_data_B_1])
def test_B_1_input_valid_seriel_number(browser, test_input, expected_output):
    # move the scroll bar to warranty area
    click_element(browser, test_element.do_you_have_question_field)
    type_in_element(browser,test_element.serial_number_column, test_input)
    click_element(browser, test_element.get_info_button)
    time.sleep(2)
    result = []
    result.append(get_element_value(browser, test_element.warranty_result))
    result.append(get_element_value(browser, test_element.column_name_description))
    result.append(get_element_value(browser, test_element.description_info))
    result.append(get_element_value(browser, test_element.column_name_part_number))
    result.append(get_element_value(browser, test_element.part_number))
    result.append(get_element_value(browser, test_element.column_name_installation))
    result.append(get_element_value(browser, test_element.installation_date))
    result.append(get_element_value(browser, test_element.column_name_warranty_end))
    result.append(get_element_value(browser, test_element.warranty_end_date))
    
    status = 'passed'
    # set the status to passed as default. 
    # If AssertionError happens, changing the status to failed and raise excetpion after all the assertions are done.

    try:
        assert result[0] == expected_output[0], 'Warranty result is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    try:
        assert result[1] == expected_output[1], 'first column name is not expected.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    try:
        assert result[2] == expected_output[2], 'description result is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    try:
        assert result[3] == expected_output[3], 'second column name is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    try:
        assert result[4] == expected_output[4], 'part number result is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    try:
        assert result[5] == expected_output[5], 'third column name is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    try:
        assert result[6] == expected_output[6], 'installation data result is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'
    
    try:
        assert result[7] == expected_output[7], 'fourth column name is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    try:
        assert result[8] == expected_output[8], 'Warranty end date result is not expeced.' 
    except AssertionError as e:
        print('Error type is:', e)
        status = 'failed'

    if status == 'failed':
        raise(AssertionError)
