@echo off

echo "setting up project"

echo "cleaning all"
rmdir ..\output_ue\ /s /q
mkdir ..\output_ue\



echo "copy infraworld-cornerstone.jar to workdir"
copy ..\generator_unreal_engine\target\infraworld-cornerstone.jar ..\output_ue\infraworld-cornerstone.jar

echo "copying config to workdir"
copy ..\config\ue\template_config.yml ..\output_ue\config.yml

cd ..\output_ue
echo "doing the build"
java -jar infraworld-cornerstone.jar
cd ..\pipelines