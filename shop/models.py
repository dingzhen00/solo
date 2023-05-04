from django.db import models
# from order.models import Order


class eletronics(models.Model):
    eid= models.AutoField(primary_key=True)
    name = models.CharField("", max_length=250, default="")
    main_category = models.CharField("", max_length=250, default="")
    sub_category = models.CharField("", max_length=250, default="")
    ratings = models.CharField("", max_length=250, default="")
    no_of_ratings = models.CharField("", max_length=250, default="")
    discount_price = models.CharField("", max_length=250, default="")
    actual_price = models.CharField("", max_length=250, default="")



class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50,default='')
    identity= models.CharField(max_length=50,default='customer')

    def __str__(self):
        return self.username

class Part(models.Model):
    eletronics = models.ForeignKey(to=eletronics, to_field="eid", on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    amount=models.IntegerField()
    time = models.CharField(max_length=250)
    eletronics=models.ManyToManyField(Part)
    user=models.ForeignKey(to=User, to_field="id", on_delete=models.CASCADE)

class eletronicsdetail(models.Model):
    did = models.AutoField(primary_key=True)
    img=models.TextField("grapg",default="")
    href= models.TextField("link",default="")
    eletronics = models.ForeignKey(to=eletronics, to_field="eid", on_delete=models.CASCADE)