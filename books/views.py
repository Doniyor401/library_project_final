from .models import Book
from .serializers import BookSerializer


from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

# Create your views here.


# function based view in DRF 2 lasini vazifasi bir xil pasdigi BookListApiView bn
# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)


# class based view in DRF- Bu tavsiya etiladi ! yani class bn - recomended
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned {len(books)} books',
            'books': serializer_data
        }
        return Response(data)
#################################################################################################


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):

    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer_data = BookSerializer(book).data

        data = {
            "status": f"Successfully retrieved: '{book.title}'",
            "book": serializer_data
        }
        return Response(data)




# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        book.delete()
        data = {
            'status': True,
            'message': f'{book.title} - successfully deleted!!'
        }
        return Response(data)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True) # partial dgani 1 tasiniyam ozgartirvuradi
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {"status": True,
             "message": f"Book {book_saved} updated successfully!"
            }
        )






# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            books = serializer.save()
            data = {'status': f'Books are saved to the database',
                    'books': data
                    }
        return Response(data)

##################################################################################

# generic views
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ViewSet
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

    # crud -> create, read, delete, update