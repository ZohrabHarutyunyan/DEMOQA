import Utils.driver_factory as dr
from Utils.locators import \
    ElementLocators, HeaderLocators, CheckBoxLocators
import time


class HomePage:
    @staticmethod
    def open_base_page(config):
        base_page = dr.DriverFactory()
        driver = base_page.get_driver(config)
        assert driver.title == "DEMOQA", "FAIL"
        return driver

    @staticmethod
    def ClickOnElement(driver):
        driver.find_element(*ElementLocators.el_menu).click()
        header = driver.find_element(*HeaderLocators.header).text
        assert header == "Elements", "FAIL"

    @staticmethod
    def ClickOnCheckBox(driver):
        driver.find_element(*CheckBoxLocators.check_box).click()
        header = driver.find_element(*HeaderLocators.header).text
        assert header == "Check Box", "FAIL"

    @staticmethod
    def OpenHome(driver):
        driver.find_element(*CheckBoxLocators.home_el).click()

    @staticmethod
    def OpenDownload(driver):
        driver.find_element(*CheckBoxLocators.download_el).click()

    @staticmethod
    def SelectWordFile(driver):
        driver.find_element(*CheckBoxLocators.file_el).click()
        time.sleep(5)

    @staticmethod
    def GetMessageText(driver):
        el = driver.find_element(*CheckBoxLocators.selected_text)
        return el.text
