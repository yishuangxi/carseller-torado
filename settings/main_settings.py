#coding=utf8
import os.path
settings = {
    'static_path': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'),
    'template_path': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template'),
    'cookie_secret': '__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__',
    'login_url': '/login',
    # 'xsrf_cookies': True,
    'debug': True,
    'autoreload': True
}