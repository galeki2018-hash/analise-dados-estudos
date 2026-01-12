"""
Primeiros Passos em Python e Data Science
Exemplos basicos de manipulacao de dados com Pandas e NumPy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Criando dados com NumPy
print("=" * 50)
print("Exemplo 1: NumPy - Criando arrays")
print("=" * 50)

# Array simples
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Tipo: {type(arr)}")
print(f"Shape: {arr.shape}")
print()

# 2. Trabalhando com Pandas
print("=" * 50)
print("Exemplo 2: Pandas - Criando DataFrame")
print("=" * 50)

# Dados de exemplo
dados = {
    'Nome': ['Alice', 'Bob', 'Carlos', 'Diana'],
    'Idade': [25, 30, 35, 28],
    'Salario': [3000, 4000, 5000, 3500]
}

df = pd.DataFrame(dados)
print("DataFrame:")
print(df)
print()

# 3. Explorando dados
print("=" * 50)
print("Exemplo 3: Explorando dados")
print("=" * 50)

print(f"Info do DataFrame:")
print(df.info())
print()
print(f"Descricao estatistica:")
print(df.describe())
print()

# 4. Operacoes basicas
print("=" * 50)
print("Exemplo 4: Operacoes basicas")
print("=" * 50)

print(f"Salario medio: R$ {df['Salario'].mean():.2f}")
print(f"Idade maxima: {df['Idade'].max()}")
print(f"Idade minima: {df['Idade'].min()}")
print()

# 5. Visualizacao
print("=" * 50)
print("Exemplo 5: Criando graficos")
print("=" * 50)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(df['Nome'], df['Salario'])
plt.title('Salario por Pessoa')
plt.ylabel('Salario (R$)')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.plot(df['Nome'], df['Idade'], marker='o')
plt.title('Idade por Pessoa')
plt.ylabel('Idade')
plt.xticks(rotation=45)

plt.tight_layout()
# plt.show()  # Descomente para visualizar
plt.savefig('exemplo_grafico.png')

print("\nGrafico salvo como 'exemplo_grafico.png'")
print("\nFim do script de primeiros passos!")
