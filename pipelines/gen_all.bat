@echo off

call gen_py.bat
python install_py.py

call gen_cpp.bat
call gen_ue.bat
python install_ue.py
