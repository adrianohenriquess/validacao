import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}.{}-{}".format(self.cep[:2], self.cep[2:5], self.cep[5:])


    def acesso_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json".format(self.cep)
        dados = requests.get(url).json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )