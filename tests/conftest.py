import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import test_element
from modules import click_element
from modules import wait_for_element
from modules import change_language
import time


@pytest.fixture()
def browser():
    # Create a new browser oject
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.barco.com/eu-en/support/clickshare-extended-warranty/warranty")

    # Close accept_all_cookie message dialogue
    try: 
        click_element(driver, test_element.accept_all_cookie_button)
        time.sleep(2)
    except:
        pass

    yield driver

    # Turn off browser after testing is done 
    driver.quit()

