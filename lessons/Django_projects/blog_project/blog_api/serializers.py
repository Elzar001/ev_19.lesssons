from django.contrib.auth.models import User
from rest_framework import serializers

from blog_api.models import Category, Post, PostImages, Comment


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, write_only=True, required=True)
    password2 = serializers.CharField(min_length=4, write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if password2 != attrs['password']:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    @staticmethod
    def validate_first_name(value):
        if not value.istitle():
            raise serializers.ValidationError('Имя должно начинаться с заглавной буквы!')
        return value

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'],
                                   first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        exclude = ('id',)


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = PostImageSerializer(many=True, read_only=False, required=False)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'comments', 'preview', 'category', 'images')

    def create(self, validated_data):
        print('validated_data: ', validated_data)
        request = self.context.get('request')
        print('FILES', request.FILES)
        images_data = request.FILES
        created_post = Post.objects.create(**validated_data)
        print(created_post)
        print('work', images_data.getlist('images'))
        images_objects = [PostImages(post=created_post, image=image) for image in images_data.getlist('images')]
        PostImages.objects.bulk_create(images_objects)
        return created_post

    def is_liked(self, post):
        user = self.context.get('request').user
        return user.liked.filter(post=post).exists()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments_detail'] = CommentSerializer(instance.comments.all(), many=True).data
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance)
        representation['likes_count'] = instance.likes.count()
        return representation


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'post')
