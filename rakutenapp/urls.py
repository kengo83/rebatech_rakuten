from django.urls import path, include
from .views import Create,resultfunc

urlpatterns = [
    path('', Create.as_view(),name='home'),
    path('result/',resultfunc,name='result'),
]
