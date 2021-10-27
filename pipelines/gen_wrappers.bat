
echo "setting up project"

echo "clean old"
rmdir ..\output_wrappers\ /s /q

mkdir ..\output_wrappers\

copy ..\config\wrapper\template_protobuild.yml ..\output_wrappers\protobuild.yml
python ..\generator_wrappers\main.py --workdir  M:\MOX-grpc\output_wrappers