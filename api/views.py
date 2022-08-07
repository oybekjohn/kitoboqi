from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from books.models import Book, BookReview
from api.serializers import BookReviewSerializer


class BookReviewDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]   # LoginRequiredMixen ni orniga user login qilganligini tekshiradi, listga ozimiz class yozib permission yozishimiz mumkin 
                                             # masalan email check lass yozib shu listga qushsak bualdi
    
    def get (self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(book_review)
        return Response(data=serializer.data)


class BookReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by("-created_at")

        #paginatsiya qilish
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)
        serializer = BookReviewSerializer(page_obj, many=True)\

        # return Response(data=serializer.data)                     # bunda datani ozini yuboradi 
        return paginator.get_paginated_response(serializer.data)    # bunda count, next, previous pages and results yuboradi


