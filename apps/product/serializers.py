from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from apps.product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'vendor_code', 'history',
            'characteristic', 'size', 'images', 'video_url', 'description'
        ]

    @swagger_serializer_method(serializers.ListField(child=serializers.URLField()))
    def get_images(self, obj):
        request = self.context['request']
        build_uri = request.build_absolute_uri
        images = obj.images.all().order_by('id')
        return [build_uri(image.image.url) for image in images]


class ProductListSerializer(ProductSerializer):
    catalog = serializers.SerializerMethodField()

    class Meta:
        model = ProductSerializer.Meta.model
        fields = ['id', 'name', 'catalog', 'price', 'images']

    def get_catalog(self, obj):
        category = obj.categories.filter(is_top=True).first()
        return category.name if category else None


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']

    @swagger_serializer_method(SubCategorySerializer(many=True))
    def get_subcategories(self, obj):
        category_id = self.context.get('category_id', None)
        sub_categories = obj.sub_categories.select_related('parent').all().order_by('id')
        if category_id:  # get the sidebar subcategories corresponding to the category
            sub_categories = sub_categories.filter(products__categories=category_id).distinct()
        return SubCategorySerializer(sub_categories, many=True).data


class SidebarSerializer(serializers.Serializer):
    data = serializers.SerializerMethodField()

    @swagger_serializer_method(CategorySerializer(many=True))
    def get_data(self, obj):
        category_id = obj.id
        querysat = Category.objects.filter(is_left=True, products__categories=category_id).distinct().order_by('id')
        return CategorySerializer(querysat, many=True, context={'category_id': category_id}).data
