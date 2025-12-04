from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    # Exibe os dados aninhados para facilitar a leitura (opcional, mas ajuda)
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    curso_nome = serializers.ReadOnlyField(source='curso.nome')

    class Meta:
        model = Matricula
        fields = ['id', 'aluno', 'aluno_nome', 'curso', 'curso_nome', 'data_matricula', 'status']
