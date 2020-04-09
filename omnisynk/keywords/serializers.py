from rest_framework import serializers
from omnisynk.keywords.models import  Example, KeyWordsGenerationMethods, KeyWordsGenerationResults

class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Example
        fields = ['text']

class KeyWordsGenerationMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWordsGenerationMethods
        fields = '__all__'

class KeyWordsGenerationResultsSerializer(serializers.HyperlinkedModelSerializer):
    id_example = ExampleSerializer( read_only=True)
    class Meta:
        model = KeyWordsGenerationResults
        fields = ['method_name', 'id_example', 'keywords']