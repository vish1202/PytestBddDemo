"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.
"""

import pytest

from pytest_bdd import given, when, then, parsers, scenario
from selenium import webdriver

# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Scenarios

# scenarios('C:/Users/vishal_dewani/PycharmProjects/PytestBddDemo/pytest-bdd/tests/features/web.feature')
@scenario(r'C:/Users/vishal_dewani/PycharmProjects/PytestBddDemo/pytest-bdd/tests/features/web1.feature', 'Basic DuckDuckGo Search')
def test_basic_duckduckgo_search():
    print("Alerts Roll-out steps definition file")


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


# When Steps

@when(parsers.cfparse('the user searches for "{phrase}"'))
def search_phrase(phrase):
    # search_input = browser.find_element_by_name('q')
    # search_input.send_keys(phrase + Keys.RETURN)
    print("When Statement executed" + phrase)


# Then Steps
@then(parsers.cfparse('results are shown for "{phrase}"'))
def search_results(phrase):
    print("Then Statement executed" + phrase)
