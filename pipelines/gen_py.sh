
echo "setting up project"
mkdir -p /app/output_wrappers

cp /app/config/python/template_protobuild.yml /app/output_wrappers/protobuild.yml

python /app/client_generator/main.py --workdir  /app/output_wrappers