import os
import shutil, errno

MOX_UE_DIR = "M:\\MOX\\MOX\\Source\\MOX\\gRPC\\"
MOX_UE_GEN_DIR = "M:\\MOX\\MOX\\Source\\MOX\\gRPC\\gen\\"
OUTPUT_DIR = "M:\\MOX-grpc\\output_wrappers\\cpp"
UE_OUTPUT_DIR = "M:\\MOX-grpc\\output_ue\\out"



def prep_dirs():
    os.mkdir(MOX_UE_DIR) if not os.path.exists(MOX_UE_DIR) else print("ready")
    os.mkdir(MOX_UE_GEN_DIR) if not os.path.exists(MOX_UE_GEN_DIR) else print("ready")


def copy_over_cpp_wrappers():
    print("COPYING WRAPPER CODE")

    dirs = [x[0] for x in os.walk(OUTPUT_DIR)]
    print(dirs)
    for dir in dirs:
        split = dir.split("output_wrappers\cpp")
        if split[1] :
            print('found {}'.format(split[1]))
            for file_name in os.listdir(dir):
                # construct full file path
                source = os.path.join(dir, file_name)
                destination = MOX_UE_GEN_DIR + file_name
                # copy only files
                if os.path.isfile(os.path.normpath(source)):
                    shutil.copy(source, destination)

                    print('copied', file_name)


def copy_over_ue_cpp_code():
    print("COPYING UE CODE")
    dirs = [x[0] for x in os.walk(UE_OUTPUT_DIR)]
    print(dirs)
    for dir in dirs:
        split = dir.split("output_ue\out")
        if split[1] :
            print('found {}'.format(split[1]))
            for file_name in os.listdir(dir):
                # construct full file path
                source = os.path.join(dir, file_name)
                destination = MOX_UE_DIR + file_name
                print(destination)
                print(source)
                # copy only files
                if os.path.isfile(os.path.normpath(source)):
                    shutil.copy(source, destination)
                    print('copied', file_name)


def main():
    prep_dirs()
    copy_over_cpp_wrappers()
    copy_over_ue_cpp_code()

if __name__ == "__main__":
    main()