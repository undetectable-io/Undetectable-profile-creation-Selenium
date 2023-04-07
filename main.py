from selenium.webdriver.support.ui import WebDriverWait
from arg_parser import InputArgParser
from driver_context import DriverContext



def execute():
    timeout = 10
    with DriverContext() as driver:
        WebDriverWait(driver, timeout)
        driver.get("https://undetectable.io")

arg_parser = InputArgParser()
for i in range(arg_parser.get_instance()):
    execute()
