import datetime as dt

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Genre


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=False)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category',
                  'rating')
        model = Title


class TitlePostSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )
    rating = serializers.IntegerField(read_only=True)

    def validate_year(self, value):
        year_now = dt.date.today().year
        if ((value < 0) or value > year_now):
            raise serializers.ValidationError(
                'Год не может быть в будущем или до нашей эры!'
            )
        return value

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category',
                  'rating')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериалайзер вьюсета Review."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    def validate(self, data):
        author = self.context['request'].user
        title_id = self.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        if self.context['request'].method == 'POST':
            if Review.objects.filter(title=title, author=author).exists():
                raise serializers.ValidationError(
                    'Вы не можете оставить второй отзыв на это же произведение'
                )
        return data

    class Meta:
        model = Review
        fields = ('id', 'author', 'title', 'text', 'score', 'pub_date')
        read_only_fields = ('title', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class UserSerializerOrReadOnly(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        fields = '__all__'
        model = User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        model = User
        lookup_field = 'username'

    def validate(self, data):
        if data.get('username') == 'me':
            raise serializers.ValidationError(
                'Использовать имя me в качестве username запрещено'
            )
        return data


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.RegexField(
        max_length=150,
        required=True,
        regex=r'^[\w.@+-]+$',
    )
    email = serializers.EmailField(
        max_length=254,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate(self, data):
        if data.get('username') == 'me':
            raise serializers.ValidationError(
                'Использовать имя me в качестве username запрещено'
            )
        return data


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
