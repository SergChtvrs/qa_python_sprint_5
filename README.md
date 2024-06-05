# qa_python_sprint_5
___
### Stellar Burgers autotests:
```test_account_button.py```
+ **test_unauthorized_user_move_to_login_page_by_click_on_account_button** - при клике по кнопке "Личный кабинет" неавторизованный пользователь переходит на страницу авторизации  
+ **test_authorized_user_move_to_account_page_by_click_on_account_button** - при клике по кнопке "Личный кабинет" авторизованный пользователь переходит на страницу аккаунта  

```test_constructor.py```
+ **test_move_to_sauce** - при клике по табу "Соусы" происходит переходит к разделу "Соусы"
+ **test_move_to_filling** - при клике по табу "Начинки" происходит переходит к разделу "Начинки"
+ **test_move_to_bun** - при клике по табу "Булки" происходит переходит к разделу "Булки"

```test_constructor_button.py```
+ **test_authorized_user_move_to_main_page_by_click_on_constructor_button** - при клике по кнопке "Конструктор" из "Личного кабинета", пользователь переходит на главную страницу
+ **test_authorized_user_move_to_main_page_by_click_on_header_logo** - при клике по логотипу в шапке из "Личного кабинета", пользователь переходит на главную страницу

```test_exit_button.py```

+ **test_authorized_user_move_to_login_page_by_click_on_exit_button** - пользователь переходит на страницу авторизации при клике по кнопке "Выход" в "Личном кабинете"

```test_login.py```

+ **test_user_should_login_successfully_by_button_on_main_page** - пользователь успешно авторизован по кнопке "Войти в аккаунт" на главной странице
+ **test_user_should_login_successfully_by_account_button_in_header** - пользователь успешно авторизован по кнопке "Личный кабинет" в шапке
+ **test_user_should_login_successfully_by_button_on_register_page** - пользователь успешно авторизован по кнопке "Войти" на странице регистрации
+ **test_user_should_login_successfully_by_button_on_forgot_password_page** - пользователь успешно авторизован по кнопке "Войти" на странице восстановления пароля

```test_register.py```
+ **test_user_register_successfully_with_correct_password_length** - пользователь успешно зарегистрирован, если указал пароль длинной 6 символов
+ **test_user_register_failed_with_incorrect_password_length** - пользователь не зарегистрирован, если указал пароль длинной 3, 5 символов