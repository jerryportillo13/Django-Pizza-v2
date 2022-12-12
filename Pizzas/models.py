from django.db import models

# Create your models here.
class Pizza(models.Model): #Topic
    pizza_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img',blank=True,null=True)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model): #Entry
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.topping_name


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'


    def __str__(self):
        return f"{self.text[:50]}..."





