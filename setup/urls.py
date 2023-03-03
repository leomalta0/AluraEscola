from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter() # Rota principal default
router.register('alunos', AlunosViewSet, basename='Alunos') # Rota para registrar alunos
router.register('cursos', CursosViewSet, basename='Cursos') # Rota para registrar cursos
router.register('matriculas', MatriculaViewSet, basename='Matriculas') # Rota para registrar matrículas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
