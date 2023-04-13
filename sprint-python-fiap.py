# Importanto Biblioteca Math
import math

Qm = float(input("Digite o valor de Qm:"))
r = float(input("Digite o valor da taxa de crescimento do fitoplâncton (0.5 a 1.5):"))

# Validando variável r, para que os valores não estejam acima dos conformes, caso esteja, aparecerá um aviso para tentar novamente.
while(r < 0.5) or (r > 1.5):
    r = float(input("\033[1;31mValor da taxa de crescimento de planctôn está fora dos conformes, tente novamente:\033[1;30m"))

t = float(input("Digite o valor de t (tempo):"))
e = 0.5

# Definindo função.
def funcao(t):
    return Qm * (1- math.e **(-r*t))

# Exibindo resultado e formatando o resultado para aparecer apenas duas casas decimais.
print(f"\n\033[1;31m {funcao(t):.2f} MLs \033[1;34mde oxigênio serão produzidos.")

# \n --> pular linha
# \033[1;30m --> cor branca.
# \033[1;31m --> cor vermelha.
# \033[1;34m --> cor azul.