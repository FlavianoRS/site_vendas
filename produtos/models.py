from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
        
class Produto(models.Model):
    
    img = models.ImageField(upload_to='img_produtos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome
    
class Carrinho(models.Model):
        pass