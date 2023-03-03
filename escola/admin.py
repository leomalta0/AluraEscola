from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome') # Campos clicáveis em admin
    search_fields = ('nome',) # Campos buscáveis
    list_per_page = 10 # Quantos por página

admin.site.register(Aluno, Alunos) # Passa a classe Alunos para o model Aluno

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')

admin.site.register(Curso, Cursos) # Passa a classe Cursos para o model Curso

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)