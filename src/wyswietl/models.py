from django.db import models

# Create your models here.
class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    data_dodania = models.DateField()
    data_przydatnosci = models.DateField()
    komentarz = models.TextField()

    def __str__(self):
        return self.nazwa + " | " + str(self.data_dodania) + " | " + str(self.data_przydatnosci)