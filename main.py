import requests
from openpyxl import Workbook
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from utils.utils import normalize_title_to_link
from time import sleep


BASE_URL = "https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products-by-category/hardware"
DEFAULT_TIMEOUT = 20 
MAX_RETRIES = 3


def safe_get(dct, path, default=None):
    cur = dct
    for key in path:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(key)
        if cur is None:
            return default
    return cur


def get_json_with_retries(url: str, retries: int = MAX_RETRIES, timeout: int = DEFAULT_TIMEOUT):
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as exc:
            last_exc = exc
            sleep(attempt)
    raise last_exc


def fetch_hardware(page: int):
    url = (
        f"{BASE_URL}"
        f"?page_number={page}&page_size=100&facet_filters=&sort=most_searched"
        f"&is_prime=false&payload_data=products_category_filters&include=gift"
    )

    try:
        payload = get_json_with_retries(url)
    except Exception as err:
        print(f"❌ Falha ao buscar página {page}. url={url}. erro={err}")
        return []  # NÃO quebra o pipeline inteiro

    data = payload.get("data", [])
    if not isinstance(data, list):
        print(f"⚠️ Resposta inesperada na página {page}: 'data' não é lista.")
        return []

    products = []
    for x in data:
        try:
            attrs = x.get("attributes", {}) if isinstance(x, dict) else {}
            pid = x.get("id") if isinstance(x, dict) else None

            title = attrs.get("title") or "SEM_TITULO"
            offer = attrs.get("offer") if isinstance(attrs.get("offer"), dict) else {}
            photos_g = safe_get(attrs, ["photos", "g"], default=None)

            price = attrs.get("price")
            price_with_discount = attrs.get("price_with_discount")
            warranty = attrs.get("warranty")
            score_of_ratings = attrs.get("score_of_ratings")
            number_of_ratings = attrs.get("number_of_ratings")

            quantity_available = offer.get("quantity_available", 0)

            if pid is not None:
                slug = normalize_title_to_link(title)
                product_url = f"https://www.kabum.com.br/produto/{pid}/{slug}"
            else:
                product_url = None

            products.append(
                {
                    "id": pid,
                    "name": title,
                    "price": price,
                    "price_with_discount": price_with_discount,
                    "quantity_available": quantity_available,
                    "score_of_ratings": score_of_ratings,
                    "number_of_ratings": number_of_ratings,
                    "photos-g": str(photos_g) if photos_g is not None else None,
                    "warranty": warranty,
                    "url": product_url,
                }
            )
        except Exception as err:
            print(f"⚠️ Erro ao processar produto da página {page}. Pulando. erro={err}")
            continue

    return products


def hardware_data(category: str):
    url = (
        f"{BASE_URL}"
        f"?page_number=1&page_size=100&facet_filters=&sort=most_searched"
        f"&is_prime=false&payload_data=products_category_filters&include=gift"
    )

    try:
        payload = get_json_with_retries(url)
        total_pages = safe_get(payload, ["meta", "total_pages_count"], default=1)
        if not isinstance(total_pages, int) or total_pages < 1:
            total_pages = 1
    except Exception as err:
        print(f"❌ Não foi possível obter total_pages. erro={err}")
        return []

    total_products = []
    start = datetime.now()

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(fetch_hardware, page): page for page in range(1, total_pages + 1)}

        for future in as_completed(futures):
            page = futures[future]
            try:
                page_products = future.result()
                total_products.extend(page_products)
                print(f"✅ Página {page}/{total_pages} ok. +{len(page_products)} produtos.")
            except Exception as err:
                print(f"❌ Página {page}/{total_pages} falhou no future.result(). erro={err}")

    print(f"total time para as reqs -> {datetime.now() - start}")
    return total_products


def to_excel(data, file_name):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Hardware Products"

    headers = [
        "ID",
        "Name",
        "Price",
        "Price with Discount",
        "Quantity Available",
        "Score of Ratings",
        "Number of Ratings",
        "Photos (g)",
        "Warranty",
        "URL",
    ]
    sheet.append(headers)

    for item in data:
        row = [
            item.get("id"),
            item.get("name"),
            item.get("price"),
            item.get("price_with_discount"),
            item.get("quantity_available"),
            item.get("score_of_ratings"),
            item.get("number_of_ratings"),
            item.get("photos-g"),
            item.get("warranty"),
            item.get("url"),
        ]
        sheet.append(row)

    workbook.save(file_name)
    print(f"Arquivo Excel salvo como '{file_name}'")


def main():
    hardware_inicial_data = hardware_data("hardware")
    print(f"quantidade de produtos = {len(hardware_inicial_data)}")
    print("percorrendo produtos\n")
    sleep(2)

    for i in hardware_inicial_data:
        sleep(0.05)
        print(i.get("url"))

    to_excel(hardware_inicial_data, file_name="hardware_products.xlsx")


if __name__ == "__main__":
    main()
