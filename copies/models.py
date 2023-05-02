from django.db import models


# Create your models here.
class Copy(models.Model):
    is_avaliable = models.BooleanField(default=False)

    books = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copy_book", default=None
    )

    user = models.ManyToManyField(
        "users.User", through="LoandBook", related_name="book_loand"
    )


class LoandBook(models.Model):
    users = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_loand_book"
    )
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="copy_loand_book"
    )

    devoluiton_date = models.DateField()
    borrowed_date = models.DateField(auto_now_add=True)
