from dataclasses import fields
from rest_framework import serializers
from .models import Link


class LinkSerializers(serializers.ModelSerializers):
    class Meta:
        model = Link
        fields = "__all__"