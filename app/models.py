from django.db import models
import django.core.validators

class Produto(models.Model):

    """
    Modelo para armazenar informações dos produtos no estoque da Praado Store.
    
    Campos:
    - nome: Nome do produto (obrigatório)
    - preco: Preço do produto (obrigatório, decimal)
    - tamanho: Tamanho do produto (opcional)
    - cor: Cor do produto (opcional)
    - quantidade: Quantidade em estoque (obrigatório, inteiro)
    - foto: Imagem do produto (opcional)
    - data_cadastro: Data de cadastro do produto (automático)
    - data_atualizacao: Data da última atualização (automático)
    """

    # Campos obrigatórios
    nome = models.CharField(max_length=100, verbose_name="Nome")
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[django.core.validators.MinValueValidator(0.01)],
        verbose_name="Preço"
    )
    quantidade = models.PositiveIntegerField(
        validators=[django.core.validators.MinValueValidator(0)],
        verbose_name="Quantidade"
    )
    
    # Campos opcionais
    tamanho = models.CharField(max_length=20, blank=True, null=True, verbose_name="Tamanho")
    cor = models.CharField(max_length=50, blank=True, null=True, verbose_name="Cor")
    foto = models.ImageField(
        upload_to='produtos/', 
        blank=True, 
        null=True,
        verbose_name="Foto"
    )
    
    # Campos de data automáticos
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    
    def __str__(self):
        """Representação em string do produto"""
        return f"{self.nome} - {self.quantidade} unidades"
    
    class Meta:
        """Meta informações do modelo"""
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']
        app_label = "your_app_name"