from rest_framework import serializers
from .models import Photo, Certificate, Logo, Video


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "image", "caption"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            "id",
            "title",
            "title_EN",
            "title_KY",
            "description",
            "description_EN",
            "description_KY",
            "image",
        ]


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ["id", "image", "uploaded_at"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["id", "video_code"]
