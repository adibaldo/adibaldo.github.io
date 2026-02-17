#!/usr/bin/env python3
import sys
import os
from pathlib import Path

def create_agent_structure(agent_name, workspace_path):
    base_path = Path(workspace_path) / "jules-agents" / agent_name
    logs_path = base_path / "logs"
    
    if base_path.exists():
        print(f"Erro: O agente '{agent_name}' já existe em {base_path}")
        return False
        
    os.makedirs(logs_path, exist_ok=True)
    
    # Criar arquivos básicos
    with open(base_path / "SOUL.md", "w") as f:
        f.write(f"# 🤖 Alma do Agente {agent_name.capitalize()}\n\n[TODO: Definir Identidade, Protocolo e Templates conforme o Framework]\n")
        
    with open(logs_path / "EXPERIENCE.md", "w") as f:
        f.write(f"# 📓 Diário de Experiência - {agent_name.capitalize()}\n\nEste arquivo registra o que o agente aprendeu sobre o código e a estrutura do blog.\n")
        
    print(f"Estrutura criada com sucesso para '{agent_name}' em {base_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 scripts/init_jules.py <nome-do-agente> <caminho-do-workspace>")
        sys.exit(1)
        
    name = sys.argv[1].lower()
    ws = sys.argv[2]
    create_agent_structure(name, ws)
