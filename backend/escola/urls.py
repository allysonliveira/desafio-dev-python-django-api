from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AlunoViewSet, 
    CursoViewSet, 
    MatriculaViewSet, 
    RelatorioCursosView,
    relatorio_dashboard,  # <--- Nova importação
    relatorio_historico   # <--- Nova importação
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    path('relatorio-cursos/', RelatorioCursosView.as_view(), name='relatorio-cursos'),

    # Relatórios HTML (Frontend)
    path('dashboard/', relatorio_dashboard, name='dashboard'),
    path('historico/', relatorio_historico, name='historico'),
]