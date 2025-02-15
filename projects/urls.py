
from django.urls import path
from projects.views import *

urlpatterns=[
    
    path("",WelcomePage,name="welcome"),

    path("list",ListProjects.as_view(),name="home"),
    path("detail/<int:pk>",DetailProjects.as_view(),name="detail"),
    path("create",CreatePageView.as_view(),name="create"),
    path("detail/<int:pk>/update",UpdatePageView.as_view(),name="update"),
    path("detail/<int:pk>/delete",DeletePageView.as_view(),name="delete")

]