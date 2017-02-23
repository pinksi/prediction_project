"""minor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'stock.views.home', name='home1'),
    url(r'^analysis/', 'stock.views.analysis', name='khatra'),
    url(r'^prediction/(?P<company_id>[0-9]+)$', 'stock.views.sidebar', name ='prediction'),
    url(r'^previous_prediction/(?P<company_id>[0-9]+)$', 'stock.views.previous_prediction', name ='previous_prediction'),
    url(r'^previous_nepse_prediction/', 'stock.views.previous_nepse_prediction', name ='previous_nepse_prediction'),
    # url(r'^adb/', 'stock.views.details2', name='adblana'),
    # url(r'^plic/', 'stock.views.details3', name='plicanalysis'),
    # url(r'^nlic/', 'stock.views.details4', name='nlicanalysis'),
    url(r'^prediction/', 'stock.views.sidebar', name='prediction'),
    url(r'^about/', 'stock.views.about', name='about'),
]
