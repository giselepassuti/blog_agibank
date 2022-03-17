from browser import Browser


class HomePageElements(object):
    CLICK_SEARCH = 'search-open'
    INPUT_BUSCA = '//*[@id="masthead"]/div[1]/div[2]/form/label/input'
    ClICK_PESQUISAR = 'search-submit'


class HomePage(Browser):
    def click_btn_search(self):
        self.driver.find_element_by_id(HomePageElements.CLICK_SEARCH).click()

    def preenche_input_busca(self, texto):
        self.driver.find_element_by_xpath(HomePageElements.INPUT_BUSCA).send_keys(texto)

    def click_btn_pesquisar(self):
        self.driver.find_element_by_class_name(HomePageElements.ClICK_PESQUISAR).click()
