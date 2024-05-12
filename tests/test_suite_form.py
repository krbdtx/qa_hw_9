from appfunc.reg_page import RegistrationPage

reg_page = RegistrationPage()

def test_fill_form():
    """
    Заполнение формы PageObjects
    Успешно заполнено
    """
    reg_page.open_win()
    (
        reg_page
        .fill_first_name('FirstNameInput')
        .fill_last_name('LastNameInput')
        .fill_email('emailName@contoso.com')
        .fill_gender('Female')
        .fill_user_number('0123456789')
        .fill_birthdate('1970', 'May', '29')
        .fill_subjects('Arts')
        .fill_hobbies('Reading')
        .fill_img('img1.jpg')
        .fill_current_address('City Msc Random street')
        .fill_state('NCR')
        .fill_city('Delhi')
        .submit_reg()
    )
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


