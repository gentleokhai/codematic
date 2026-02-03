from rest_framework import serializers
from film.models import Film, Comment

class FilmSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Film
        fields = ["id", "title", "release_date", "comment_count"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "author_name",
            "text",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_text(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                "Comment must not exceed 500 characters."
            )
        return value
