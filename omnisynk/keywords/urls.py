from django.contrib import admin
from django.urls import path
from omnisynk.keywords.views import *

urlpatterns = [
    path('examples/show-all/', AddExample.as_view()),
    path('examples/update/<int:pk>', UpdateExample.as_view()),

    # path('methods/show-all/', ShowMethods.as_view()),
    # path('methods/update/<int:pk>', UpdateMethods.as_view()),

    path('keywords/show-all/', ShowKeyWordsResults.as_view()),
    path('keywords/delete/<int:pk>', UpdateKeyWordsResults.as_view()),
    path('keywords/create/', CreateKeyWords.as_view()),

]
