from .models import Posts,User,Comments
from .serializers import PostsSerializer,UserSerializer,CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated


class users(ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)  
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class posts(ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)  
    serializer_class = PostsSerializer
    
    def get_queryset(self):
       posts = Posts.objects.all().order_by('-post_date')
       return posts

    # Get all posts
    def get(self, request):
        posts = self.get_queryset()
        #paginate_queryset = self.paginate_queryset(posts)
        serializer = self.serializer_class(posts, many=True)
        if len(serializer.data) == 0:
            return Response([{"msg":"no data"}])
        return Response(serializer.data,status=status.HTTP_200_OK)

    # Create a new post
    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class comments(ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)  
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class postlike(RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)  
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


    def put(self, request, pk):
        model = get_object_or_404(Posts, pk=pk)
        #serializer = PostsSerializer(model, data=request.data)
        data = {"likes" : model.likes+1}
        serializer = PostsSerializer(model,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class postdislike(RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)  
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


    def put(self, request, pk):
        model = get_object_or_404(Posts, pk=pk)
        serializer = PostsSerializer(model, data=request.data)
        data = {"dislikes" : model.dislikes+1}
        serializer = PostsSerializer(model,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




