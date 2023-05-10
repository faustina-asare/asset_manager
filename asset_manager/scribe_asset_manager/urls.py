from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ScribeAssetMangerView

urlpatterns = [
    path('scribe_asset_manager/<int:pk>', ScribeAssetMangerView.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'update'}), name="asset-product-pk"),
    path('scribe_asset_manager/', ScribeAssetMangerView.as_view({'get': 'list', 'post': 'create'}), name="asset-product"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
