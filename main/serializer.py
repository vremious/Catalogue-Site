from rest_framework import serializers
from .models import Models, Company, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ModelsSerializer(serializers.ModelSerializer):
    # company = serializers.SlugRelatedField(queryset=Company.objects.all(), slug_field='company')
    # type_fk = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='type')

    class Meta:
        model = Models
        fields = '__all__'
        depth = 1


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['company'] = instance.company.company
        rep['type'] = instance.type_fk.type
        return rep
