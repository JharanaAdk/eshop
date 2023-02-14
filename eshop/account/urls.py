from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from products.controller import authview

urlpatterns = [
    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

