import requests
import re
import subprocess
import argparse
import time

print("     __     _       _        _     _                 _            ")
print("  /\ \ \___| |_ ___| |_ __ _| |_  | |__  _   _ _ __ | |_ ___ _ __ ")
print(" /  \/ / _ \ __/ __| __/ _` | __| | '_ \| | | | '_ \| __/ _ \ '__|")
print("/ /\  /  __/ |_\__ \ || (_| | |_  | | | | |_| | | | | ||  __/ |   ")
print("\_\ \/ \___|\__|___/\__\__,_|\__| |_| |_|\__,_|_| |_|\__\___|_|   ")

def config(ip, api_key):
    # Faz a consulta do IP utilizando a API
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    params = {'apikey': api_key, 'ip': ip}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_data = response.json()
        print('----- IP:'+ ip + '----- ')
        print('País:'+ response.json()['country'])
        
        detected_urls = response.json()['detected_urls']
        for url in detected_urls:
            print('URL:', url['url'])
            print('Positives:', url['positives'])
            print('Total:', url['total'])
            print('Scan date:', url['scan_date'])

    elif response.status_code == 403:
        print('Acesso negado: verifique a chave de API')
    else:
        print('Erro ao fazer a consulta de IP')
    
    time.sleep(15) # Atraso de 15 segundos entre cada chamada

def execute(api_key):
    non_internal_ips = netstat()
    for ip in non_internal_ips:
        config(ip, api_key)
    print("Executar selecionado")

def netstat():
    # Roda o netstat e filtra apenas os IPs
    output = subprocess.check_output(['netstat', '-n'])
    ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', str(output))

    # Filtra os IPs que não sejam IPs internos
    non_internal_ips = []
    for ip in ips:
        if not ip.startswith('10.') and not ip.startswith('172.') and not ip.startswith('192.168') and not ip.startswith('127.0.0.1'):
            non_internal_ips.append(ip)

    return non_internal_ips

#--------------------------------------------------
# Define os argumentos de linha de comando
parser = argparse.ArgumentParser(description='Menu - Netstat Hunter')
parser.add_argument('--key', dest='api_key', help='Chave da API para configuração e execução')

# Analisa os argumentos de linha de comando
args = parser.parse_args()

# Chama a função correspondente ao argumento de linha de linha de comando
if args.api_key:
    execute(args.api_key)
else:
    print("É necessário utilizar a opção --key para informar a chave de API.")
