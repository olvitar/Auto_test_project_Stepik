class BasePage(object):
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        # your code