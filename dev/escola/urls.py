from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AlunoViewSet, 
    CursoViewSet, 
    MatriculaViewSet, 
    RelatorioCursosView,
    relatorio_dashboard,
    relatorio_historico,
    home # <--- Importe a home
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    # Rota Raiz (Landing Page)
    path('', home, name='home'), # Raiz acessa a Home
    
    # API endpoints
    path('api/', include(router.urls)), # API acessa via /api/
    path('api/relatorio-cursos/', RelatorioCursosView.as_view(), name='relatorio-cursos'),
    
    # Relatórios HTML
    path('api/dashboard/', relatorio_dashboard, name='dashboard'),
    path('api/historico/', relatorio_historico, name='historico'),
]