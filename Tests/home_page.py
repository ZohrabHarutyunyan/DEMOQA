from Pages.HomePage import HomePage
import config as c


def home_page_test():
    home_page = HomePage()
    driver = home_page.open_base_page(c.config)
    home_page.ClickOnElement(driver)
    home_page.ClickOnCheckBox(driver)
    home_page.OpenHome(driver)
    home_page.OpenDownload(driver)
    home_page.SelectWordFile(driver)
    message = home_page.GetMessageText(driver)
    assert message == "You have selected :\nwordFile", "FAIL"
    print("PASS")


if __name__ == "__main__":
    home_page_test()




