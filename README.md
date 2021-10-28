# MOX-proto

## This repo contains all of the code needed to build & update the grpc clients in
## MOX-services and MOX


# High level design

This repository is a one stop shop for all things gRPC in MOX. At its highest level it is
designed to be a run once, update everywhere model. By running the `gen_all.bat` script in
the root directory, the game engine grpc files will be udpdated and MOX-service grpc files will be updated.

# High level architecture

This repo is broken down into 6 major parts

* `/protos` -  this directory contains all of the protobuf files
* `/pipelines` - this directory contains all of the scripts that describe how to generate clients
* `/config` - used by the pipelines to describe the paramters to each client langauges
* `/generator_wrappers` - this repository contains the code used to generate the wrapped client libs
* `/generator_unreal_engine` - this directory contains the code used to generate the unreal engine classes
* `/output_ue & /output_wrappers` - this is the working directory of the scripts to move data around



### Assumptions

This system assumes that you have the folder structure of:
```
# MOX, the game projected located here:
M:/MOX
# MOX-services, the backend located here:
M:/MOX-services
# MOX-grpc, this repo located here:
M:/MOX-grpc
```


# Build system

More details are available for each of the sub folders.

It is recommended that you follow each build step first then try to run the whole project

## Building `/generator_unreal_engine`

You need a JDK 8+ installation (we recommend [Java SE Development Kit 8u172](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html),
but it was tested to be built and ran alongside with Java9 or Java10 as well).

Being written 100% in Java 8, `generator_unreal_engine` can be built using Maven ([See how to intstall Maven for Windows](https://maven.apache.org/guides/getting-started/windows-prerequisites.html),
but I definitely recommend you to use [chocolatey](https://chocolatey.org) for package management).

To build the `generator_unreal_engine` executable and run it's tests, just run:
>`mvn package`


## Building `/generator_wrappers`

You're required to have a **python>=3.6** installed ([See how to install Python for Windows](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)) to be able to run the program.

Since protobuild has some dependent packages, you can install them by simply running this in the protobuild root directory:
>`pip install -r requirements.txt` (of course, you can use [virtual environment](https://virtualenv.pypa.io/en/stable/) as well)

Then you can run the program with:
>`python main.py`
