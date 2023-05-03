from django.db import models
import uuid

# Create your models here.
class Copy(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_avaliable = models.BooleanField(default=False)

    books = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copy_book", default=None
    )

    user = models.ManyToManyField(
        "users.User", through="LoandBook", related_name="book_loand"
    )


class LoandBook(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    users = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_loand_book"
    )
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="copy_loand_book"
    )

    devoluiton_date = models.DateField()
    borrowed_date = models.DateField(auto_now_add=True)
