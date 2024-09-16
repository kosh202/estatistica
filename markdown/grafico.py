# # # # import numpy as np
# # # # import matplotlib.pyplot as plt
# # # # from scipy.stats import pearsonr

# # # # # Dados
# # # # quantidade_vendida = np.array([166, 180, 73, 81, 229, 182, 233, 102, 190, 150, 215, 137, 173, 150, 92, 200, 102, 190, 156, 218, 137, 173, 150])
# # # # preco = np.array([14, 12, 22, 20, 8, 11, 6, 18, 7, 14, 9, 15, 11, 15, 22, 9, 20, 9, 13, 8, 15, 8, 12])
# # # # lucro = np.array([20, 21, 12, 16, 24, 24, 23, 15, 20, 19, 25, 21, 19, 20, 14, 22, 18, 19, 25, 21, 19, 20, 17])

# # # # # Função para calcular covariância
# # # # def cov(x, y):
# # # #     return np.mean((x - np.mean(x)) * (y - np.mean(y)))

# # # # # Função para calcular o coeficiente de Pearson
# # # # def pearson_corr(x, y):
# # # #     return pearsonr(x, y)[0]

# # # # # Gráfico de dispersão: Quantidade Vendida vs. Preço
# # # # plt.figure(figsize=(12, 8))

# # # # plt.subplot(3, 1, 1)
# # # # plt.scatter(quantidade_vendida, preco, color='blue')
# # # # plt.title('Quantidade Vendida vs. Preço')
# # # # plt.xlabel('Quantidade Vendida')
# # # # plt.ylabel('Preço')

# # # # # Gráfico de dispersão: Quantidade Vendida vs. Lucro
# # # # plt.subplot(3, 1, 2)
# # # # plt.scatter(quantidade_vendida, lucro, color='green')
# # # # plt.title('Quantidade Vendida vs. Lucro')
# # # # plt.xlabel('Quantidade Vendida')
# # # # plt.ylabel('Lucro')

# # # # # Gráfico de dispersão: Preço vs. Lucro
# # # # plt.subplot(3, 1, 3)
# # # # plt.scatter(preco, lucro, color='red')
# # # # plt.title('Preço vs. Lucro')
# # # # plt.xlabel('Preço')
# # # # plt.ylabel('Lucro')

# # # # plt.tight_layout()
# # # # plt.show()

# # # # # Cálculo da covariância e coeficiente de Pearson
# # # # cov_qv_preco = cov(quantidade_vendida, preco)
# # # # cov_qv_lucro = cov(quantidade_vendida, lucro)
# # # # cov_preco_lucro = cov(preco, lucro)

# # # # pearson_qv_preco = pearson_corr(quantidade_vendida, preco)
# # # # pearson_qv_lucro = pearson_corr(quantidade_vendida, lucro)
# # # # pearson_preco_lucro = pearson_corr(preco, lucro)

# # # # print(f'Covariância (Quantidade Vendida vs. Preço): {cov_qv_preco}')
# # # # print(f'Covariância (Quantidade Vendida vs. Lucro): {cov_qv_lucro}')
# # # # print(f'Covariância (Preço vs. Lucro): {cov_preco_lucro}')

# # # # print(f'Coeficiente de Pearson (Quantidade Vendida vs. Preço): {pearson_qv_preco}')
# # # # print(f'Coeficiente de Pearson (Quantidade Vendida vs. Lucro): {pearson_qv_lucro}')
# # # # print(f'Coeficiente de Pearson (Preço vs. Lucro): {pearson_preco_lucro}')

# # # import numpy as np
# # # import matplotlib.pyplot as plt
# # # from scipy.stats import linregress

# # # # Dados
# # # quantidade_vendida = np.array([166, 180, 73, 81, 229, 182, 233, 102, 190, 150, 215, 137, 173, 150, 92, 200, 102, 190, 156, 218, 137, 173, 150])
# # # preco = np.array([14, 12, 22, 20, 8, 11, 6, 18, 7, 14, 9, 15, 11, 15, 22, 9, 20, 9, 13, 8, 15, 8, 12])
# # # lucro = np.array([20, 21, 12, 16, 24, 24, 23, 15, 20, 19, 25, 21, 19, 20, 14, 22, 18, 19, 25, 21, 19, 20, 17])

# # # # Função para calcular e plotar a reta de regressão
# # # def plot_regression(x, y, xlabel, ylabel, title):
# # #     slope, intercept, r_value, p_value, std_err = linregress(x, y)
# # #     plt.figure(figsize=(8, 6))
# # #     plt.scatter(x, y, color='blue', label='Dados')
# # #     plt.plot(x, intercept + slope * x, color='red', label=f'Reta de Regressão: y = {intercept:.2f} + {slope:.2f}x')
# # #     plt.xlabel(xlabel)
# # #     plt.ylabel(ylabel)
# # #     plt.title(title)
# # #     plt.legend()
# # #     plt.show()
# # #     return slope, intercept

