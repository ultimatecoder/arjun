from rest_framework import viewsets

from team import models, serializers


class MemberViewSet(viewsets.ModelViewSet):
    """Creates an API endpoints. Supports CRUD operations"""

    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
