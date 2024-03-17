import json
import pytest
from selenium import webdriver


@pytest.fixture
def config(scope='session'):

    #Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    #Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


##Setup and Cleanup
@pytest.fixture
def browser(config):
    ##Arrange
    # Initialize Chromedriver object
    if config['browser'] == 'Firefox':
        driver = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        driver = webdriver.Chrome()
    elif config['browser']== 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'browser "{config["browser"]}" is not supported')
    
    # Add an implicite wait after every action on browser for element to appear
    driver.implicitly_wait(config['implicit_wait'])

    # Return driver object to test
    yield driver

    # Quit driver object after test is complete for cleanup
    driver.quit()
