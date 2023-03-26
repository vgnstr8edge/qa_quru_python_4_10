from selene import have, command
from selene.support.shared import browser
import os
from demoda_tests.users.user import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.second_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone_number = browser.element('#userNumber')

        self.date_of_bd = browser.element('#dateOfBirthInput')
        self.month_of_bd = browser.element('.react-datepicker__month-select')
        self.year_of_bd = browser.element('.react-datepicker__year-select')

        self.subject = browser.element('#subjectsInput')
        self.hobbie = browser.all('[for=hobbies-checkbox-3]')
        self.picture = browser.element('#uploadPicture')

        self.street = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.list_state = browser.all('[id^=react-select][id*=option]')
        self.city = browser.element('#city')
        self.list_city = browser.all('[id^=react-select][id*=option]')
        self.submit = browser.element('#submit')

    def type_first_name(self, first_name):
        self.first_name.type(first_name)

    def type_second_name(self, second_name):
        self.second_name.type(second_name)

    def type_email(self, email):
        self.email.type(email)

    def choose_gender(self, gender):
        self.gender.element_by(have.value(gender)).element('..').click()

    def type_phone_number(self, number):
        self.phone_number.type(number)

    def choose_BD_date(self, month, year, day):
        self.month_of_bd.type(month)
        self.year_of_bd.type(year)
        self.date_of_bd.click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def type_subject(self, subject):
        self.subject.type(subject).press_enter()

    def choose_hobbie(self, hobbie):
        self.hobbie.element_by(have.exact_text(hobbie)).click()

    def upload_pic(self, picture):
        self.picture.send_keys((os.getcwd() + picture))

    def type_street(self, street):
        self.street.type(street)

    def type_state(self, state):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.list_state.element_by(have.exact_text(state)).click()

    def type_city(self, city):
        self.city.click()
        self.list_city.element_by(
            have.exact_text(city)
        ).click()

    def press_sybmit(self):
        self.submit.perform(command.js.click)


    def press_close(self):
        browser.element('#closeLargeModal').click()

    def user_info(self, user: User):
        self.first_name(user.first_name)
        self.second_name(user.second_name)
        self.email(user.email)
        self.gender(user.gender)
        self.phone_number(user.phone_number)
        self.choose_BD_date(user.month_of_bd, user.year_of_bd, user.date_of_bd)
        self.subject(user.subject)
        self.hobbie(user.hobbie)
        self.upload_pic(user.photo)
        self.type_street(user.street)
        self.type_state(user.state)
        self.type_city(user.city)

    def should_have_text(self, first_second_name, email, gender, phone_number, BD_date, subject, hobbie, file, street,
                         state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                first_second_name,
                email,
                gender,
                phone_number,
                BD_date,
                subject,
                hobbie,
                file,
                street,
                state_city))






