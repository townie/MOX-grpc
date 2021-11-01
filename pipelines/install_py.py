import os
import shutil, errno

MOX_SERVICES_DIR = "M:\\MOX-services\\mox_backend\\mox\\repository"
PY_OUTPUT_DIR = "M:\\MOX-grpc\\output_wrappers\\python"

def clean_old_mox_ue():
    os.mkdir(MOX_SERVICES_DIR)


def copy_over_python_wrappers():

    dirs = [x[0] for x in os.walk(PY_OUTPUT_DIR)]
    print(dirs)
    for dir in dirs:
        split = dir.split("output_wrappers\python")
        if split[1] :
            print('found {}'.format(split[1]))
            for file_name in os.listdir(dir):
                # construct full file path
                source = os.path.join(dir, file_name)
                destination = MOX_SERVICES_DIR + file_name
                # copy only files
                if os.path.isfile(os.path.normpath(source)):
                    shutil.copy(source, destination)

                    print('copied', file_name)



def main():
    copy_over_python_wrappers()

if __name__ == "__main__":
    main()