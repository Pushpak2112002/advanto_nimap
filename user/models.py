from django.db import models

###############################################
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    
class clients(models.Model):
    company_id=models.AutoField(primary_key=True)
    client_name=models.CharField(max_length=50)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=30)

class project(models.Model):
    project_id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=50)
    Time_stand=models.DateField()
    