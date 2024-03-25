
# Quantidade mínima do produto foi colocada em 1, pois se for 0 não há como adicionar no estoque
MINIMO_PRODUTO = 1

# Um valor limite de 100 produtos foi adicionado ao estoque para ilustração do cálculo de porcentagem
ESTOQUE = 100

quantidade_total = 0

print("Digite a categoria do produto:\n")
categoria_prod = input()

print("Digite o nome do produto:\n")
nome_prod = input()

print("Digite a quantidade do produto:\n")
quantidade_prod = int(input())

if quantidade_prod < MINIMO_PRODUTO:
    print("Registro invalido. Quantidade do produto não pode ser menor que 1.\n")
else:
    quantidade_total += quantidade_prod
    porcentagem_prod = (quantidade_prod * 100) / ESTOQUE

print('A quantidade total de produtos no estoque é: {}\n'.format(quantidade_total))
print('Os produtos da categoria {} compõem {}% do estoque total'.format(categoria_prod,porcentagem_prod))