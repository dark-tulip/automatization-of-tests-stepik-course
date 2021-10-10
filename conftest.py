import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose laguage")


@pytest.fixture(scope="function")
def browser(request):
    page_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': page_language})

    browser = webdriver.Chrome(options=options)
    print(f"\nLanguage {page_language} selected for test..")

    yield browser

    print("\nquit browser..")
    browser.quit()
