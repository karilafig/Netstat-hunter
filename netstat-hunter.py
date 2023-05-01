import argparse

print("     __     _       _        _     _                 _            ")
print("  /\ \ \___| |_ ___| |_ __ _| |_  | |__  _   _ _ __ | |_ ___ _ __ ")
print(" /  \/ / _ \ __/ __| __/ _` | __| | '_ \| | | | '_ \| __/ _ \ '__|")
print("/ /\  /  __/ |_\__ \ || (_| | |_  | | | | |_| | | | | ||  __/ |   ")
print("\_\ \/ \___|\__|___/\__\__,_|\__| |_| |_|\__,_|_| |_|\__\___|_|   ")

def config():
    # Lógica para configurar a API aqui
    print("Configurar API selecionada")

def portas():
    # Lógica para configurar as portas aqui
    print("Configurar Portas selecionado")

def execute():
    # Lógica para executar aqui
    print("Executar selecionado")

# Define os argumentos de linha de comando
parser = argparse.ArgumentParser(description='Menu - Netstat Hunter')
parser.add_argument('--config', action='store_true', help='Configura a API')
parser.add_argument('--portas', action='store_true', help='Configura as portas')
parser.add_argument('--execute', action='store_true', help='Executa')

# Analisa os argumentos de linha de comando
args = parser.parse_args()

# Chama a função correspondente ao argumento de linha de comando
if args.config:
    config()
elif args.portas:
    portas()
elif args.execute:
    execute()
else:
    parser.print_help()
