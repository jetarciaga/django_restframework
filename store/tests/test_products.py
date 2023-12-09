from decimal import Decimal

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
import pytest

from store.models import Product
from store.serializers import ProductSerializer


PRODUCT_URL = reverse('store:product-list')
pytestmark = pytest.mark.django_db

def create_product(**params):
    """Create and return a simple product."""
    defaults = {
        'name': 'sample product',
        'price': Decimal('900.25')
    }

    defaults.update(**params)
    product = Product.objects.create(**defaults)
    return product

def detail_url(product_id):
    return reverse('store:product-detail', args=[product_id])


# ---------- Test Products API -------------

def test_create_product(client):
    payload = {'name': 'Kings\'s Herbal', 'price': Decimal('1200.50')}
    res = client.post(PRODUCT_URL, payload)

    assert res.status_code == status.HTTP_201_CREATED

    product = Product.objects.get(id=res.data['id'])
    for k, v in payload.items():
        assert getattr(product, k) == v
    assert product.name == payload['name']

def test_get_product_list(client):
    pass