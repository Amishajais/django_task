from django.shortcuts import render
from rest_framework import viewsets, status
from encroachment.models.models import Encroachment_table
from rest_framework.response import Response
from .serializers import EncroachmentSerializer


# Create your views here.
class EncroachmentViewSet(viewsets.ModelViewSet):
    def get(self, request, id=None):
        if id:
            item = Encroachment_table.objects.get(id=id)
            serializer = EncroachmentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Encroachment_table.objects.all()
        serializer = EncroachmentSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def get_queryset(self):
        item = self.request.query_params.get('department', None)
        if item is not None:
            return Encroachment_table.objects.filter(department__contains=item)
        return Encroachment_table.objects.all()

    def post(self, request):
        serializer = EncroachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    queryset = Encroachment_table.objects.all()
    serializer_class = EncroachmentSerializer
    
    def patch(self, request, id=None):
        item = Encroachment_table.objects.get(id=id)
        serializer = EncroachmentSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self,id):
        item=Encroachment_table.objects.get(id=id)
        item.delete()

    