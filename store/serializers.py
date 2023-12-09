from rest_framework import serializers
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product Model"""

    class Meta:
        model = Product
        fields = ['id', 'name', 'price']
        read_only_fields = ['id']