<div align="center">

# 🖥️ System Hardware Inventory Script

  <p>
    <b>Automação leve e eficiente em Python para coleta de dados de hardware e geração de relatórios de inventário de TI.</b>
  </p>

  <!-- Badges -->
  <p>
    <img src="https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/OS-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows" />
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge" alt="Status" />
  </p>

</div>

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para resolver gargalos operacionais no levantamento de ativos de TI e auditorias de hardware. O script automatiza a extração de métricas do sistema e gera um relatório estruturado em formato de texto (`.txt`), ideal para leitura rápida no Bloco de Notas ou anexos de chamados.

### ⚡ Principais Funcionalidades
* **Identificação precisa de Hardware:** Coleta o modelo exato do processador (via PowerShell/WMIC), quantidade de núcleos lógicos, memória RAM total e uso percentual.
* **Mapeamento de Armazenamento:** Identifica a capacidade total do disco principal (`C:`) e o espaço livre disponível.
* **Relatório Formatado:** Gera automaticamente um arquivo `.txt` com cabeçalho, seções limpas e divisores visuais organizados.

---

## 💻 Exemplo de Saída do Relatório (`.txt`)

```text
===================================================================
                  RELATÓRIO DE INVENTÁRIO DE HARDWARE
===================================================================
 Data/Hora da Coleta : 14/10/2026 19:26:32
 Nome da Máquina     : DESKTOP-7DCQL8J
 Sistema Operacional : Windows 10
-------------------------------------------------------------------

 [ PROCESSADOR ]
   Modelo            : 12th Gen Intel(R) Core(TM) i3-12100F
   Núcleos Lógicos   : 8

 [ MEMÓRIA RAM ]
   Capacidade Total  : 15.86 GB
   Uso Atual         : 84.7%

 [ ARMAZENAMENTO (DISCO C:) ]
   Capacidade Total  : 476.83 GB
   Espaço Livre      : 199.52 GB

===================================================================
                 STATUS: COLETA CONCLUÍDA COM SUCESSO
===================================================================
