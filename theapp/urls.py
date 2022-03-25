from django.urls import path
from .views import indexPageView, encouragementPageView, lowPageView, favoritesPageView
from .views import testimonyPageView, markPageView, unmarkPageView, loginPageView, loginUserPageView
from .views import logoutPageView, createUserPageView, createTheUserPageView, searchPageView

urlpatterns = [
    path("enc/", encouragementPageView, name="encouragement"),
    path("low/", lowPageView, name="low"),
    path("fav/", favoritesPageView, name="favorites"),
    path("test/", testimonyPageView, name="testimony"),
    path("mark/<id>/", markPageView, name="mark"),
    path("unmark/<id>/", unmarkPageView, name="unmark"),
    path("login/", loginPageView, name="loginpage"),
    path("loginuser/", loginUserPageView, name="login"),
    path("logout/", logoutPageView, name="logout"),
    path("create/", createUserPageView, name="create"),
    path("createuser/", createTheUserPageView, name="createuser"),
    path("search/", searchPageView, name="search"),
    path("", indexPageView, name="index")
]