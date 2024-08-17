import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Função para baixar o arquivo PDF
def download_pdf(pdf_url, file_name):
    response = requests.get(pdf_url)
    response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"PDF baixado com sucesso: {file_name}")

# Função principal para encontrar e baixar o PDF
def find_and_download_pdf(url):
    # Enviar uma solicitação GET para o site
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a solicitação foi bem-sucedida

    # Analisar o conteúdo da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos os links de PDF
    pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].lower().endswith('.pdf')]

    if pdf_links:
        # Construir URL completa do PDF
        pdf_url = urljoin(url, pdf_links[0])
        # Nome do arquivo PDF que será salvo localmente
        file_name = pdf_url.split('/')[-1]
        # Baixar o PDF
        download_pdf(pdf_url, file_name)
    else:
        print("Nenhum link PDF encontrado.")

# URL do site que você deseja acessar
site_url = 'https://www.cachoeiro.es.gov.br/procon/pesquisas-de-precos-procon/combustivel/'
find_and_download_pdf(site_url)
