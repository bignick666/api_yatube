from rest_framework import serializers
from posts.models import Post, Group



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image',
                  'pub_date', 'image')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
