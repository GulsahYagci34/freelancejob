from django.db import models

#Category Model
class Category(models.Model):
    name = models.CharField(max_length=40,verbose_name="Kategori")
    slug = models.SlugField(max_length=40,unique=True)


    def __str__(self):
        return self.name

#Location Model
class Location(models.Model):
    name = models.CharField(max_length=50,verbose_name="Lokasyon")
    slug = models.SlugField(max_length=40,unique=True)

    def __str__(self):
        return self.name

#Mission Model
class Mission(models.Model):
    title = models.CharField(max_length=150,verbose_name="Başlık")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Kategori")
    location = models.ForeignKey(Location,on_delete=models.CASCADE,verbose_name="Lokasyon")
    createdBy = models.ForeignKey("auth.User",on_delete=models.CASCADE,default=1,verbose_name="Yayınlayan")
    mission = models.TextField(max_length=500,verbose_name="Görev Detayları")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlandığı Tarih")
    budget = models.FloatField(null=True, blank=True, default=None,verbose_name="Bütçe")

    def __str__(self):
        return self.title
    class Meta:
        ordering= ["-date"]

