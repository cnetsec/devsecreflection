# setup.ps1 - Script para configurar o ambiente de desenvolvimento automaticamente

Write-Host "=================================================" -ForegroundColor Green
Write-Host "🚀 Iniciando configuração do ambiente DevSecReflection..."
Write-Host "================================================="

$PythonExecutable = "python"

if (-not (Test-Path -Path "venv" -PathType Container)) {
    Write-Host "-> Ambiente virtual (venv) não encontrado. Criando agora..." -ForegroundColor Yellow
    & $PythonExecutable -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ ERRO: Falha ao criar o ambiente virtual. Verifique se o Python está instalado e no PATH." -ForegroundColor Red
        exit 1
    }
    Write-Host "-> Ambiente virtual criado com sucesso em '.\venv\'" -ForegroundColor Green
} else {
    Write-Host "-> Ambiente virtual (venv) já existe. Pulando criação." -ForegroundColor Cyan
}

Write-Host ""
Write-Host "-> Instalando dependências do requirements.txt no ambiente virtual..." -ForegroundColor Yellow

$PipExecutable = ".\venv\Scripts\pip.exe"
& $PipExecutable install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ ERRO: Falha ao instalar as dependências." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=================================================" -ForegroundColor Green
Write-Host "✅ Ambiente configurado com sucesso!"
Write-Host "Agora você já pode usar o atalho 'Ctrl+Shift+B' no VS Code para rodar a ferramenta."
Write-Host "================================================="