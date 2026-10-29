from django.db import models

# Create your models here.


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
    

class Todo(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    


# MVT 





