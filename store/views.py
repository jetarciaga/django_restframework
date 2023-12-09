from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema

from store.models import Product
from store import serializers


@extend_schema_view(
    list=extend_schema(
        description="This returns all available products"
    ),
    create=extend_schema(
        description="This api expects the fields \
            'name' and 'price' creates a new oject and returns it"
    ),
    retrieve=extend_schema(
        description="This api returns a single product \
            object by providing the product 'id'. "
    ),
    update=extend_schema(
        description="This api updates a product object y providing its 'id'. \
            It needs the entire schema to update the object."
    ),
    partial_update=extend_schema(
        description="This api updates a product object by providing its 'id'. \
            It doesn't necessarily need the entire schema to update the object.\
                \ne.g. {'name': 'update_name'}",
    ),
    destroy=extend_schema(
        description="This api delete a product object by providing its 'id'."
    ),
)
class ProductViewSet(viewsets.ModelViewSet):
    """View for manage product APIs"""
    serializer_class = serializers.ProductSerializer
    queryset = Product.objects.all()