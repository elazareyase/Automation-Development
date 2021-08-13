from selenium.webdriver.common.keys import Keys


class HomePage:
    HOME_PAGE_URL = "https://skinnyties.com/"

    def __init__(self, driver):
        self.driver = driver

        self.search_link_linkText = "SEARCH"
        self.search_link_xpath = "//*[@id='section-header']/div/div[3]/nav/ul/li[1]/a"
        self.search_input_xpath = "//input[@class='Search__Input Heading'][@placeholder='Search...']"
        self.PRODUCT_NAME = "BLACK POPLIN SKINNY TIE"

    def enter_input_search(self, product_name):
        self.driver.find_element_by_xpath(self.search_input_xpath).clear()
        self.driver.find_element_by_xpath(self.search_input_xpath).send_keys(product_name)

    def click_find_product(self):
        self.driver.find_element_by_xpath(self.search_input_xpath).send_keys(Keys.ENTER)

    def click_search_link_text(self):
        self.driver.find_element_by_xpath(self.search_link_xpath).click()
