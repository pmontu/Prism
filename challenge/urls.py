from django.conf.urls import url
from challenge.views import *

urlpatterns = [
    url(r'^add/',add),
    url(r'^list/',list),
    url(r'^user/list/',user_list),
]
