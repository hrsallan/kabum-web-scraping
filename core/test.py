import requests, json
from pprint import pprint

"""
Este módulo é responsável por testar a conexão com a API do Kabum.
Ele realiza uma requisição de teste e salva a resposta em um arquivo JSON.
"""

def test_hardware():
    """
    Testa a endpoint de hardware da API do Kabum.
    Faz uma requisição GET, imprime o primeiro item da resposta e salva todo o conteúdo
    em 'response.json'.
    """
    # URL da API para buscar produtos de hardware
    url = f"https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products-by-category/hardware?page_number=1&page_size=100&facet_filters=&sort=most_searched&is_prime=false&payload_data=products_category_filters&include=gift"

    try:
        # Faz a requisição GET
        response = requests.get(url)
        # Levanta exceção se o status code não for 200
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(
            f"Erro ao fazer a requisição: url{url}, status_code: {response.status_code}"
        )
        raise err
    
    # Imprime o primeiro produto retornado para verificação rápida
    pprint(response.json()['data'][0])
    
    # Salva a resposta completa em um arquivo JSON para inspeção detalhada
    with open("response.json", "w", encoding='utf-8') as f:
        json.dump(response.json(), f, indent=4, ensure_ascii=False)
        
if __name__ == "__main__":
    test_hardware()
