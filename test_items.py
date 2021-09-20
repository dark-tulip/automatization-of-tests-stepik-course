import time


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_includes_add_to_busket_button(browser):
    browser.get(link)

    try:
        time.sleep(30)
        button = browser.find_element_by_css_selector(".btn-add-to-basket")
        if(button.text == "Ajouter au panier"):
            print("French language on button -> PASSED")
        print("Add to basket - PASSED")

    finally:
        browser.quit()


if __name__ == "__main__":
    test_page_includes_add_to_busket_button()
    print("Tests passed successful")
