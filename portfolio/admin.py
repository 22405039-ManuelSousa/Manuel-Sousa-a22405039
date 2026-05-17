from django.contrib import admin
from .models import (
    Docente, Licenciatura, UnidadeCurricular,
    Tecnologia, Projeto, TFC,
    Competencia, Formacao, MakingOf, Conquista
)


class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "url_lusofona")
    ordering = ("nome",)
    search_fields = ("nome", "email")


class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nome", "ects")
    ordering = ("nome",)
    search_fields = ("nome", "sigla")


class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "ano", "semestre", "obrigatoria")
    ordering = ("ano", "semestre", "nome")
    search_fields = ("nome", "sigla")
    list_editable = ("obrigatoria",)


class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "nivel")
    ordering = ("nome",)
    search_fields = ("nome",)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "unidade_curricular", "destaque")
    ordering = ("titulo",)
    search_fields = ("titulo",)
    list_editable = ("destaque",)


class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "aluno", "orientador", "ano", "destaque")
    ordering = ("-ano",)
    search_fields = ("titulo", "aluno")
    list_editable = ("destaque",)


class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel")
    ordering = ("tipo", "nome")
    search_fields = ("nome",)


class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "data_inicio", "data_fim")
    ordering = ("-data_fim",)
    search_fields = ("nome",)


class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("titulo", "entidade_relacionada")
    ordering = ("titulo",)
    search_fields = ("titulo",)



class ConquistaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo")
    ordering = ("titulo",)
    search_fields = ("titulo",)
    
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(TFC, TFCAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(MakingOf, MakingOfAdmin)
admin.site.register(Conquista, ConquistaAdmin)