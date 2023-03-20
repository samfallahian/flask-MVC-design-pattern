import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "mysecret"
    DB_HOST = "localhost"
    DB_NAME = "sandwich_maker"
    DB_USERNAME = "root"
    DB_Password = "rootroot"
    TEMPLATE_PATH = f"{basedir}\\app\\views"
