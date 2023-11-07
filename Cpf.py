from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format_cpf()

    def cpf_eh_valido(self, documento):
        return CPF().validate(documento)

    def format_cpf(self):
        return CPF().mask(self.cpf)