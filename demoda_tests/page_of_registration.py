from selene import browser, be, have, command
import os


class RegistrationPage:

    def type_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def type_second_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def type_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def choose_gender(self, value):
        browser.element('[for=gender-radio-1]').should(have.text(value)).click()

    def type_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def choose_BD_date(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select [value="5"]').should(have.text(month)).click()
        browser.element('.react-datepicker__year-select [value="2000"]').should(have.text(year)).click()
        browser.element('.react-datepicker__day--021').should(have.text(day)).click()

    def type_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def choose_hobbie(self, value):
        browser.element('[for=hobbies-checkbox-3]').should(have.text(value)).click()

    def upload_pic(self, value):
        browser.element('#uploadPicture').send_keys((os.getcwd() + value))

    def type_street(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)


    def type_state(self, value):
        browser.element('#react-select-3-input').should(be.blank).type(value).press_enter()


    def type_city(self, value):
        browser.element('#react-select-4-input').should(be.blank).type(value).press_enter()

    def press_sybmit(self):
        browser.element('#submit').perform(command.js.click)

    def title_text(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.text(value))

    def should_have_text(self, first_second_name, email, gender, phone_number, BD_date, subject, hobbie, file, street,
                         state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                'Dima Nasedkin',
                'test@mail.com',
                'Male',
                '8926001010',
                '21 June,2000',
                'Accounting',
                'Music',
                'pic.png',
                'Pushkina str',
                'Haryana Karnal'))

    def press_close(self):
        browser.element('#closeLargeModal').click()


