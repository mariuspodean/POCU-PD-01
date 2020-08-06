import django_tables2 as tables

class PacientTable(tables.Table):
    class Meta:
        model = Pacient