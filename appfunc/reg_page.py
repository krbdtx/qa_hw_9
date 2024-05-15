from selene import browser, have, by, command
from appfunc import resource


class RegistrationPage:

    def open_win(self) -> object:
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender(self, value):
        browser.all('[name="gender"]').element_by(have.value(value)).element('..').click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_birthdate(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        browser.all('#hobbiesWrapper label').element_by(have.exact_text(value)).element('..').perform(
            command.js.scroll_into_view).click()
        return self

    def fill_img(self, file):
        browser.element('#uploadPicture').send_keys(resource.path(file))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit_reg(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()
        return self

    def should_reg_user(self, first_name, last_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture,
                        current_address, state, city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{first_name} {last_name}',
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            f'{state} {city}'
        ))
        return self
