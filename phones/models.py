from django.db import models

class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True
class Phone(models.Model):
    # id = models.AutoField()
    # objects = None
    name = models.CharField(max_length=50)
    price = models.FloatField(max_length=15)
    image = models.ImageField(max_length=100)
    release_date = models.DateField(max_length=10)
    lte_exists = models.TextField()
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return f"{self.name}{self.price}{self.image}{self.release_date}{self.lte_exists}{self.slug}"

# phone_ = Phone.objects.all()
# print(phone_)