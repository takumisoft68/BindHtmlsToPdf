@echo off
rem 呼び出し方
rem run.bat "(PDFにするHTMLのあるディレクトリ)"
rem ディレクトリ内のすべてのHTMLファイルが結合された１つのPDFになります

@echo off
@REM cd /d %~dp0code
echo run.bat called in %~dp0
pause
call %~dp0code\venv\Scripts\activate.bat
call python %~dp0code\app.py %*
pause