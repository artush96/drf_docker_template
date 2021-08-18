from collections import OrderedDict

from rest_framework import filters, pagination, serializers
from rest_framework.response import Response


class ModelFilterBackend(filters.BaseFilterBackend):
    """
    Custom filter backend

    filter_params = {
        'attr': 'field__with__lookup'
    }
    """

    def filter_queryset(self, request, queryset, view):
        filters = {}
        for attr, field in view.filter_params.items():
            if attr in request.query_params:
                value = request.query_params.get(attr)
                filters[field] = value

        return queryset.filter(**filters)


class LimitOffsetPagination(pagination.LimitOffsetPagination):
    max_limit = 10000
    min_limit = 1
    min_offset = 0
    max_offset = 10000

    def paginate_queryset(self, queryset, request, view=None):

        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')

        if limit:
            limit = int(limit)
            if limit > self.max_limit:
                raise serializers.ValidationError({'limit': [
                    'Limit should be less than or equal to %s' % self.max_limit]})
            elif limit < self.min_limit:
                raise serializers.ValidationError({'limit': [
                    'Limit should be greater than or equal to %s' % self.min_limit]})
        if offset:
            offset = int(offset)
            if offset > self.max_offset:
                raise serializers.ValidationError({'offset': [
                    'Offset should be less than or equal to %s' % self.max_offset]})
            elif offset < self.min_offset:
                raise serializers.ValidationError({'offset': [
                    'Offset should be greater than or equal to %s' % self.min_offset]})

        return super(self.__class__, self).paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('limit', self.limit),
            ('offset', self.offset),
            ('count', self.count),
            ('results', data)
        ]))
