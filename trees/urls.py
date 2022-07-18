from django.urls import path, include
from trees import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_trees),
    path('all/', views.get_all_trees),
]
