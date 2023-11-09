from cpf_cnpj import Documento
from TelefonesBr import TelefoneBr
import re
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

cpf = "36650057878"
obj_cpf = Documento.cria_documento(cpf)
print(obj_cpf)

cnpj = "44748402456385"
obj_cnpj = Documento.cria_documento(cnpj)
print(obj_cnpj)
print()

#1 numero, duas letras, e um numero no final 1ac2
padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1ac2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta.group())

padrao_email = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto_email = "aaabbbccc adrianohenriquesds@gmail.com.br gfdsggfdsgfdsgfdsfds"
resposta_email = re.search(padrao_email, texto_email)
print(resposta_email.group())

telefone = "5511971339033"
telefone_obj = TelefoneBr(telefone)
print(telefone_obj)

print("#########################")
print()

cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)

print("#########################")
print()

cadastro = DatasBr()
print(cadastro.tempo_cadastro())

print("######################### CEP ###############")
print()

cep = 13212321
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)
bairro, cidade, uf = objeto_cep.acesso_via_cep()
print(bairro, cidade, uf)