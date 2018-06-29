from django.conf.urls import url
from api_request import views
urlpatterns=[
    url(r'^$',views.form_view),
    url(r'^after/',views.after,name='after'),
]
