from rest_framework import serializers
from .models import Product, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['title', 'description'] 


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    pass
    class Meta:
        model = StockProduct
        fields = ['positions', 'quantity', 'price'] 


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for item in positions:
            StockProduct.objects.create(
                stock=stock,
                product=item.get('product'),
                quantity=item.get('quantity'),
                price=item.get('price'),
            )
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for item in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=item.get('product'),
                defaults={
                    'quantity': item.get('quantity'),
                    'price': item.get('price')
                }
            )
        return stock
