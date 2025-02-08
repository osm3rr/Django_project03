from django.urls import path
from authentication.views import *

urlpatterns=[

    path("",SignUpView.as_view(),name="signup"),
]