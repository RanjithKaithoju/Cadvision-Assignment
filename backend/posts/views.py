from .models import Posts,User,Comments
from .serializers import PostsSerializer,CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404
from django.shortcuts import render

#index view
def index(request):
    return render(request,'index.html')



#API to get/post the posts    
class posts(ListCreateAPIView): 
    serializer_class = PostsSerializer
    
    def get_queryset(self):
       posts = Posts.objects.all().order_by('-post_date')
       return posts

    def get(self, request):
        '''Get all Posts'''
        posts = self.get_queryset()
        #paginate_queryset = self.paginate_queryset(posts)
        serializer = self.serializer_class(posts, many=True)
        if len(serializer.data) == 0:
            return Response([{"msg":"no data"}])
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        '''Creates new post'''
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API for Comments
class comments(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

#API for likes
class postlike(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


    def put(self, request, pk):
        '''Update like count by 1'''
        model = get_object_or_404(Posts, pk=pk)
        #serializer = PostsSerializer(model, data=request.data)
        data = {"likes" : model.likes+1}
        serializer = PostsSerializer(model,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API for Dislikes
class postdislike(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


    def put(self, request, pk):
        '''updates dislike count by 1'''
        model = get_object_or_404(Posts, pk=pk)
        serializer = PostsSerializer(model, data=request.data)
        data = {"dislikes" : model.dislikes+1}
        serializer = PostsSerializer(model,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




