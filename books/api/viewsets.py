from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.api.serializers import BooksSerializer
from books.models import Books


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
