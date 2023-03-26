from selene import browser, be, have, command
import os

from demoda_tests.page_of_registration import RegistrationPage


def test_practice_form(browser_settings):
    registration_page = RegistrationPage()

    registration_page.type_first_name('Dima')
    registration_page.type_second_name('Nasedkin')
    registration_page.type_email('test@mail.com')
    registration_page.choose_gender('Male')
    registration_page.type_phone_number('89260010101')
    registration_page.choose_BD_date('June', '2000', '21')
    registration_page.type_subject('Accounting')
    registration_page.choose_hobbie('Music')
    registration_page.upload_pic('/resources/pic.png')
    registration_page.type_street('Pushkina str')
    registration_page.type_state('Haryana')
    registration_page.type_city('Karnal')
    registration_page.press_sybmit()


    #проверка данных
    registration_page.title_text('Thanks for submitting the form')
    registration_page.should_have_text('Dima Nasedkin',
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








