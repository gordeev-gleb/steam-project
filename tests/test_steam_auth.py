def test_google_search(browser):
    browser.get("https://store.steampowered.com/")

    search_box = browser.find_element_by_name("q")
    search_box.send_keys("Selenium")
    search_box.submit()

    assert "Selenium" in browser.page_source
