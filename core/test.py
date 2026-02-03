import requests, json
from pprint import pprint


def test_hardware():
    url = f"https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products-by-category/hardware?page_number=1&page_size=100&facet_filters=&sort=most_searched&is_prime=false&payload_data=products_category_filters&include=gift"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(
            f"Erro ao fazer a requisição: url{url}, status_code: {response.status_code}"
        )
        raise err
    
    pprint(response.json()['data'][0])
    
    with open("response.json", "w", encoding='utf-8') as f:
        json.dump(response.json(), f, indent=4, ensure_ascii=False)
        
if __name__ == "__main__":
    test_hardware()