<<<<<<< HEAD
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    
=======
from django.conf.urls import url, patterns, include
from django.contrib import admin
import django_twilio

from recipes import views

admin.autodiscover()

urlpatterns = [
    url(r'^list/(?P<ingredients>.+?)/$', views.recipe_list, name='recipe_list'),
    url(r'^(?P<recipe_id>[0-9]+)/(?P<ingredients>.+?)/$', views.detail_view, name='detail'),
    url(r'^ingredients/', views.choose_ingredients, name='choose_ingredients'),
    url(r'^message/$', 'django_twilio.views.message', {
        'message': 'Thanks for da SMS',
    }),
>>>>>>> be8d88bdb6587541493f2c93f91ebdbc8d0618eb
]
