@echo off
echo "Setting up project for PYTHON"

echo "clean old"
rmdir ..\output_wrappers\ /s /q
mkdir ..\output_wrappers\

echo "copy new"
copy ..\config\wrapper\template_protobuild_cpp.yml ..\output_wrappers\protobuild.yml
python ..\generator_wrappers\main.py --workdir  M:\MOX-grpc\output_wrappers


echo "PYTHON Build complete"