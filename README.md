# 🛒 Kabum Web Scraping

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Ativo-success?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-Proprietária-red?style=for-the-badge)

**Web scraper profissional para coleta de dados de produtos de hardware do Kabum**

[Funcionalidades](#-funcionalidades) •
[Instalação](#-instalação) •
[Uso](#-uso) •
[Estrutura](#-estrutura-do-projeto) •
[Créditos](#-créditos)

</div>

---

## 📋 Sobre o Projeto

Este projeto é um **web scraper** desenvolvido em Python para extrair informações de produtos de hardware do site [Kabum](https://www.kabum.com.br). Utiliza a API pública do Kabum para coletar dados de forma eficiente e organizada, exportando os resultados para uma planilha Excel.

### O que este scraper coleta?

- 🔢 **ID do Produto**
- 📦 **Nome/Título**
- 💰 **Preço Original**
- 🏷️ **Preço com Desconto**
- 📊 **Quantidade Disponível**
- ⭐ **Avaliação (Score)**
- 📝 **Número de Avaliações**
- 🖼️ **URL da Imagem**
- 🛡️ **Garantia**
- 🔗 **URL do Produto**

---

## ✨ Funcionalidades

- ⚡ **Execução Paralela**: Utiliza `ThreadPoolExecutor` para requisições simultâneas
- 🔄 **Sistema de Retry**: Tentativas automáticas em caso de falha nas requisições
- 📊 **Exportação Excel**: Gera planilhas organizadas com todos os dados
- 🛡️ **Tratamento de Erros**: Robusto sistema de tratamento de exceções
- 🔗 **URLs Amigáveis**: Geração automática de slugs para URLs dos produtos
- ⏱️ **Timeout Configurável**: Controle sobre tempo de espera das requisições

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório**
```bash
git clone https://github.com/hrsallan/kabum-web-scraping.git
cd kabum-web-scraping
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install requests openpyxl
```

---

## 💻 Uso

### Execução Básica

```bash
python main.py
```

### O que acontece ao executar?

1. 📡 O scraper conecta à API do Kabum
2. 📄 Identifica o número total de páginas
3. ⚡ Faz requisições paralelas para todas as páginas
4. 🔄 Processa e normaliza os dados dos produtos
5. 📊 Exporta tudo para `hardware_products.xlsx`

### Exemplo de Saída

```
✅ Página 1/50 ok. +100 produtos.
✅ Página 2/50 ok. +100 produtos.
✅ Página 3/50 ok. +100 produtos.
...
total time para as reqs -> 0:00:15.234567
quantidade de produtos = 5000
percorrendo produtos

https://www.kabum.com.br/produto/123456/placa-de-video-...
https://www.kabum.com.br/produto/789012/processador-amd-...
...
Arquivo Excel salvo como 'hardware_products.xlsx'
```

---

## 📁 Estrutura do Projeto

```
kabum-web-scraping/
│
├── main.py                    # Script principal
├── utils/
│   └── utils.py               # Funções utilitárias
├── hardware_products.xlsx     # Arquivo de saída (gerado)
├── response.json              # Exemplo de resposta da API
├── LICENSE                    # Licença do projeto
├── README.md                  # Este arquivo
└── .gitignore                 # Arquivos ignorados pelo Git
```

---

## ⚙️ Configuração

### Parâmetros Customizáveis

No arquivo `main.py`, você pode ajustar:

```python
BASE_URL = "https://servicespub.prod.api.aws.grupokabum.com.br/catalog/v2/products-by-category/hardware"
DEFAULT_TIMEOUT = 20      # Tempo máximo de espera (segundos)
MAX_RETRIES = 3           # Número de tentativas em caso de falha
```

### ThreadPoolExecutor

```python
with ThreadPoolExecutor(max_workers=5) as executor:  # Ajuste o número de workers
```

---

## 📊 Estrutura do Excel Gerado

| Coluna | Descrição |
|--------|-----------|
| ID | Identificador único do produto |
| Name | Nome completo do produto |
| Price | Preço original (R$) |
| Price with Discount | Preço com desconto (R$) |
| Quantity Available | Estoque disponível |
| Score of Ratings | Média das avaliações |
| Number of Ratings | Total de avaliações |
| Photos (g) | URL da imagem grande |
| Warranty | Informações de garantia |
| URL | Link direto para o produto |

---

## ⚠️ Aviso Legal

Este projeto é destinado **apenas para fins educacionais e de estudo**. O uso de web scraping pode violar os Termos de Serviço de alguns sites. Certifique-se de:

- ✅ Respeitar o `robots.txt` do site alvo
- ✅ Não sobrecarregar os servidores com requisições excessivas
- ✅ Usar os dados de forma ética e legal
- ✅ Verificar os Termos de Serviço do site

---

## 🏆 Créditos

<div align="center">

### Código Original

Este projeto foi desenvolvido com base no trabalho de:

[![GitHub](https://img.shields.io/badge/@pedrohcleal-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pedrohcleal)

**[kabum-api-scraper](https://github.com/pedrohcleal/kabum-api-scraper)**

Agradecimentos especiais por disponibilizar o código inicial que serviu de inspiração e base para este projeto.

</div>

---

## 📄 Licença

⚠️ **ATENÇÃO**: Este projeto está sob uma **Licença Proprietária Exclusiva**.

O uso, cópia, modificação ou distribuição deste software sem autorização prévia e expressa é **estritamente proibido** e sujeito a **ações legais**.

Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autores

<div align="center">

| [![hrsallan](https://github.com/hrsallan.png?size=100)](https://github.com/hrsallan) | [![nicolaszbq](https://github.com/nicolaszbq.png?size=100)](https://github.com/nicolaszbq) | [![gustavoobezerra](https://github.com/gustavoobezerra.png?size=100)](https://github.com/gustavoobezerra) |
|:---:|:---:|:---:|
| **[@hrsallan](https://github.com/hrsallan)** | **[@nicolaszbq](https://github.com/nicolaszbq)** | **[@gustavoobezerra](https://github.com/gustavoobezerra)** |

</div>

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

</div>