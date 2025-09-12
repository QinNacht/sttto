from django.db import models

class Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    registered_date = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"
    
    