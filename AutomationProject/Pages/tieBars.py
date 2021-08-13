from Pages.action import Action


class TieBars(Action):
    TIE_BARS_URL = "https://skinnyties.com/collections/tie-bars"

    def __init__(self, driver):
        super().__init__(driver)

        self.product_class = "ProductItem__Price Price Text--subdued"

