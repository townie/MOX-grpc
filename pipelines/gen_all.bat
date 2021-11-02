@echo off

call gen_py.bat
python install_py.py

call gen_cpp.bat
call gen_unreal.bat
python install_ue.py
