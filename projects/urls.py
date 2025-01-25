
from django.urls import path
from projects.views import ListProjects,DetailProjects,CreatePageView

urlpatterns=[
    
    path("",ListProjects.as_view(),name="home"),
    path("detail/<int:pk>",DetailProjects.as_view(),name="detail"),
    path("create",CreatePageView.as_view(),name="create"),

]