
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from blog.models import BlogModel
from blog.serializers import BlogSerializer


class BlogViewset(viewsets.ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer

	@action(detail=True, methods=['get'])
	def cool_blogs(self, request, pk=None):
		blogs = BlogModel.objects.filter(pk=pk)
		sr = BlogSerializer(blogs, many=True)
		return Response({'data': sr.data})
