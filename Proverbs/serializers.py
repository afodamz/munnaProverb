from rest_framework import serializers
from .models import *


class EthnicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Ethnic
        fields = ['id', 'name', 'language', 'state']
        extra_kwargs = {'id': {'read_only': False, 'required': True}}


class InterpreteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Interpretation
        fields = ['id', 'language', 'content']
        extra_kwargs = {'id': {'read_only': False, 'required': True}}


class TranslateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Translation
        fields = ['id', 'language', 'content']
        extra_kwargs = {'id': {'read_only': False, 'required': True}}



class ProverbSerializer(serializers.ModelSerializer):
    # ethnic = EthnicSerializer(many=True, read_only=True)
    ethnic = EthnicSerializer(many=True)
    interpretation = InterpreteSerializer(many=True)
    translation = TranslateSerializer(many=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        ethnic_data = validated_data.pop('ethnic')
        translation_data = validated_data.pop('translation')
        interpretation_data = validated_data.pop('interpretation')

        proverb = Proverb.objects.create(**validated_data)

        for ethnic in ethnic_data:
            Ethnic.objects.create(**ethnic, proverb=proverb)

        for translation in translation_data:
            Translation.objects.create(**translation, proverb=proverb)

        for interpretation in interpretation_data:
            Interpretation.objects.create(**interpretation, proverb=proverb)

        return proverb

    def update(self, instance, validated_data):
        ethnics = validated_data.pop('ethnic', None)
        translations = validated_data.pop('translation', None)
        interpretations = validated_data.pop('interpretation', None)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        # ethnics = validated_data.get('ethnic')
        for ethnic in ethnics:
            ethnic_id = ethnic.get('id', None)
            print(ethnic_id)
            if ethnic_id:
                ethnic_item = Ethnic.objects.get(pk=ethnic_id)
                ethnic_item.name = ethnic.get('name', ethnic_item.name)
                ethnic_item.language = ethnic.get('language', ethnic_item.language)
                ethnic_item.state = ethnic.get('state', ethnic_item.state)
                ethnic_item.save()
            else:
                Ethnic.objects.create(proverb=instance, **ethnic)



        for translation in translations:
            translation_id = translation.get('id', None)
            if translation_id:
                translation_item = Translation.objects.get(pk=translation_id)
                translation_item.content = translation.get('content', translation_item.content)
                translation_item.language = translation.get('language', translation_item.language)
                translation_item.save()
            else:
                Translation.objects.create(proverb=instance, **translation)


        # interpretations = validated_data.get('interpretation')

        for interpretation in interpretations:
            interpretation_id = interpretation.get('id', None)
            if interpretation_id:
                interpretation_item = Interpretation.objects.get(pk=interpretation_id)
                interpretation_item.content = interpretation.get('content', interpretation_item.content)
                interpretation_item.language = interpretation.get('language', interpretation_item.language)
                interpretation_item.save()
            else:
                Interpretation.objects.create(proverb=instance, **interpretation)


        return instance



    class Meta:
        model = Proverb
        fields = ['id', 'author', 'content',
                  'category', 'ethnic',
                  'interpretation', 'translation',
                  'date_created', 'date_modified']


