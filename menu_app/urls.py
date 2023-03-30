from django.urls import path

from menu_app.views import menu

urlpatterns = [
    path('<slug:slug>/', menu, name='menu')
]
