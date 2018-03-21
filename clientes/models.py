from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('deletar_clientes', 'Deletar clientes'),
        )

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name
