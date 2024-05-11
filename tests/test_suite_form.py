from selene import browser,  be, have, by
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
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img1.jpg'))
    browser.element('#currentAddress').should(be.blank).type("City Msc Random street")
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()
    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text("Thanks for submitting the form"))
    browser.element("tbody tr:nth-child(1) td:nth-child(2)").should(have.text('FirstNameInput LastNameInput'))
    browser.element("tbody tr:nth-child(2) td:nth-child(2)").should(have.text('emailName@contoso.com'))
    browser.element("tbody tr:nth-child(3) td:nth-child(2)").should(have.text('Female'))
    browser.element("tbody tr:nth-child(4) td:nth-child(2)").should(have.text('0123456789'))
    browser.element("tbody tr:nth-child(5) td:nth-child(2)").should(have.text('29 April,1970'))
    browser.element("tbody tr:nth-child(6) td:nth-child(2)").should(have.text('Arts'))
    browser.element("tbody tr:nth-child(7) td:nth-child(2)").should(have.text('Reading'))
    browser.element("tbody tr:nth-child(8) td:nth-child(2)").should(have.text('img1.jpg'))
    browser.element("tbody tr:nth-child(9) td:nth-child(2)").should(have.text('City Msc Random street'))
    browser.element("tbody tr:nth-child(10) td:nth-child(2)").should(have.text('NCR Delhi'))

