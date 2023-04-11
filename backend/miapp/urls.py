from django.urls import path
from .views import HomeView, TestUserView, TestUserPdfView, TestUserList, TestUserSavePdfView


urlpatterns= [
    # path("", HomeView.as_view()),
    path("<int:id>", TestUserView.as_view()),
    path("pdf/<int:id>", TestUserPdfView.as_view()),
    path("list", TestUserList.as_view()),
    path("savepdf/<int:id>", TestUserSavePdfView.as_view()),

]
