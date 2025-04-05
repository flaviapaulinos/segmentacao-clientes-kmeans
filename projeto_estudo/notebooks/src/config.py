from pathlib import Path
PASTA_PROJETO = Path(__file__).resolve().parents[2]
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"

PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
PASTA_MODELOS = PASTA_PROJETO / "modelos"


DADOS_ORIGINAIS = PASTA_DADOS / "Mall_Customers.csv"
DADOS_LIMPOS = PASTA_DADOS / "Mall_Customers-clean.parquet"
DADOS_SCALED = PASTA_DADOS / "Mall_Customers-scaled.parquet"
DADOS_CLUSTERED = PASTA_DADOS /  "Mall_Customers-clustered.parquet"
DADOS_PCA_SCALED = PASTA_DADOS /  "Mall_Customers-pca.parquet"

RELATORIO = PASTA_RELATORIOS / "00-fbps-eda.html"
MODELO = PASTA_MODELOS / "modelo_clustering.pkl"
MODELO_PCA = PASTA_MODELOS / "modelo_pca_clustering.pkl"





