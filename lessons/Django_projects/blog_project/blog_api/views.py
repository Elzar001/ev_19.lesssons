from rest_auth.views import LogoutView
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from blog_api import serializers
from blog_api.models import Post, Comment, Likes
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from blog_api.models import Post, Category
from blog_api.permissions import IsAuthor
from blog_api.serializers import PostSerializer, CommentSerializer


# TODO Add likes

class StandartPaginationClass(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 1000


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.RegisterSerializer


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer

#
# class PostCreateView(generics.CreateAPIView):
#     serializer_class = serializers.PostSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class PostListView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#
# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#
# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#
# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer


class PostViewSet(ModelViewSet):
    class Meta:
        model = Post
        fields = '__all__'
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class = StandartPaginationClass
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'owner')
    search_fields = ('title', )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # api/v1/posts/<id>/comments
    @action(['GET'], detail=True)
    def comments(self, request, pk):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    # api/v1/posts/<id>/add_to_liked/
    @action(['POST'], detail=True)
    def add_to_liked(self, request, pk):
        post = self.get_object()
        if request.user.liked.filter(post=post).exists():
            # request.user.liked.filter(post=post).delete()
            return Response('Вы уже лайкали этот пост', status=status.HTTP_400_BAD_REQUEST)
        Likes.objects.create(post=post, user=request.user)
        return Response('Вы поставили лайк', status=status.HTTP_201_CREATED)

    @action(['POST'], detail=True)
    def remove_from_liked(self, request, pk):
        post = self.get_object()
        if not request.user.liked.filter(post=post).exists:
            return Response('Вы еще не лайкнули пост', status=status.HTTP_400_BAD_REQUEST)
        request.user.liked.filter(post=post).delete()
        return Response('Ваш лайк удален', status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        #Создавать посты может залогиненный пользователь
        if self.action in ('create', ):
            return [permissions.IsAuthenticated()]
        # Изменять и удалять может только автор
        elif self.action in ('update', 'partial_update', 'destroy',):
            return [IsAuthor()]
        # Просматривать могут все
        else:
            return [permissions.AllowAny()]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor)


# class PostView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#
# class PostDetailView(APIView):
#     @staticmethod
#     def get_object(pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Exception('not found')
#
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, many=True)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data,)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response('Deleted', status=204)
#
#
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

