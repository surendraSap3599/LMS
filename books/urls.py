from django.urls import path
from . import views
urlpatterns = [
    path('',views.book_List, name='index'),
    path("<int:book_id>",views.book_details,name="details"),
]
