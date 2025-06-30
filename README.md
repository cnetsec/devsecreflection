# 🧠 DevSecReflection (CLI Seguro) -

DISCLAIMER :  Lembrando que é o Cenário Hipotético(Não Homologado) Recomendado não utilizar em produção.

**DevSecReflection** é uma ferramenta para desenvolvedores refletirem sobre segurança ao implementar novas funcionalidades. Ela faz perguntas guiadas e gera uma análise com base nas respostas, usando a API do Gemini da Google.

Totalmente seguro: sem entradas livres de texto — apenas opções fechadas.

---

## 🚀 Instalação Rápida

### ✅ Pré-requisitos

- [Python 3.9+](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- Conta e [API Key do Google Gemini](https://aistudio.google.com/app/apikey)

---

## 🛠️ Passo a passo (1ª vez)

1. Extraia o `.zip` em uma pasta
2. Abra essa pasta no **VS Code**
3. No terminal do VS Code, execute:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

Isso irá:
- Criar um ambiente virtual `venv`
- Instalar as dependências em `requirements.txt`

---

## ▶️ Como rodar

### ✅ Rodar a qualquer momento:

Pressione `Ctrl + Shift + B` no VS Code  
(Ou `F1 > Run Task > 🧠 Run DevSecReflection`)

Você verá:

```
🧠 Bem-vindo ao DevSecReflection (CLI Seguro)
```
![image](https://github.com/user-attachments/assets/bec7f959-cfce-4f20-98df-5973aa6288d4)

---

## ⚙️ Criando a pasta `.vscode/` com execução automática

Caso a pasta `.vscode/` ainda não exista no seu projeto, você pode criá-la manualmente e adicionar o arquivo `tasks.json` com a configuração abaixo:

### 📁 Passos:

1. Na raiz do projeto, crie a pasta `.vscode`
2. Dentro dela, crie o arquivo `tasks.json`
3. Cole o conteúdo abaixo:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "🧠 Run DevSecReflection",
      "type": "shell",
      "command": "${workspaceFolder}\venv\Scripts\python.exe",
      "args": [
        "${workspaceFolder}\devsecreflection_cli.py"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": true,
        "panel": "dedicated",
        "clear": true
      },
      "problemMatcher": []
    }
  ]
}
```

---

## 🔐 Segurança

- Todas as perguntas usam menus fechados
- Sua API Key do Gemini nunca é armazenada
- Caso forneça seu token do GitHub, a ferramenta cria uma **issue automaticamente** com a análise gerada (opcional)

---

## 📂 Estrutura do Projeto

```
devreflection_package/
│
├── devsecreflection_cli.py     # Script principal
├── requirements.txt
├── README.md
├── setup.ps1                   # Script de setup no Windows
├── .gitignore
└── .vscode/
    └── tasks.json              # Atalho para execução via VS Code
```

---

## 💬 Sugestões?

Contribuições são bem-vindas. Você pode abrir uma **issue** com sugestões de melhoria ou ajustes!
