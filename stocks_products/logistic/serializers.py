from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id' , 'title', 'description']
        



class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе

    #product = ProductSerializer()  # Включаем информацию о продукте
    
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']

    def create(self, validated_data):
        title_data = validated_data.pop('tilte')
        product_data = validated_data.pop('product')
        product = Product.objects.get_or_create(title=title_data)
        validated_data['product'] = product
              
        return super().create(validated_data)


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    #address = serializers.CharField(required=False)  # Делаем поле необязательным

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        print(validated_data)
        positions_data = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position_data in positions_data:
            StockProduct.objects.get_or_create(stock=stock, **position_data)
        return stock



   
    def update(self, instance, validated_data):
        # print(validated_data)
        # print(instance)
        positions_data = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        # print(stock)
        
        for position_data in positions_data:
            print(position_data)                   
            defaults=dict(quantity=position_data["quantity"], price=position_data['price'])

            StockProduct.objects.update_or_create(
                stock=stock,
                product=position_data["product"],
                defaults=defaults
            )

        return stock 