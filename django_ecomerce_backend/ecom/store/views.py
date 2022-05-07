from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, permissions


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = ProductSerializer

    def get_queryset(self):
        cat = self.request.query_params.get('cat')
        featured = self.request.query_params.get('featured')
        query= self.request.query_params.get('q')
        queryset = Product.objects.all()
        if cat:
            queryset = Product.objects.filter(category = cat)
        if featured:
            queryset = Product.objects.filter(is_featured = True)
        if query:
            queryset = Product.objects.filter(name__icontains = query)
        return queryset
