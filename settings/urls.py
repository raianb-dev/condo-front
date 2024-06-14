

from django.urls import path
from login import views as views_login
from homework import views as views_homework
from registerorder import views as vies_registerorder

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views_login.redirect_login, name='login'),
    path('painel', views_homework.redirect_home, name='homework'),
    path('register-order', vies_registerorder.redirectorder, name='registerorder'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
