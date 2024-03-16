from django.db import models

class Feedback(models.Model):
    username=models.CharField(max_length=10)
    feedback=models.TextField(max_length=1500)
    
    def __str__(self):
        return self.username
    
class Contact(models.Model):
    email=models.CharField(max_length=20)
    text=models.TextField(max_length=122)
    #for contact user name in database or email then use this function
    def __str__(self):
        return self.email
        