from handler.user import UserPageHandler, LoginPageHandler, RegisterPageHandler, \
    LoginApiHandler, RegisterApiHandler, PasswordApiHandler, UserApiHandler


Router = [

    #handler: user
    (r'/login', LoginPageHandler),
    (r'/register', RegisterPageHandler),
    (r'/user/(\d+)', UserPageHandler),

    (r'/api/login', LoginApiHandler),
    (r'/api/register', RegisterApiHandler),
    (r'/api/user/(\d+)', UserApiHandler),
    (r'/api/password/reset', PasswordApiHandler)
]