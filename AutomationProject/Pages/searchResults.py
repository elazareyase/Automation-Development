from Pages.action import Action


class ResultPage(Action):
    PRODUCT_URL = "https://skinnyties.com/search?q=BLACK+POPLIN+SKINNY+TIE&type=product"

    def __init__(self, driver):
        super().__init__(driver)

        self.tie_price_span_text = "//*[@id='main']/section/div/div/div/div/div/div/span"
        self.tie_description_linkText = "//*[@id='main']/section/div/div/div/div/div/h2/a"
