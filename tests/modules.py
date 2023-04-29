from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import test_element
import time


# wait for element for 10 sec to be clicable 
def wait_for_element(driver, element):
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, element))
    )

# click the specified element
def click_element(driver, element):
    wait_for_element(driver, element)
    button = driver.find_element(By.CSS_SELECTOR, element)
    button.click()   

# type input_data in the specified element
def type_in_element(driver, element, input_data):
    wait_for_element(driver, element)   
    input_field = driver.find_element(By.CSS_SELECTOR, element)
    input_field.click()
    input_field.send_keys(input_data)    

# get the value of the specified element
def get_element_value(driver, element):
    wait_for_element(driver, element)
    element_item = driver.find_element(By.CSS_SELECTOR, element)
    value = element_item.get_attribute('innerText')
    return value

# change the languae of the web 
def change_language(driver, language):
    click_element(driver, test_element.language_switch_button)
    click_element(driver, test_element.language_drop_down_button)
    if language == 'EN':
        click_element(driver, test_element.language_EN)
    elif language == 'JA':
        click_element(driver, test_element.language_JA)
    elif language == 'KO':
        click_element(driver, test_element.language_KO)
    elif language == 'RU':
        click_element(driver, test_element.language_RU)
    elif language == 'ZH':
        click_element(driver, test_element.language_ZH)
    click_element(driver, test_element.update_language_button)
    time.sleep(2)

# clear the input of the specified element
def clear_input(driver, element):
    click_element(driver, element)
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.send_keys('a')
    actions.key_up(Keys.CONTROL)
    actions.key_down(Keys.BACK_SPACE)
    actions.perform()
