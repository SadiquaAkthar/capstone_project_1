# locators.py
# keep all my locators data
class WebApp_Locators:
    username_input_box      = "username"
    password_input_box      = "password"
    submit_button           = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    logout_button           = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
    forgot_pass             = '//p[text()="Forgot your password? "]'
    reset_pass_btn          = '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]'
    reset_succ_msg          = 'h6.oxd-text.oxd-text--h6.orangehrm-forgot-password-title'
    page_head_Admin         = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul'
    menu_items_header       = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul'
    add_emp_save_btn        = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'