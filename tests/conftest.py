import pytest
from selenium import webdriver

##Setup and Cleanup
@pytest.fixture
def browser():
    ##Arrange
    # Initialize Chromedriver object
    driver = webdriver.Chrome()

    # Add an implicite wait after every action on browser for element to appear
    driver.implicitly_wait(10)

    # Return driver object to test
    yield driver

    # Quit driver object after test is complete for cleanup
    driver.quit()
