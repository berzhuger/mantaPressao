from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=256, verbose_name='Nome do Paciente')
    dataNascimento = models.DateField('Data Nascimento')


class Avaliacao(models.Model):
    idPaciente = models.ForeignKey(
        'Paciente',
        on_delete=models.CASCADE,  
        verbose_name='Paciente',
        related_name='avaliacao',
    )
    dataInicio = models.DateField('Data Inicio')
    dataFim = models.DateField('Data Data Fim')
    atendimento = models.IntegerField(verbose_name='Numero Atendimento')

class DadosSensor(models.Model):
    idAvaliacao = models.ForeignKey(
        'Avaliacao',
        on_delete=models.CASCADE,  
        verbose_name='Avaliacao',
        related_name='dadosAvaliacao',
    )
    dataHora = models.DateField('Data Hora')
    dadosSensor01 = models.DecimalField(("Valor  1"), max_digits=10, decimal_places=5)
    dadosSensor02 = models.DecimalField(("Valor  2"), max_digits=10, decimal_places=5)
    dadosSensor03 = models.DecimalField(("Valor  3"), max_digits=10, decimal_places=5)
    dadosSensor04 = models.DecimalField(("Valor  4"), max_digits=10, decimal_places=5)
    dadosSensor05 = models.DecimalField(("Valor  5"), max_digits=10, decimal_places=5)
    dadosSensor06 = models.DecimalField(("Valor  6"), max_digits=10, decimal_places=5)
    dadosSensor07 = models.DecimalField(("Valor  7"), max_digits=10, decimal_places=5)
    dadosSensor08 = models.DecimalField(("Valor  8"), max_digits=10, decimal_places=5)
    dadosSensor09 = models.DecimalField(("Valor  9"), max_digits=10, decimal_places=5)
    dadosSensor10 = models.DecimalField(("Valor 10"), max_digits=10, decimal_places=5)
    dadosSensor11 = models.DecimalField(("Valor 11"), max_digits=10, decimal_places=5)
    dadosSensor12 = models.DecimalField(("Valor 12"), max_digits=10, decimal_places=5)
    dadosSensor13 = models.DecimalField(("Valor 13"), max_digits=10, decimal_places=5)
    dadosSensor14 = models.DecimalField(("Valor 14"), max_digits=10, decimal_places=5)
    dadosSensor15 = models.DecimalField(("Valor 15"), max_digits=10, decimal_places=5)
    dadosSensor16 = models.DecimalField(("Valor 16"), max_digits=10, decimal_places=5)
    dadosSensor17 = models.DecimalField(("Valor 17"), max_digits=10, decimal_places=5)
    dadosSensor18 = models.DecimalField(("Valor 18"), max_digits=10, decimal_places=5)
    dadosSensor19 = models.DecimalField(("Valor 19"), max_digits=10, decimal_places=5)
    dadosSensor20 = models.DecimalField(("Valor 20"), max_digits=10, decimal_places=5)
    dadosSensor21 = models.DecimalField(("Valor 21"), max_digits=10, decimal_places=5)
    dadosSensor22 = models.DecimalField(("Valor 22"), max_digits=10, decimal_places=5)
    dadosSensor23 = models.DecimalField(("Valor 23"), max_digits=10, decimal_places=5)
    dadosSensor24 = models.DecimalField(("Valor 24"), max_digits=10, decimal_places=5)
    dadosSensor25 = models.DecimalField(("Valor 25"), max_digits=10, decimal_places=5)
    dadosSensor26 = models.DecimalField(("Valor 26"), max_digits=10, decimal_places=5)
    dadosSensor27 = models.DecimalField(("Valor 27"), max_digits=10, decimal_places=5)
    dadosSensor28 = models.DecimalField(("Valor 28"), max_digits=10, decimal_places=5)
    dadosSensor29 = models.DecimalField(("Valor 29"), max_digits=10, decimal_places=5)
    dadosSensor30 = models.DecimalField(("Valor 30"), max_digits=10, decimal_places=5)
    dadosSensor31 = models.DecimalField(("Valor 31"), max_digits=10, decimal_places=5)
    dadosSensor32 = models.DecimalField(("Valor 32"), max_digits=10, decimal_places=5)
    dadosSensor33 = models.DecimalField(("Valor 33"), max_digits=10, decimal_places=5)
    dadosSensor34 = models.DecimalField(("Valor 34"), max_digits=10, decimal_places=5)
    dadosSensor35 = models.DecimalField(("Valor 35"), max_digits=10, decimal_places=5)
    dadosSensor36 = models.DecimalField(("Valor 36"), max_digits=10, decimal_places=5)
    dadosSensor37 = models.DecimalField(("Valor 37"), max_digits=10, decimal_places=5)
    dadosSensor38 = models.DecimalField(("Valor 38"), max_digits=10, decimal_places=5)
    dadosSensor39 = models.DecimalField(("Valor 39"), max_digits=10, decimal_places=5)
    dadosSensor40 = models.DecimalField(("Valor 40"), max_digits=10, decimal_places=5)
    dadosSensor41 = models.DecimalField(("Valor 41"), max_digits=10, decimal_places=5)
    dadosSensor42 = models.DecimalField(("Valor 42"), max_digits=10, decimal_places=5)
    dadosSensor43 = models.DecimalField(("Valor 43"), max_digits=10, decimal_places=5)
    dadosSensor44 = models.DecimalField(("Valor 44"), max_digits=10, decimal_places=5)
    dadosSensor45 = models.DecimalField(("Valor 45"), max_digits=10, decimal_places=5)
    dadosSensor46 = models.DecimalField(("Valor 46"), max_digits=10, decimal_places=5)
    dadosSensor47 = models.DecimalField(("Valor 47"), max_digits=10, decimal_places=5)
    dadosSensor48 = models.DecimalField(("Valor 48"), max_digits=10, decimal_places=5)
    dadosSensor49 = models.DecimalField(("Valor 49"), max_digits=10, decimal_places=5)
    dadosSensor50 = models.DecimalField(("Valor 50"), max_digits=10, decimal_places=5)
    dadosSensor51 = models.DecimalField(("Valor 51"), max_digits=10, decimal_places=5)
    dadosSensor52 = models.DecimalField(("Valor 52"), max_digits=10, decimal_places=5)
    dadosSensor53 = models.DecimalField(("Valor 53"), max_digits=10, decimal_places=5)
    dadosSensor54 = models.DecimalField(("Valor 54"), max_digits=10, decimal_places=5)
    dadosSensor55 = models.DecimalField(("Valor 55"), max_digits=10, decimal_places=5)
    dadosSensor56 = models.DecimalField(("Valor 56"), max_digits=10, decimal_places=5)    

    
