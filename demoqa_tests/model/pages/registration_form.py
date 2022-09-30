from typing import Tuple
from selene import have, command
from selene.support.shared import browser
import demoqa_tests
from demoqa_tests import config
from demoqa_tests.model.controls import dropdown, radiobutton, datepicker, checkbox
from demoqa_tests.model.data import user
import datetime

state = browser.element('#state')
birthday = browser.element('#dateOfBirthInput')

def fill_firstname(firstname: str):
    browser.element('#firstName').send_keys(firstname)

def fill_lastname(lastname: str):
    browser.element('#lastName').send_keys(lastname)

def fill_email(email: str):
    browser.element('#userEmail').send_keys(email)

def fill_mobile(mobile: str):
    browser.element('#userNumber').send_keys(mobile)

def fill_subjects(subjects: Tuple):
    for i in subjects:
        browser.element('#subjectsInput').send_keys(i).press_enter()

def fill_address(address):
    browser.element('#currentAddress').send_keys(address)

def set_state(value: str):
    dropdown.select(state, value)

def set_city(value: str):
    city = browser.element('#city')
    dropdown.select(city, value)

def scroll_to_state():
    state.perform(command.js.scroll_into_view)

def scroll_to_submit():
    submit = browser.element('#submit')
    submit.perform(command.js.scroll_into_view)

def submit_form():
    browser.element('#submit').press_enter()

def should_have_submitted(data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))

def fill_gender(value: user.Gender):
    radiobutton.select_choice(value.value) #noqa

def fill_birthday(date: datetime.date):
    datepicker.select_date(birthday, date)

#def assert_filled_birthday(date: datetime.date):
    #birthday.should(datepicker.have_date(date))

def fill_hobbies(*options: user.Hobby):
    checkbox.select_checkbox(
        browser.all('[for^=hobbies-checkbox]'), *[option.value for option in options]
    )
