from selene import browser, be, have, by, command
import os.path


def test_fill_form():
    """
    Заполнение формы
    Успешно заполнено
    """
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('FirstNameInput')
    browser.element('#lastName').type('LastNameInput')
    browser.element('#userEmail').type('emailName@contoso.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('May')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1970')).click()
    browser.element('.react-datepicker__day--029').click()
    browser.element('#subjectsInput').should(be.blank).type('Arts').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img1.jpg'))
    browser.element('#currentAddress').should(be.blank).type("City Msc Random street")
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    browser.element('.modal-content').element('table').browser.all('tr').all('td').even.should(
        have.exact_texts(
            'FirstNameInput LastNameInput',
            'emailName@contoso.com',
            'Female',
            '0123456789',
            '29 April,1970',
            'Arts',
            'Reading',
            'img1.jpg',
            'City Msc Random street',
            'NCR Delhi'
        ))
