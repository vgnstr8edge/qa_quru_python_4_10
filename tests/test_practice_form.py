from selene import browser, be, have, command

from demoda_tests.page_of_registration import RegistrationPage
from demoda_tests.users.user import User

user = User(first_name='Dima', second_name='Nasedkin', email='test@mail.com', gender='Male',
            phone_number='8926001010', date_of_bd='21', month_of_bd='June', year_of_bd='2000',
            subject='Accounting', hobbie='Music', photo='/resources/pic.png', street='Pushkina str',
            state='Haryana',
            city='Karnal')


def test_practice_form(browser_settings):
    registration_page = RegistrationPage()
    registration_page.user_info(user)

    # проверка данных
    registration_page.should_have_text(
            'Dima Nasedkin',
            'test@mail.com',
            'Male',
            '8926001010',
            '21 June,2000',
            'Accounting',
            'Music',
            'pic.png',
            'Pushkina str',
            'Haryana Karnal')

    registration_page.press_close()
