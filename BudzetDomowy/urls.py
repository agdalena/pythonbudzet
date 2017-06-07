"""BudzetDomowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from polls import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^polls/', include('polls.urls')),
    url(r'^mail/$', views.mail, name='mail'),
    url(r'^account_detail/(?P<pk>\d+)$', views.account_detail, name='account_detail'),
    
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', views.all_accounts, name='all_accounts'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    

    url(r'^transactions/', views.all_transactions, name='all_transactions'),
    url(r'^add_transaction/$', views.add_transaction, name='add_transaction'),
    url(r'^edit_transaction/(?P<pk>\d+)$', views.edit_transaction, name='edit_transaction'),
    url(r'^delete_transaction/(?P<pk>\d+)$', views.delete_transaction, name='delete_transaction'),
    url(r'^filter_transactions/' , views.filter_transactions, name='filter_transactions'),

    url(r'^categories/', views.all_categories, name='all_categories'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^edit_category/(?P<pk>\d+)$', views.edit_category, name='edit_category'),
    url(r'^delete_category/(?P<pk>\d+)$', views.delete_category, name='delete_category')
]
