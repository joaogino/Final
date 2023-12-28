from django.shortcuts import render
from rest_framework import viewsets
from .models import users, todos, comments, posts
from .serializers import usersSerializer, todosSerializer, commentsSerializer, postsSerializer

class usersViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de userss
    """
    queryset = users.objects.all()
    serializer_class = usersSerializer

class todosViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Albuns
    """
    queryset = todos.objects.all()
    serializer_class = todosSerializer

class commentsViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de Músicas
    """
    queryset = comments.objects.all()
    serializer_class = commentsSerializer
class postsViewset(viewsets.ModelViewSet):
    queryset = posts.objects.all()
    serializer_class = postsSerializer
