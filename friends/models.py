from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Friends(models.Model):
    name = models.CharField(max_length=50, null=False)
    dob = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50, unique=True)
    instagram = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    postal_code = models.CharField(max_length=50)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
