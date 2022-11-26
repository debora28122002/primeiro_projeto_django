from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/', views.hello),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/'))
]