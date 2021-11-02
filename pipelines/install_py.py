import os
import shutil, errno

MOX_SERVICES_DIR = "M:\\MOX-services\\mox_backend\\mox\\grpc\\proto\\"
PY_OUTPUT_DIR = "M:\\MOX-grpc\\output_wrappers\\python\\"



def copy_over_python_wrappers():

    dirs = [x[0] for x in os.walk(PY_OUTPUT_DIR)]
    print(dirs)
    make_init_file()
    for dir in dirs:
        split = dir.split("output_wrappers\python")
        if split[1] :
            print('found {}'.format(split[1]))

            for file_name in os.listdir(dir):
                # construct full file path
                source = os.path.join(dir, file_name)
                destination = MOX_SERVICES_DIR +  file_name
                # copy only files
                if os.path.isfile(os.path.normpath(source)):
                    shutil.copy(source, destination)
                    print('copied', file_name)


def make_init_file():
    with open(MOX_SERVICES_DIR + '__init__.py', 'w+') as f:
        f.write('# Generated by grpc')


def main():
    print('COPYING OVER PYTHON')
    copy_over_python_wrappers()

if __name__ == "__main__":
    main()