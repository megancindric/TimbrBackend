from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, RegistrationSerializer, UserSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from trees.models import Tree
User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class FavoritesView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, tree_id):
        print(
            'User ', f"{request.user.id} {request.user.email} {request.user.username}")
        user = get_object_or_404(User, pk=request.user.id)
        favorite = get_object_or_404(Tree,pk=tree_id)
        if favorite not in user.favorites.all():        
            user.favorites.add(favorite)
        else:
            user.favorites.remove(favorite)
        serializer = UserSerializer(user)
        return Response(serializer.data)
 
class GetUserInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = get_object_or_404(User, pk=request.user.id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            pass

class RemoveFavorite(APIView):
    def patch(self, request, tree_id):
        try:
            print(
                'User ', f"{request.user.id} {request.user.email} {request.user.username}")
        except:
            pass
