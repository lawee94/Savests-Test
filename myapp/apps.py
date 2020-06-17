from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MyappConfig(AppConfig):
    name = 'myapp'

#Setting myapp admin as the default admin
class MyAdminConfig(AdminConfig):
    default_site = 'myproject.admin.MyModelAdmin'