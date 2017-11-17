from django.conf.urls import url
from Testline_Details import views

urlpatterns=[url(r'^$',views.home,name='home'),
             url(r'^about/',views.about,name="about"),
             url(r'^edit/(?P<sbtsid>[\w\-]+)/$',views.editdetails,name="editdetails"),
             url(r'^register/$',views.register,name="register"),
             url(r'^login/$',views.user_login,name="login"),
             url(r'^logout/$',views.user_logout,name="logout")
             ]
