import numpy as np
import pandas as pd
from numpy import arange
import matplotlib.pyplot as plt


def fx(weight):
    return int((weight * 2.6) - 8.6)


data = pd.read_excel("Dataset2.ods")
# df = pd.DataFrame(data)
weights = data['Peso(kg)']
heights = data['Altura (cm)']

# calculo do valor previsto
for weight, height in zip(weights, heights):
    print(f'Valor previsto pelo modelo ({weight}Kg) = {fx(weight)}cm')

# coeficiente de correlação
coefcorr = np.corrcoef(weights, heights)

# Exibindo os coeficientes de correlação em uma tabela formatada
msg = '\nCorrelação entre Peso(Kg) e Altura(cm) na nossa base de dados:'
print(msg)
print(f'\t\t\tPeso(Kg)   Altura(cm)')
for line in coefcorr:
    print(f'\t\t\t{line[0]:^10.2f} {line[1]:^12.2f}')

# modelo de previsão
dom = np.arange(0, max(heights), 5)
rline = (dom * 2.6) - 8.60

# parâmetros do gráfico
plt.xlabel('Peso (Kg)')
plt.ylabel('Altura (cm)')
plt.xlim(40, 120)
plt.ylim(140, 220)
plt.scatter(weights, heights)
plt.plot(dom, rline, label='y= 2,6x -8,6', color='red')

# trecho responsável por plotar o gráfico
plt.grid(True)
plt.show()
