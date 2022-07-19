from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AddFavorite, GetUserInfo, RegisterView, MyTokenObtainPairView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('addtree/<int:tree_id>/', AddFavorite.as_view(), name='add_favorite'),
    path('userinfo/', GetUserInfo.as_view(), name='get_user_info'),
]