# # # # Gráficos de dispersão com retas de regressão
# # # slope_qv_preco, intercept_qv_preco = plot_regression(quantidade_vendida, preco, 'Quantidade Vendida', 'Preço', 'Quantidade Vendida vs. Preço')
# # # slope_qv_lucro, intercept_qv_lucro = plot_regression(quantidade_vendida, lucro, 'Quantidade Vendida', 'Lucro', 'Quantidade Vendida vs. Lucro')
# # # slope_preco_lucro, intercept_preco_lucro = plot_regression(preco, lucro, 'Preço', 'Lucro', 'Preço vs. Lucro')

# # # print(f'Reta de Regressão (Quantidade Vendida vs. Preço): y = {intercept_qv_preco:.2f} + {slope_qv_preco:.2f}x')
# # # print(f'Reta de Regressão (Quantidade Vendida vs. Lucro): y = {intercept_qv_lucro:.2f} + {slope_qv_lucro:.2f}x')
# # # print(f'Reta de Regressão (Preço vs. Lucro): y = {intercept_preco_lucro:.2f} + {slope_preco_lucro:.2f}x')

# # import numpy as np
# # import pandas as pd
# # import statsmodels.api as sm

# # # Dados
# # quantidade_vendida = np.array([166, 180, 73, 81, 229, 182, 233, 102, 190, 150, 215, 137, 173, 150, 92, 200, 102, 190, 156, 218, 137, 173, 150])
# # preco = np.array([14, 12, 22, 20, 8, 11, 6, 18, 7, 14, 9, 15, 11, 15, 22, 9, 20, 9, 13, 8, 15, 8, 12])
# # lucro = np.array([20, 21, 12, 16, 24, 24, 23, 15, 20, 19, 25, 21, 19, 20, 14, 22, 18, 19, 25, 21, 19, 20, 17])

# # # Criação do DataFrame
# # df = pd.DataFrame({
# #     'Quantidade_Vendida': quantidade_vendida,
# #     'Preço': preco,
# #     'Lucro': lucro
# # })

# # # Variáveis independentes
# # X = df[['Quantidade_Vendida', 'Preço']]
# # # Adicionando uma constante para o intercepto
# # X = sm.add_constant(X)

# # # Variável dependente
# # y = df['Lucro']

# # # Ajuste do modelo de regressão múltipla
# # model = sm.OLS(y, X).fit()

# # # Resumo do modelo
# # print(model.summary())

# import numpy as np
# import pandas as pd
# import statsmodels.api as sm

# # Dados
# quantidade_vendida = np.array([166, 180, 73, 81, 229, 182, 233, 102, 190, 150, 215, 137, 173, 150, 92, 200, 102, 190, 156, 218, 137, 173, 150])
# preco = np.array([14, 12, 22, 20, 8, 11, 6, 18, 7, 14, 9, 15, 11, 15, 22, 9, 20, 9, 13, 8, 15, 8, 12])
# lucro = np.array([20, 21, 12, 16, 24, 24, 23, 15, 20, 19, 25, 21, 19, 20, 14, 22, 18, 19, 25, 21, 19, 20, 17])

# # Criação do DataFrame
# df = pd.DataFrame({
#     'Quantidade_Vendida': quantidade_vendida,
#     'Lucro': lucro,
#     'Preço': preco
# })

# # Variáveis independentes
# X = df[['Quantidade_Vendida', 'Lucro']]
# # Adicionando uma constante para o intercepto
# X = sm.add_constant(X)

# # Variável dependente
# y = df['Preço']

# # Ajuste do modelo de regressão múltipla
# model = sm.OLS(y, X).fit()

# # Resumo do modelo
# print(model.summary())


import numpy as np
import pandas as pd
import statsmodels.api as sm

# Dados
quantidade_vendida = np.array([166, 180, 73, 81, 229, 182, 233, 102, 190, 150, 215, 137, 173, 150, 92, 200, 102, 190, 156, 218, 137, 173, 150])
preco = np.array([14, 12, 22, 20, 8, 11, 6, 18, 7, 14, 9, 15, 11, 15, 22, 9, 20, 9, 13, 8, 15, 8, 12])
lucro = np.array([20, 21, 12, 16, 24, 24, 23, 15, 20, 19, 25, 21, 19, 20, 14, 22, 18, 19, 25, 21, 19, 20, 17])

# Criação do DataFrame
df = pd.DataFrame({
    'Quantidade_Vendida': quantidade_vendida,
    'Lucro': lucro,
    'Preço': preco
})

# Variáveis independentes
X = df[['Quantidade_Vendida', 'Lucro']]
# Adicionando uma constante para o intercepto
X = sm.add_constant(X)

# Variável dependente
y = df['Preço']

# Ajuste do modelo de regressão múltipla
model = sm.OLS(y, X).fit()

# Resumo do modelo
print(model.summary())
