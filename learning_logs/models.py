from django.db import models

class Topic(models.Model):
    """Um topico que o usuario esta aprendendo"""
    text= models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        """Retorna uma representacao de string do modelo"""
        return self.text