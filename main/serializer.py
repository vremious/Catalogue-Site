from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Models, Company, Type


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        search = self.slug_field + '__iexact'
        try:
            return self.get_queryset().get(**{search: data})
        except ObjectDoesNotExist:
            return self.get_queryset().create(**{self.slug_field: data})  # to create the object
        except (TypeError, ValueError):
            self.fail('invalid')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ModelsSerializer(serializers.ModelSerializer):
    company = CreatableSlugRelatedField(queryset=Company.objects.all(), slug_field='company')
    type_fk = CreatableSlugRelatedField(queryset=Type.objects.all(), slug_field='type')

    class Meta:
        model = Models
        fields = '__all__'
        # depth = 1

    def create(self, validated_data):
        company_name = validated_data.pop('company')
        type_name = validated_data.pop('type_fk')
        company_instance, created_company = Company.objects.get_or_create(company__iexact=company_name)
        type_instance, created_type = Type.objects.get_or_create(type__iexact=type_name)
        new_model = Models.objects.create(**validated_data, company=company_instance, type_fk=type_instance)
        return new_model


