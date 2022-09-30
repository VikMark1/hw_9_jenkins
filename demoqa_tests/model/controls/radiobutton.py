from selene.support.shared import browser


def select_choice(number: int):
    browser.element(f'[for=gender-radio-{number}]').double_click()