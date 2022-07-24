from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn_inHTML", "describtion_short")
    search_fields = ("title", "isbn", "describtion")
    list_filter = ("title", "isbn")

    def describtion_short(self, obj):
        return obj.describtion[:100]

    def isbn_inHTML(self, obj):
        from django.utils.html import format_html
        return format_html("<b><i>{}</i></b>", obj.isbn)

    isbn_inHTML.short_description = "ISBN code"
admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)



#admin register by decorator
@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    search_fields = ('stars_given',)
    list_display = ["get_book_title", "get_user", "stars_given", "comment_fix"]

    def get_book_title(self, obj):
        result = obj.book.title
        return result.title()
    get_book_title.short_description = "Books"
    # get_book_title.admin_order_field = "comment"

    def get_user(self, obj):
        user = obj.user
        return user
    get_user.short_description = "Users"

    def comment_fix(self, obj):
        short_comment = obj.comment
        return short_comment[:50]