from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Book, Author, BookAuthor, BookReview


#book admin view
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "isbn_inHTML", "describtion_short")
    search_fields = ("title", "isbn", "describtion")
    # list_filter = ("title", "isbn")

    # fields = ["title", "isbn", "describtion", "cover_picture"] # admin panelda malumot qo'shish tartibi | ADMIN panelda fields berishni yana bitta yomon tarafi, modelga qoshimcha poliya kiritilsayu bu yerda berilmasa adminda chiqmaydi ;)

    def describtion_short(self, obj):
        return obj.describtion[:100]

    def isbn_inHTML(self, obj):
        from django.utils.html import format_html
        return format_html("<b><u>{}</u></b>", obj.isbn)

    isbn_inHTML.short_description = "ISBN code"
admin.site.register(Book, BookAdmin)


# author admin view
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["get_fullname", "email"]
    search_fields = ('first_name', 'last_name', "email")

    def get_fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    
admin.site.register(Author, AuthorAdmin)


# bookauthor admin view
class AuthorFilter(SimpleListFilter):
    title = "author"         # _("author") for translating
    parameter_name = "author"

    def lookups(self, request, model_admin):
        author_data = [data for data in model_admin.model.objects.all()]
        # print([(author.author.first_name, author.author.last_name) for author in author_data])
        for author in author_data:
            t = [[author.author.first_name, author.author.last_name] for author in author_data]
            print([[author.author.first_name, author.author.last_name] for author in author_data])

            return t
        # return [(author.author.first_name, author.author.last_name) for author in author_data]

    def queryset(self, request, queryset):
        if self.value():
            print(self.value())
            return queryset.filter(author__first_name=self.value())

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ["get_author", "book",]
    search_fields = ["author", "book"]
    list_filter = ["author", "book"]  # list_filter = [AuthorFilter, "book"] - admin filter customized
    fields = ["book", "author"]

    def get_author(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'
    get_author.short_description = "user"

admin.site.register(BookAuthor, BookAuthorAdmin)



# bookreview admin register by decorator
@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    search_fields = ('stars_given',)
    list_display = ["get_book_title", "get_user", "stars_given", "comment_fix", "created_at", "updated_at"]
    

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