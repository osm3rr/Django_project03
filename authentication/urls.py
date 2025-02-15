from django.urls import path,include
from authentication.views import *

urlpatterns=[

    path("",SignUpView.as_view(),name="signup"),
    path("accounts/",include("django.contrib.auth.urls")),
]