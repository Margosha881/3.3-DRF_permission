from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement, Favorite


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status']


class FavoriteFilter(filters.FilterSet):
    class Meta:
        model = Favorite
        fields = ['person']
