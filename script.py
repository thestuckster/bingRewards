#!/usr/bin/env/python
import time
from selenium import webdriver


def main():
    terms = read_terms()

    print "Setting up selenium..."
    browser = setup_selenium()

    login(browser)

    print "Starting search terms..."
    for term in terms:
        print "searching: " + term
        enter_search_term(browser, term)
        clear_search_box(browser)

    print "Script finished. Closing window."
    browser.quit()


def read_terms():
    terms = []
    print "Reading in search terms.."
    file = open("searchTerms.txt", "r")

    for line in file:
        terms.append(line)

    return terms


def setup_selenium():
    browser = webdriver.Firefox()
    browser.get("https://www.bing.com/fd/auth/signin?action=interactive&provider=windows_live_id&return_url=http%3a%2f%2fwww.bing.com%2f%3fwlexpsignin%3d1&src=EXPLICIT&sig=12748851626769B425B980AC63C56846")

    return browser


def login(browser):
    time.sleep(2)

    print "Signing in..."
    email_box = browser.find_element_by_id("i0116")
    email_box.send_keys("sstucky3@gmail.com")

    next_btn = browser.find_element_by_id("idSIButton9")
    next_btn.click()
    time.sleep(1)

    password_box = browser.find_element_by_id("i0118")
    password_box.send_keys("nikond90")

    sign_in_btn = browser.find_element_by_id("idSIButton9")
    sign_in_btn.click()
    time.sleep(1)


def enter_search_term(browser, term):
    box = find_search_box(browser)

    box.send_keys(term)
    click_submit(browser)
    time.sleep(1)


def find_search_box(browser):
    search_box = browser.find_element_by_id("sb_form_q")

    return search_box


def click_submit(browser):
    submit_btn = browser.find_element_by_id("sb_form_go")
    submit_btn.click()


def clear_search_box(browser):
    box = find_search_box(browser)
    box.clear()


if __name__ == "__main__":
    main()
else:
    print "Error: This is not a library"
