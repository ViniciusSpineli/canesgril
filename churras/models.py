from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
#from funcionario.models import Funcionario
from django.contrib.auth.models import User
import uuid

def get_file_path(_instance, filename):
    name = filename.split('.')[0] 
    ext = filename.split('.')[-1]
    filename = f'pratos/{name}-{uuid.uuid4()}.{ext}'
    return filename
class Prato(models.Model):
    nome_prato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.CharField(max_length=255)
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=10)
    categoria = models.CharField(max_length=100)
    date_prato = models.DateTimeField(default=datetime.now, blank=True)
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)
    #foto_prato = models.ImageField(upload_to=get_file_path, blank=True)
    foto_prato = CloudinaryField(
        'foto_do_prato',
        folder='canesgril_pratos',
        transformation={
            'width': 600,
            'crop': 'limit',
        },
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome_prato
    
