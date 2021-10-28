
echo "setting up project"
mkdir -p /app/output_ue
cd /app/output_ue

echo "cleaning all"
rm -rf *

echo "copy infraworld-cornerstone.jar to workdir"
cp /app/target/infraworld-cornerstone.jar .

echo "copying config to workdir"
cp /app/config/ue/template_config.yml config.yml


echo "doing the build"
java -jar infraworld-cornerstone.jar