from selenium.webdriver.common.by import By


class ElementLocators:
    el_menu = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]")


class HeaderLocators:
    header = (By.CLASS_NAME, "main-header")


class CheckBoxLocators:
    check_box = (By.ID, "item-1")
    home_el = (By.CLASS_NAME, "rct-icon-expand-close")
    download_el = (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[3]/span/button")
    file_el = (By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[1]/span/label/span[3]")
    selected_text = (By.ID, "result")

