from selene.support.conditions import have
from selene.support.shared import browser


def select_checkbox(elements, *options: str):
    for option in options:
        elements.by(have.exact_text(option)).first.element('..').click()