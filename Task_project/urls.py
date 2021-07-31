from django.contrib import admin
from django.urls import path
from auapp.views import ulogin, usignup, ulogout, uresetpassword
from taskapp.views import home,create,view,delete,feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usignup/', usignup, name="usignup"),
    path('ulogin/', ulogin, name="ulogin"),
    path('ulogout/', ulogout, name="ulogout"),
    path('uresetpassword/', uresetpassword, name="uresetpassword"),
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("view/", view, name="view"),
    path("delete/<int:id>", delete, name="delete"),
    path("feedback/", feedback, name="feedback")
]
