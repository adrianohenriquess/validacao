from cpf_cnpj import Documento

cpf = "36650057878"
obj_cpf = Documento.cria_documento(cpf)
print(obj_cpf)

cnpj = "44748402456385"
obj_cnpj = Documento.cria_documento(cnpj)
print(obj_cnpj)
