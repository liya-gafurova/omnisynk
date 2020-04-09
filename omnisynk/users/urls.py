from django.urls import path
from .views import authinticate, SignInUser

urlpatterns = [
    path('signup/', authinticate),
    path('signin/', SignInUser.as_view(actions={'post': 'create'}))
]