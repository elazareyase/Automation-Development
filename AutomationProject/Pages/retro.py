from Pages.action import Action


class Retro(Action):
    RETRO_URL = "https://skinnyties.com/collections/retro"

    def __init__(self, driver):
        super().__init__(driver)

        self.product_class = "ProductItem__Title Heading"
