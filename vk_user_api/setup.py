from decouple import config


TOKEN = config("VK_API_TOKEN", default="VK_API_TOKEN")
LOGIN = config("LOGIN", default="LOGIN")
PASSWORD = config("PASSWORD", default = "PASSWORD")
