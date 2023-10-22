import pandas as pd;

df_original = pd.read_csv(r'C:\Users\adm\Documents\bootcamp_dio\DesafioETL\desafio_etl\licitacoes.csv', sep=';', header=0,encoding='latin-1');

df_manipulado = df_original.drop(columns=["Código Modalidade Compra","Modalidade Compra","Número Processo","Objeto","Situação Licitação","Código Órgão Superior","Nome Órgão Superior","Código Órgão","Nome Órgão","Município","Data Resultado Compra","Data Abertura","data_arquivo","UF"]);

df_manipulado["Valor Licitação"] = df_manipulado["Valor Licitação"].str.replace(",", ".").astype(float);
df_manipulado = df_manipulado.groupby(["Número Licitação","Código UG"])["Valor Licitação"].agg('sum');
df_manipulado.to_csv(r'C:\Users\adm\Documents\bootcamp_dio\DesafioETL\desafio_etl\resultado_desafio_etl.csv', sep=';', header=1,encoding='latin-1');
