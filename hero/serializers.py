from rest_framework import serializers

from book.models import HeroInfo


class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = '__all__'