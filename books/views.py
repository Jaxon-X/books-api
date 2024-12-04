from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        data = {
            "status": f" Returned {len(books)}",
            "data": serializer.data
        }
        return  Response(data)

# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer = BookSerializer(book)
            return  Response(serializer.data)
        except Exception:
            return  Response({
                "status": False,
                "message": "Book no found",

            }, status=status.HTTP_404_NOT_FOUND)

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return  Response({
                "status": True,
                "message": "Book deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception:
            return  Response({
                "status": False,
                "message": "Book no found",
            },status=status.HTTP_404_NOT_FOUND)

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            data = request.data
            serializer = BookSerializer(book, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except Exception:
            return Response({
                "status":False,
                "message":"book not found "
            }, status = status.HTTP_404_NOT_FOUND)


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateApiView(APIView):

    def post(self,request):
        try:
            newBook = request.data
            serializer = BookSerializer(data=newBook)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Error:", str(e))
            return Response({
                "status": False,
                "message": "Error occurred while creating the book."
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







