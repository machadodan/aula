from decimal import Decimal

import pytest

from ..models import Item, Order

pytestmark = pytest.mark.django_db

def test__str__(product):
    order = order.objects.create(
     cpf="401.142.450-10",
     nome="Fulano",
     email="test@fulano.com",
     postal_code="76900-649",
     address="Rua Castro Alves",
     number="123",
     district="Jardim dos Migrantes",
     status="RO",
     city="Ji Paraná",	
)

assert order.__str__() == f"Pedido {order.id}"
assert str(order) == f"Pedido {order.id}"

item = Item.objects.create(
    order=Order,
    product=product,
    price=Decimal(10),
    quantity=1,	
) 

assert item.__str__() == str(item.id)
assert str(item) == str(item.id)