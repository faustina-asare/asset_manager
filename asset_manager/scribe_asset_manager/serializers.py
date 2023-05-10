from rest_framework import serializers
from scribe_asset_manager.models import ScribeAssetManager


class ScribeAssetManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScribeAssetManager
        fields = ['id', 'title', 'description', 'image']