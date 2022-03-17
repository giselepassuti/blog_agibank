
from browser import Browser


class ResultsPages(Browser):
    def get_text_title(self):
        return self.driver.find_element_by_css_selector('.archive-header h1').text

    def get_text_title_fail(self):
        return self.driver.find_element_by_css_selector('.entry-header h1').text

