from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework import viewsets
from .models import Photo, Certificate, Logo, Video
from .serializers import (
    PhotoSerializer,
    CertificateSerializer,
    LogoSerializer,
    VideoSerializer,
)
from .service import translate_instance_service


class LanguageParamMixin:
    def get_language(self):
        return self.request.query_params.get("lang", "ru")


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAdminUser]

class CertificateViewSet(viewsets.ModelViewSet, LanguageParamMixin):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        lang = self.get_language()
        instance = translate_instance_service(instance, lang)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LogoCreateView(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAdminUser]

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUser]
