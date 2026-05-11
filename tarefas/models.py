from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    imagem = models.ImageField(
        upload_to='tarefas/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo