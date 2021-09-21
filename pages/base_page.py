class BasePage():
    # Constructor of base class
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # Open page by objects url
    def open(self):
        self.browser.get(self.url)
