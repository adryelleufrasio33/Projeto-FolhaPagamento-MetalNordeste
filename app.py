#criar função de calculo do inss ok
# criar função de calculo do fgts
# criar função do calculo de insalubridade
# criar função do calculo de vale transporte
# criar função de calculo do salario liquido

salario = float("Digite seu salario bruto")

menu = [
    ("1 - cadastrar funcionario"),
    ("2 - Atualizar funcionario"),
    ("3 - listar funcionario"),
    ("4 - deletar funcionario")
     

    ]
trabalhador = []

def cadastrar(trabalhador):
    nome = input("Digite seu nome Completo ")
    cpf = input("Digite seu cpf")
    cargo = input("Digite seu cpf")
    ctps = input("digite seu número da carteira social ")
    rg = input("digite seu número do rg")

    funcionario = {
        "nome" : nome,
        "cpf" : cpf,
       " cargo" : cargo,
       " ctps" : ctps,
        "rg" : rg

    }
    trabalhador.append(trabalhador)
    print("Cadastro realizado com sucesso")

def calcular_inss(salario):
    desconto = 0
    

    if salario > 1518:
        desconto += 1518 * 0.075
    else:
        desconto += salario* 0.075
        return desconto
    if salario > 2793.88:
        desconto += (2793.88 - 1518) * 0.09
    else:
        desconto += (salario - 1518) * 0.09
        return desconto
    if salario > 4190.83:
        desconto += (4190.83 - 2793.88) * 0.12
    else:
        desconto += (salario - 2793.88 ) * 0.12
        return desconto
    if salario > 8157.41:
        desconto += (8157.41 - 4190.83 ) * 0.14
        return desconto
    else:
        desconto += (salario - 4190.83) * 0.14
        return desconto
    
def calculo_valeTransporte(salario):
    desconto_transporte = salario * 0.06
    return desconto_transporte
    
        



#while True:
    

    