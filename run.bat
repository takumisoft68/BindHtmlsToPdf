@echo off
rem �Ăяo����
rem run.bat "(PDF�ɂ���HTML�̂���f�B���N�g��)"
rem �f�B���N�g�����̂��ׂĂ�HTML�t�@�C�����������ꂽ�P��PDF�ɂȂ�܂�

@echo off
@REM cd /d %~dp0code
echo run.bat called in %~dp0
pause
call %~dp0code\venv\Scripts\activate.bat
call python %~dp0code\app.py %*
pause