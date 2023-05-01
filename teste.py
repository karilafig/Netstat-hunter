import re
import subprocess
# Roda o netstat e filtra apenas os IPs
output = subprocess.check_output(['netstat', '-n'])
ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', str(output))


    # Filtra os IPs que não sejam IPs internos
non_internal_ips = []
for ip in ips:
    if not ip.startswith('10.') and not ip.startswith('172.') and not ip.startswith('192.168') and not ip.startswith('127.0.0.1'):
            non_internal_ips.append(ip)

print(non_internal_ips)