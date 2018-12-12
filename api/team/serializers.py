# -*- coding: utf-8 -*-

from rest_framework import serializers

from team import models


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Member
        fields = ('id', 'firstname', 'lastname', 'phone', 'email', 'role')
