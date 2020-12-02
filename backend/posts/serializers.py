from .models import Posts,Comments
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    # user_name = serializers.ReadOnlyField(source='user_id.username')
    comments = CommentSerializer(read_only=True,many=True)
    class Meta:
        model = Posts
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     #posts = PostsSerializer(read_only=True,many=True)
#     class Meta:
#         model = User
#         fields = '__all__'

