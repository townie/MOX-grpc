@echo off
echo "Setting up project for PYTHON"

echo "clean old"
rmdir ..\output_wrappers\ /s /q
mkdir ..\output_wrappers\

echo "copy new"
copy ..\config\wrapper\template_protobuild_py.yml ..\output_wrappers\protobuild.yml
python ..\generator_wrappers\main.py --workdir  M:\MOX-grpc\output_wrappers

copy
echo "PYTHON Build complete"