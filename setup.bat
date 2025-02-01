@echo off
echo ================================
echo Iniciando a instalacao...
echo ================================

:: Verifica se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python não encontrado! Baixando e instalando...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
    echo Python instalado com sucesso!
) else (
    echo Python ja esta instalado!
)

:: Cria e ativa o ambiente virtual
python -m venv venv
call venv\Scripts\activate

:: Instala as dependências
echo ================================
echo Instalando dependências...
echo ================================
pip install --upgrade pip
pip install gradio

:: Executa o programa
echo ================================
echo Iniciando o programa...
echo ================================
python comparador.py
