from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True) # Ex: 000.000.000-00
    data_ingresso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    nome = models.CharField(max_length=255)
    carga_horaria = models.PositiveIntegerField(help_text="Carga horária em horas")
    valor_inscricao = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    STATUS_MATRICULA = [
        ('pago', 'Pago'),
        ('pendente', 'Pendente'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_MATRICULA, default='pendente')

    class Meta:
        # Garante que um aluno não se matricule 2x no mesmo curso (opcional, mas boa prática)
        unique_together = ('aluno', 'curso') 

    def __str__(self):
        return f"{self.aluno} - {self.curso}"