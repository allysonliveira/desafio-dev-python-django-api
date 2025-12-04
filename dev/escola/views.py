from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import connection
from django.shortcuts import render

from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

# (BACKEND) 

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    @action(detail=True, methods=['get'])
    def matriculas(self, request, pk=None):
        aluno = self.get_object()
        matriculas = Matricula.objects.filter(aluno=aluno)
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    @action(detail=True, methods=['post'])
    def pagar(self, request, pk=None):
        matricula = self.get_object()
        matricula.status = 'pago'
        matricula.save()
        return Response({'status': 'matrícula atualizada para pago'})

class RelatorioCursosView(APIView):
    def get(self, request):
        query = """
            SELECT 
                c.nome, 
                COUNT(m.id) as total_alunos, 
                COALESCE(SUM(c.valor_inscricao), 0) as receita_total
            FROM escola_curso c
            LEFT JOIN escola_matricula m ON c.id = m.curso_id
            GROUP BY c.nome
            ORDER BY total_alunos DESC;
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        
        resultado = [
            {
                "curso": row[0],
                "alunos_matriculados": row[1],
                "receita_total": row[2]
            } 
            for row in rows
        ]
        return Response(resultado)

# (FRONTEND) VISUALIZAÇÃO DOS RELATÓRIOS HTML

def relatorio_dashboard(request):
    """
    Exibe dashboard geral com totais.
    Requisitos: Total de alunos, Cursos ativos, Matrículas pagas vs pendentes.
    """
    total_alunos = Aluno.objects.count()
    cursos_ativos = Curso.objects.filter(status='ativo').count()
    matriculas_pagas = Matricula.objects.filter(status='pago').count()
    matriculas_pendentes = Matricula.objects.filter(status='pendente').count()

    context = {
        'total_alunos': total_alunos,
        'cursos_ativos': cursos_ativos,
        'matriculas_pagas': matriculas_pagas,
        'matriculas_pendentes': matriculas_pendentes,
    }
    return render(request, 'escola/dashboard.html', context)

def relatorio_historico(request):
    """
    Lista histórico do aluno: Cursos matriculados e status.
    """
    # prefetch_related otimiza a busca das matrículas para cada aluno
    alunos = Aluno.objects.prefetch_related('matriculas__curso').all()
    
    context = {
        'alunos': alunos
    }
    return render(request, 'escola/historico.html', context)

def home(request):
    """
    Landing Page que centraliza o acesso.
    """
    return render(request, 'escola/home.html')