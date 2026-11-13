"""Exploração dos metadados das tabelas 7060 (IPCA) e 5436 (renda) do IBGE."""

import truststore

truststore.inject_into_ssl()  # precisa vir antes do import do requests

import requests  # noqa: E402

BASE = "https://servicodados.ibge.gov.br/api/v3/agregados"
SIDRA = "https://apisidra.ibge.gov.br/values"


def buscar_json(url: str) -> dict | list:
    resposta = requests.get(url,timeout=30)
    resposta.raise_for_status()
    return resposta.json()



def trimestres_esperados(inicio: int, fim: int) -> list[str]:
    """Gera os códigos AAAATT entre inicio e fim. Ex.: 201201, 201202..."""
    # TODO 3a


def main() -> None:
    meta_ipca = buscar_json(f"{BASE}/7060/metadados")
    meta_renda = buscar_json(f"{BASE}/5436/metadados")


#    print("== 1. Níveis territoriais ==")
    # TODO 2: imprima os níveis das duas tabelas
    print(meta_ipca["nivelTerritorial"])
    print(meta_renda["nivelTerritorial"])
 #meta ipca com 3 níveis e meta renda com 7 níveis
 

 #   print("== 2. Índice geral + 9 grupos ==")
    # TODO 4: filtre as categorias da classificação 315

  #  print("== 3. Lacuna da renda ==")
    # TODO 3b: compare os trimestres esperados com os de /periodos

  #  print("== 4. Revisões ==")
    # TODO 5: conte as datas de 'modificacao' distintas em cada tabela

  #  print("== 5. Áreas com dados ==")
    # TODO 6: liste as áreas N7 das duas tabelas pela API SIDRA


if __name__ == "__main__":
    main()