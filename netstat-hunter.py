import argparse

print("     __     _       _        _     _                 _            ")
print("  /\ \ \___| |_ ___| |_ __ _| |_  | |__  _   _ _ __ | |_ ___ _ __ ")
print(" /  \/ / _ \ __/ __| __/ _` | __| | '_ \| | | | '_ \| __/ _ \ '__|")
print("/ /\  /  __/ |_\__ \ || (_| | |_  | | | | |_| | | | | ||  __/ |   ")
print("\_\ \/ \___|\__|___/\__\__,_|\__| |_| |_|\__,_|_| |_|\__\___|_|   ")

def config(api_key):
    # Lógica para configurar a API aqui
    print("Configurar API selecionada")

def execute():
    netstat()
    print("Executar selecionado")

def netstat():
    # Função para rodar o netstat e retornar a outra função x os IPs para que seja feita a chamada da API
    pass

# Define os argumentos de linha de comando
parser = argparse.ArgumentParser(description='Menu - Netstat Hunter')
parser.add_argument('--config', dest='api_key', help='Chave da API para configuração')
parser.add_argument('--execute', action='store_true', help='Executa')

# Analisa os argumentos de linha de comando
args = parser.parse_args()

# Chama a função correspondente ao argumento de linha de linha de comando
if args.api_key:
    config(args.api_key)
elif args.execute:
    execute()
else:
    parser.print_help()
