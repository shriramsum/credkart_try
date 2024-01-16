import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# from selenium.webdriver.chrome.options import Options


# In pytest, hook functions are functions that can be used to extend or
# modify the behavior of pytest. They are called automatically by pytest at
# specific times during the test run.

# The pytest_configure function is a hook function in pytest that is called once the
# configuration object has been created and all plugins and initial conftest files have been loaded.

# The pytest_addoption function is a hook function in pytest that is used to add custom command-line options to the
# pytest command. It takes a single argument, parser, which is an instance of the argparse.ArgumentParser class.


# add arg --broswer this for your command linner
def pytest_addoption(parser):
    parser.addoption("--browser")


# passing the value to --browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value
# of the --browser option passed to pytest on the command line.


# here we are passing actual value to --browser
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome Browser")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print("Launching Firefox Browser")
        driver = webdriver.Firefox()
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    # if browser == 'headless':
    else:
        print("Headless mode")
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options= chrome_options)
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  #
    driver.quit()


def pytest_metadata(metadata):
    metadata["Project Name"] = "CredKart"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User Profile"
    metadata["Tester"] = "Vishal"
    metadata.pop("Plugins", None)


@pytest.fixture(params=[

    ("TestUser101@credence.in", "Test123", "Pass"),
    ("TestUser101@credence.in1", "Test123", "Fail"),
    ("TestUser101@credence.in", "Test1231", "Fail"),
    ("TestUser101@credence.in1", "Test1231", "Fail")

])
def getDataForLogin(request):
    return request.param
