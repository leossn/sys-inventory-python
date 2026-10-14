import platform
import psutil
import subprocess
from datetime import datetime

def get_cpu_model():
    """Busca o modelo exato do processador no Windows via WMIC/PowerShell."""
    try:
        cmd = "Get-CimInstance -ClassName Win32_Processor | Select-Object -ExpandProperty Name"
        output = subprocess.check_output(["powershell", "-Command", cmd], text=True).strip()
        if output:
            return output
    except Exception:
        pass
    return platform.processor() or "N/A"

def collect_system_info():
    """Coleta informações detalhadas de hardware e sistema operacional."""
    try:
        uname = platform.uname()
        cpu_model = get_cpu_model()
        cpu_count = psutil.cpu_count(logical=True)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        data = {
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "hostname": uname.node,
            "os_system": f"{uname.system} {uname.release}",
            "processor_model": cpu_model,
            "cpu_cores_logical": cpu_count,
            "total_ram_gb": round(memory.total / (1024**3), 2),
            "ram_usage_percent": memory.percent,
            "disk_total_gb": round(disk.total / (1024**3), 2),
            "disk_free_gb": round(disk.free / (1024**3), 2)
        }
        return data
    except Exception as e:
        print(f"[ERRO] Falha ao coletar métricas do sistema: {e}")
        return None

def export_to_notepad(data, filename="relatorio_inventario.txt"):
    """Gera um relatório formatado e estruturado para Bloco de Notas (.txt)."""
    if not data:
        return

    content = f"""===================================================================
                  RELATÓRIO DE INVENTÁRIO DE HARDWARE
===================================================================
 Data/Hora da Coleta : {data['timestamp']}
 Nome da Máquina     : {data['hostname']}
 Sistema Operacional : {data['os_system']}
-------------------------------------------------------------------

 [ PROCESSADOR ]
   Modelo            : {data['processor_model']}
   Núcleos Lógicos   : {data['cpu_cores_logical']}

 [ MEMÓRIA RAM ]
   Capacidade Total  : {data['total_ram_gb']} GB
   Uso Atual         : {data['ram_usage_percent']}%

 [ ARMAZENAMENTO (DISCO C:) ]
   Capacidade Total  : {data['disk_total_gb']} GB
   Espaço Livre      : {data['disk_free_gb']} GB

===================================================================
                 STATUS: COLETA CONCLUÍDA COM SUCESSO
===================================================================
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[SUCESSO] Relatório formatado exportado para '{filename}'!")

if __name__ == "__main__":
    print("Iniciando coleta detalhada de dados de inventario...")
    system_data = collect_system_info()
    if system_data:
        export_to_notepad(system_data)