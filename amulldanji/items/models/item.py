from django.db.models import models


class Item(models.Modle):

    title = models.CharField(
            max_length=50,
            )

    content = models.textField()


    def __str__(self):
        return self.title()
