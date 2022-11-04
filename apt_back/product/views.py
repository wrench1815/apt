from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product
from .serializers import ProductSerializer, ProductUpdateSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['$name']
    ordering_fields = ['date_added']
    ordering = '-date_added'


class ProductRetrieveUpdateAPIView(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        product = self.get_object()

        try:
            serializer = ProductUpdateSerializer(
                product,
                data=request.data,
                partial=True,
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

        except Exception as ex:
            return Response(
                {'detail': str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response = ProductSerializer(product)

        return Response(
            response.data,
            status=status.HTTP_200_OK,
        )
