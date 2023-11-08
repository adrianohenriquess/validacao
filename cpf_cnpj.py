from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError("Quantidade de digitos está incorreta.")


class DocCPF:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        return CPF().validate(documento)

    def format(self):
        return CPF().mask(self.cpf)


class DocCNPJ:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        return CNPJ().validate(documento)

    def format(self):
        return CNPJ().mask(self.cnpj)