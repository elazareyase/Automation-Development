import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.homePage import HomePage
from Pages.searchResults import ResultPage
from Pages.tieBars import TieBars
from Pages.retro import Retro


class ProductTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test_product_price(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(HomePage.HOME_PAGE_URL)

        home_page = HomePage(driver)
        home_page.click_search_link_text()
        home_page.enter_input_search(home_page.PRODUCT_NAME)
        time.sleep(1)
        home_page.click_find_product()
        time.sleep(2)

        result_page = ResultPage(driver)
        product_price_str = result_page.get_elements_text(result_page.tie_price_span_text)[0].text
        product_description = result_page.get_elements_text(result_page.tie_description_linkText)[0].text

        print("Tie Description: {}, Tie Price: {}".format(product_description, product_price_str))
        product_price = float(product_price_str.lstrip("$"))

        assert product_price > 10

    def test_retro_products_size(self):
        driver = self.driver
        driver.get(Retro.RETRO_URL)
        time.sleep(1)

        retro = Retro(driver)

        h2_elements = retro.get_elements_text(retro.product_class, find_by="class_name")
        total_size_sum = retro.sum_data(h2_elements, data_type="size")
        print(total_size_sum)

        assert total_size_sum > 4

    def test_tie_bars_products_sum(self):
        driver = self.driver
        time.sleep(2)

        tie_bars = TieBars(driver)

        self.driver.find_element_by_xpath("//*[@id='section-header']/div/div[1]/nav/ul/li[6]").click()
        time.sleep(4)

        elements_text = tie_bars.get_elements_text(tie_bars.product_class, find_by="span")
        total_price = tie_bars.sum_data(elements_text)
        print(total_price)

        assert total_price > 20

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
