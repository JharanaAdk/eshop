from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from products.controller import authview
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name="password_reset_complete"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

