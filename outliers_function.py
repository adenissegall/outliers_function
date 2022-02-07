import pandas as pd

def outliers(dados):
    q3 = dados.quantile(0.75)
    q1 = dados.quantile(0.25)
    fiq = q3 - q1
    deadline = q3 + (1.5 * fiq)
    
    acima = []
    
    for i in dados:
        if i > deadline:
            acima.append(i)
    
    qtd_acima = len(acima)
    pct_acima = (qtd_acima / len(dados))*100
    qtd_acima_max = max(acima)
    
    print('O valor para ser considerado outlier nessa variável é {} e existem {} ocorrências que estão acima desse valor.'\
      .format(deadline, qtd_acima))
    print(' ')
    print('Os outliers nessa variável representam {:.2f}% do total dos valores presentes.'.format(pct_acima))
    print(' ')
    print('O valor máximo encontrado no conjunto de dados é {:.2f}.'.format(qtd_acima_max))
    print(' ')
    print('Amostra dos 8 maiores valores presentes nessa variável:')
    print(dados.sort_values(ascending=False).values[:8])
