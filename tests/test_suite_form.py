from appfunc.reg_page import RegistrationPage

reg_page = RegistrationPage()

def test_fill_form():
    """
    Заполнение формы PageObjects
    Успешно заполнено
    """
    reg_page.open_win()

    reg_page.fill_first_name('FirstNameInput')
    reg_page.fill_last_name('LastNameInput')
    reg_page.fill_email('emailName@contoso.com')
    reg_page.fill_gender('Female')
    reg_page.fill_user_number('0123456789')
    reg_page.fill_birthdate('1970', 'May', '29')
    reg_page.fill_subjects('Arts')
    reg_page.fill_hobbies('Reading')
    reg_page.fill_img('img1.jpg')
    reg_page.fill_current_address('City Msc Random street')
    reg_page.fill_state('NCR')
    reg_page.fill_city('Delhi')
    reg_page.submit_reg()

    reg_page.should_reg_user(
        'FirstNameInput',
        'LastNameInput',
        'emailName@contoso.com',
        'Female',
        '0123456789',
        '29 May,1970',
        'Arts',
        'Reading',
        'img1.jpg',
        'City Msc Random street',
        'NCR',
        'Delhi'
    )


