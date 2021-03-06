from .models import Card, Feature, Combo, Variant
from .serializers import CardDetailSerializer, FeatureSerializer, ComboSerializer, VariantSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class VariantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Variant.objects.filter(status=Variant.Status.OK)
    serializer_class = VariantSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['unique_id', 'includes__id', 'produces__id', 'of__id']
    search_fields = ['includes__name', 'produces__name']
    ordering_fields = ['created', 'updated', 'unique_id']


variant_list = VariantViewSet.as_view({'get': 'list'})
variant_detail = VariantViewSet.as_view({'get': 'retrieve'})


class FeatureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


feature_list = FeatureViewSet.as_view({'get': 'list'})
feature_detail = FeatureViewSet.as_view({'get': 'retrieve'})


class ComboViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer


combo_list = ComboViewSet.as_view({'get': 'list'})
combo_detail = ComboViewSet.as_view({'get': 'retrieve'})


class CardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardDetailSerializer


card_list = CardViewSet.as_view({'get': 'list'})
card_detail = CardViewSet.as_view({'get': 'retrieve'})
