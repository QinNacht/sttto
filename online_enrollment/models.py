from django.db import models

# Create your models here.
# class TestingDatabase(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     registration_date = models.DateField(max_length=100)

#     def __str__(self):
#         return f"{self.first_name}"

class Students(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.CharField(max_length=100)
    Contact_No = models.CharField(max_length=12)
    Student_ID = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Name}"
    
class Additonal_Info(models.Model):
    Civil_Status = models.CharField(max_length=100)
    Nationality = models.CharField(max_length=100)
    Religion = models.CharField(max_length=100)
    Person_with_Disability = models.BooleanField()
    Sped_Student = models.BooleanField()

    def __str__(self):
        return f"{self.Civil_Status}"

class Address(models.Model):
    Region = models.CharField(max_length=100)
    Province = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Barangay = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Region}"

class EducationBG(models.Model):
    School = models.CharField(max_length=100)
    Year = models.CharField(max_length=4)
    Achievements = models.CharField(max_length=100)
    AVG_grade = models.DecimalField(max_digits=2, decimal_places=0)
    Status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.School}"

class Account(models.Model):
    stud_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    e_mail = models.CharField(max_length=100)
    first_pet_name = models.CharField(max_length=100)
    your_bestfriend = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.stud_id}"