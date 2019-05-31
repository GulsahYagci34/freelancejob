from django.db import models

class Category(models.Model):
    categoryId = models.IntegerField(primary_key=True,auto_created=True)
    categories = models.CharField(max_length=30)
    def __str__(self):
        return self.categories


class Location(models.Model):
    localId = models.IntegerField(primary_key=True,auto_created=True)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.location

class Mission(models.Model):
    missionId = models.IntegerField(primary_key=True,auto_created=True)
    startDate = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    createdBy = models.ForeignKey("auth.User",on_delete=models.CASCADE,default=1,verbose_name="Yayınlayan")
    category = models.ForeignKey("mission.Category",on_delete=models.CASCADE,default=1,verbose_name="Kategori")
    location = models.ForeignKey("mission.Location",on_delete=models.CASCADE,default=1,verbose_name="Lokasyon")
    title = models.CharField(max_length=30,verbose_name="İlan Başlığı")
    detail = models.TextField(max_length=400,verbose_name="İlan Detayları")
    budget = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="Bütçe")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-startDate']
