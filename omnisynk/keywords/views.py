from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from omnisynk.keywords.models import  Example, KeyWordsGenerationMethods, KeyWordsGenerationResults
from omnisynk.keywords.serializers import ExampleSerializer, KeyWordsGenerationMethodsSerializer, KeyWordsGenerationResultsSerializer
from omnisynk.keywords.keyword_extractors.lib import Methods
from omnisynk.keywords.keyword_extractors.text_ranker import text_rank
from omnisynk.keywords.keyword_extractors.rake import rake_keywors
from rest_framework.permissions import IsAuthenticated, AllowAny
from omnisynk.keywords.permissions import *
# Create your views here.

METHODS_MAPPING = {
    Methods.TEXT_RANK.value : text_rank,
    Methods.RAKE.value : rake_keywors,
}

# EXAMPLE
class AddExample(generics.ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    permission_classes = [IsAuthenticated, ]

class UpdateExample(generics.RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    permission_classes = [IsAuthenticated, ]

# METHODS
# class ShowMethods(generics.ListCreateAPIView):
#     queryset = KeyWordsGenerationMethods.objects.all()
#     serializer_class = KeyWordsGenerationMethodsSerializer
#
# class UpdateMethods(generics.RetrieveUpdateDestroyAPIView):
#     queryset = KeyWordsGenerationMethods.objects.all()
#     serializer_class = KeyWordsGenerationMethodsSerializer


# RESULTS
class ShowKeyWordsResults(generics.ListAPIView):
    queryset = KeyWordsGenerationResults.objects.all()
    serializer_class = KeyWordsGenerationResultsSerializer
    pagination_classes = [AllowAny, ]

class UpdateKeyWordsResults(generics.RetrieveDestroyAPIView):
    queryset = KeyWordsGenerationResults.objects.all()
    serializer_class = KeyWordsGenerationResultsSerializer
    pagination_class = IsAuthenticated


# Create keywords
class CreateKeyWords(generics.GenericAPIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        examples  = Example.objects.get(id = request.query_params['text_id'])
        exec_class = METHODS_MAPPING[request.query_params['method']]
        key_words = exec_class.get_keywords(text = examples.text)

        KeyWordsGenerationResults.objects.create(id_example = examples,
                                                 method_name = request.query_params['method'],
                                                 keywords = key_words)
        return Response({'result': ', '.join(key_words)})
