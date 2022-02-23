from django.urls import path
# from the same folder (.)
from . import views
# If the request reaches /january, execute the index function from views.
# <month> is a dynamic path segment
urlpatterns = [
    #path("january", views.january),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
    # path converter (int)
    path("<int:month>", views.monthly_challenge_by_number),
    path("", views.index, name="index")
]
