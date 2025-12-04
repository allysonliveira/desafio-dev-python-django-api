from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, CursoViewSet, MatriculaViewSet, RelatorioCursosView

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('relatorio-cursos/', RelatorioCursosView.as_view(), name='relatorio-cursos'),
]