import datetime
import platform
import selene
from selene.support.conditions import have
from selenium.webdriver.common.keys import Keys
from selene.support.shared import browser
import demoqa_tests


def select_date(element: selene.Element, date: datetime.date):
    os_base = platform.system()
    if os_base == 'Darwin':
        element.send_keys(
            Keys.COMMAND + 'a' + Keys.NULL,
            date.strftime(demoqa_tests.config.datetime_format),
        ).press_enter()
    else:
        browser.element('#dateOfBirthInput').send_keys(
            Keys.CONTROL + 'a' + Keys.NULL,
            date.strftime(demoqa_tests.config.datetime_format),
        ).press_enter()


def select_date_2():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1991')
    browser.element('[aria-label="Choose Monday, October 7th, 1991"]').click()


#def assert_value(element: selene.Element, date: datetime.date):
    #element.should(
        #have.value(date.strftime(hw_5_demoqa_tests.config.datetime_format)))

def have_date(value: datetime.date):
    return have.value(value.strftime(demoqa_tests.config.datetime_format))