from model.reg_page import RegistrationPage
from data.users import User


test_user1 = User(first_name='FirstNameInput', last_name='LastNameInput', email='emailName@contoso.com',
                  gender='Female',
                  phone_number='0123456789', year='1970', month='May', day='29', subjects='Arts',
                  hobbies='Reading', img='img1.jpg', address='City Msc Random street', state='NCR',
                  city='Delhi')
test_user2 = User(first_name='Aaaaaaaa', last_name='Bbbbbbb', email='asdasd@adasdasd.com', gender='Male',
                  phone_number='0123456789', year='1970', month='September', day='01', subjects='Physics',
                  hobbies='Sports', img='img2.jpg',
                  address='City Msc Random street,City Msc Random street,City Msc Random street', state='Haryana',
                  city='Panipat')


reg_page = RegistrationPage()


def test_fill_form_01():
    """
    Заполнение формы PageObjects test_user1
    Успешно заполнено
    """
    reg_page.open_win()
    reg_page.reg_user(test_user1)
    reg_page.should_users_reg(test_user1)


def test_fill_form_02():
    """
    Заполнение формы PageObjects test_user2
    Успешно заполнено
    """
    reg_page.open_win()
    reg_page.reg_user(test_user2)
    reg_page.should_users_reg(test_user2)
