from browser import Browser


def before_all(self):
    self.browser = Browser()


def after_all(self):
    self.browser.driver.close()
