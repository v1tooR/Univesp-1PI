from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tamanho = models.CharField(max_length=50, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='produtos/', blank=True, null=True)

    class Meta:
        app_label = 'univesp-1pi'  # Fundamental para o Django reconhecer o modelo