class Action:

    def __init__(self, driver):
        self.driver = driver

    def get_elements_text(self, xpath,  find_by="xpath"):

        if find_by is "class_name":
            xpath = "//h2[@class='{}']".format(xpath)
        elif find_by is "span":
            xpath = "//span[@class='{}']".format(xpath)
        return self.driver.find_elements_by_xpath(xpath)

    def sum_data(self, elements_text, data_type="price"):
        total, char, index = 0, "$", 1
        elements_len = -2

        if data_type is "size":
            char, index, elements_len = '"', 0, len(elements_text)

        for num_str in elements_text[:elements_len]:
            print(num_str.text)
            num = float(num_str.text.split(char)[index])
            total += num

        return total
