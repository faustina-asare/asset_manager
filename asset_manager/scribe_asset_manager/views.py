from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from scribe_asset_manager.models import ScribeAssetManager
from scribe_asset_manager.serializers import ScribeAssetManagerSerializer


class ScribeAssetMangerView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ScribeAssetManagerSerializer
    queryset = ScribeAssetManager.objects.all()
    pagination_class = LimitOffsetPagination
    ordering_fields = ['created', 'id']
    search_fields = ['title', 'description']
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]