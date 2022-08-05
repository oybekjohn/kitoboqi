from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView, DetailView

from books.models import Book, BookReview
from books.forms import BookReviewForm


# class BooksView(ListView):
#     template_name = "books/list.html"
#     queryset = Book.objects.all()
#     context_object_name = "books"
#     paginate_by = 3


# class BookDetailView(DetailView):
#     template_name = "books/detail.html"
#     # queryset = Book.objects.all()
#     pk_url_kwarg = "id"  # modeldan urlga berilgan nom boyicha objectni query qiberadi
#     model = Book



class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by("id")

        search_query = request.GET.get("q", "")
        if search_query:
            books = Book.objects.filter(title__icontains=search_query)

        page_size = request.GET.get('page_size', 3)
        pagination = Paginator(books, page_size)

        page_num = request.GET.get("page", 1)
        page_obj = pagination.get_page(page_num)
        return render(
            request, 
            'books/list.html', 
            { "page_obj": page_obj, "search_query": search_query }
            )

 


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        context = {
            "book": book,
            "review_form": review_form
        }
        return render(request, "books/detail.html", context)

class AddReviewView(View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book = book,
                user = request.user,
                stars_given = review_form.cleaned_data['stars_given'],
                comment = review_form.cleaned_data['comment'],
            )

            return redirect(reverse("books:detail", kwargs={'id':book.id}))

        context = {
            "book": book,
            "review_form": review_form
        }
        return render(request, "books/detail.html", context)