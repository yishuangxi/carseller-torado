from handler.user import UserPageHandler, UserInfoHandler, ResetPasswordHandler

Router = [
    (r'/user', UserPageHandler),
    (r'/api/user', UserInfoHandler),
    (r'/api/user/(\d+)', UserInfoHandler),
    (r'/api/password/reset', ResetPasswordHandler)
]