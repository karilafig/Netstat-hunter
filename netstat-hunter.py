import argparse
import time
import requests
import re
import subprocess

print("     __     _       _        _     _                 _            ")
print("  /\ \ \___| |_ ___| |_ __ _| |_  | |__  _   _ _ __ | |_ ___ _ __ ")
print(" /  \/ / _ \ __/ __| __/ _` | __| | '_ \| | | | '_ \| __/ _ \ '__|")
print("/ /\  /  __/ |_\__ \ || (_| | |_  | | | | |_| | | | | ||  __/ |   ")
print("\_\ \/ \___|\__|___/\__\__,_|\__| |_| |_|\__,_|_| |_|\__\___|_|   ")

api_key = '' # Variável global

def config(ip):
    global api_key # Avisa que a variável será usada no escopo global
    # Lógica para configurar a API aqui
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    params = {'apikey': api_key, 'ip': ip}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(response.json())
    elif response.status_code == 403:
        print('Acesso negado: verifique a chave de API')
    else:
        print('Erro ao fazer a consulta de IP')
    
    time.sleep(15) # Atraso de 15 segundos entre cada chamada
def execute():
    non_internal_ips = netstat()
    for ip in non_internal_ips:
        config(ip)
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
parser.add_argument('--config', dest='api_key', help='Chave da API para configuração')
parser.add_argument('--execute', action='store_true', help='Executa')

# Analisa os argumentos de linha de comando
args = parser.parse_args()

# Define o valor da variável global 'api_key'
if args.api_key:
    api_key = args.api_key

# Chama a função correspondente ao argumento de linha de linha de comando
if args.execute:
    execute()
elif args.api_key:
    print("É necessário utilizar a opção --execute para executar a busca de IPs.")

