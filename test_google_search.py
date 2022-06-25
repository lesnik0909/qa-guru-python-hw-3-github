from selene import be, have
from selene.support.shared import browser

search_selector = '[name="q"]'
result_text_selector = '[id="search"]'

selene_search_query = 'selene'
selenide_search_query = 'selenide'
selene_search_result = 'User-oriented Web UI browser tests in Python'


def test_able_find_selene_in_google(open_google):
    browser.element(search_selector).should(be.blank).type(selene_search_query).press_enter()
    browser.element(result_text_selector).should(have.text(selene_search_result))


def test_unable_find_selene_in_google(open_google):
    browser.element(search_selector).should(be.blank).type(selenide_search_query).press_enter()
    browser.element(result_text_selector).should(have.text(selene_search_result))
