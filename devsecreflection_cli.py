import os
import google.generativeai as genai
from InquirerPy import inquirer
from rich import print

# Segurança: exige variável de ambiente com a API Key
def config_gemini(api_key: str):
    genai.configure(api_key=api_key)

def select_available_model():
    preferred_models = [
        "models/gemini-1.5-flash-latest",
        "models/gemini-1.5-pro-latest",
        "models/gemini-pro"
    ]
    try:
        print("🔎 Verificando modelos disponíveis na sua API Key...")
        available_models = [
            m.name for m in genai.list_models()
            if "generateContent" in m.supported_generation_methods
        ]
        if not available_models:
            print("❌ Nenhum modelo com suporte a 'generateContent' foi encontrado para sua API Key.")
            return None
        for model_name in preferred_models:
            if model_name in available_models:
                print(f"✅ Modelo selecionado (otimizado para Free Tier): {model_name}")
                return model_name
        fallback_model = available_models[0]
        print(f"⚠️ Usando fallback: {fallback_model}")
        return fallback_model
    except Exception as e:
        print(f"❌ Erro ao listar modelos: {e}")
        return None

def build_prompt(context):
    return f"""
Você é um assistente de segurança que analisa decisões de desenvolvimento com foco em segurança, privacidade e boas práticas.

Com base nas respostas abaixo, forneça dicas claras e práticas de segurança para o desenvolvedor revisar com seu time e PO:

- O que está sendo desenvolvido: {context['tipo']}
- Objetivo: {context['objetivo']}
- Público-alvo: {context['usuario']}
- Envolve IA? {context['usa_ia']}
- Riscos identificados: {", ".join(context['riscos']) if context['riscos'] else "Nenhum"}

Liste recomendações em tópicos, separando por:

1. Validações importantes
2. Controles de segurança recomendados
3. Alertas sobre uso de IA (se aplicável)
4. Pontos para validação com o PO
"""

def generate_analysis(context, api_key):
    config_gemini(api_key)
    model_name = select_available_model()
    if not model_name:
        return "❌ Não foi possível selecionar um modelo válido."
    model = genai.GenerativeModel(model_name)
    prompt = build_prompt(context)
    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    print("
" + "="*43)
    print("🧠 Bem-vindo ao DevSecReflection (CLI Seguro)")
    print("-------------------------------------------")
    print("Auxílio ao dev com segurança em primeiro lugar.")
    print("Entradas são todas por menus guiados.")
    print("="*43 + "
")

    context = {
        "tipo": inquirer.select(
            message="🧱 O que você vai desenvolver?",
            choices=["API", "Integração com IA", "Front-end", "Backend", "Banco de Dados", "Autenticação", "Outros"]
        ).execute(),
        "objetivo": inquirer.select(
            message="🎯 Qual é o objetivo principal?",
            choices=["Nova funcionalidade", "Correção", "Melhoria", "Refatoração", "Prototipação"]
        ).execute(),
        "usuario": inquirer.select(
            message="👥 Quem vai usar essa funcionalidade?",
            choices=["Usuário final", "Admin", "Serviço interno", "API externa", "Outros"]
        ).execute(),
        "usa_ia": inquirer.select(
            message="🤖 Essa entrega envolve uso de IA?",
            choices=["Yes", "No"]
        ).execute(),
        "riscos": inquirer.checkbox(
            message="🛡️ Quais riscos de segurança você enxerga?",
            choices=["Exposição de dados", "Injeção", "Acesso indevido", "Disponibilidade", "Nenhum identificado"]
        ).execute()
    }

    api_key = inquirer.secret(message="🔐 Cole aqui sua Gemini API Key").execute()

    print("⏳ Gerando análise com base nas respostas...")
    result = generate_analysis(context, api_key)

    print("
" + "="*40)
    print("📌 Resultado da Análise:")
    print("="*40)
    print(result)

if __name__ == "__main__":
    main()