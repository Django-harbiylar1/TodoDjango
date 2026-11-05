from django.db import models

# Create your models here.


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        
    
    def __str__(self):
        return self.name

    
    

class Todo(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="todo/", blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="todos")
    
    class Meta:
        verbose_name = "Vazifa"
        verbose_name_plural = "Vazifalar"
        
    def __str__(self):
        return self.title


    



    


# MVT 





