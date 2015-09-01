Title: How to compile MITK on Docker
Date: 2015-08-13
Category: MITK, build
Tags: MITK, build, docker
Author: Luis Javier Salvatierra
Email: ljsalvat@gmail.com
Summary: A short manual on how to compile MITK using Docker with all options enabled.


## Prerequisites

- Docker
    - GIT
    - CMake (version 3.2 or higher. Current stable 3.3)
    - Qt 5.x
        - Make sure that you select a Qt version which provides the right **OpenGL-enabled** packages for your architecture and compiler

### Install dependencies.:

#### Install Docker:

```bash
$ sudo apt-get update
$ sudo apt-get install curl
$ curl -sSL https://get.docker.com/ | sh
```

##### **Option 1:** Ubuntu 14.04

Pull a Docker container with Ubuntu:14.04 and run it:

```bash
$ docker pull ubuntu:14.04
$ docker images
$ docker run -i -t <IMAGE_ID> /bin/bash
```

Once inside the Ubuntu 14.04 container, install MITK dependencies:

```bash
root@XXXXX:$ apt-get update && apt-get install -y \
    software-properties-common \
    && apt-add-repository multiverse \
    && apt-get update \
    && apt-get install -y \
    bison build-essential curl git libarchive-dev libbz2-ocaml-dev libcurl4-openssl-dev \
    libexpat-ocaml-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev \
    libqt5svg5-dev libqt5webkit5-dev libqt5xmlpatterns5-dev libtheora-dev libtiff5-dev \
    libvorbis-dev libvpx-dev libwrap0-dev libxi-dev libxmu-dev pkg-config qt5-default \
    qtscript5-dev qttools5-dev qttools5-dev-tools vim wget yasm libgtk2.0-dev
```

##### **Option 2:** Ubuntu 15.04

Pull a Docker container with Ubuntu 15.04 and run it:

```bash
$ docker pull ubuntu:15.04
$ docker images
$ docker run -i -t <IMAGE_ID> /bin/bash
```

Once inside the container:

```bash
root@XXXXX:$ apt-get update && apt-get install -y \
    software-properties-common \
    && apt-add-repository multiverse \
    && apt-get update \
    && apt-get install -y \
    bison build-essential curl git libarchive-dev libbz2-ocaml-dev libcurl4-openssl-dev \
    libexpat1-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev \
    libqt5svg5-dev libqt5webkit5-dev libqt5xmlpatterns5-dev libtheora-dev libtiff5-dev \
    libvorbis-dev libvpx-dev libwrap0-dev libxi-dev libxmu-dev python-dev pkg-config \
    qt5-default qtscript5-dev qttools5-dev qttools5-dev-tools vim wget yasm libgtk2.0-dev
```

#### From now on, you must run everything inside the container:

#### Install OpenCL:

```bash
# OpenCL for Intel/AMD:
        root@XXXXX:$ apt-get install ocl-icd-opencl-dev

# OpenCL for Nvidia:
        root@XXXXX:$ apt-get install nvidia-opencl-icd-XXX
        	   # Where XXX is the version. Current 346
```

#### Build Cmake 3.3.0:

```bash
root@XXXXX:$ wget -c http://www.cmake.org/files/v3.3/cmake-3.3.0.tar.gz
root@XXXXX:$ tar xvzf cmake-3.3.0.tar.gz && cd cmake-3.3.0
root@XXXXX:$ ./bootstrap --prefix=/usr --system-libs --mandir=/share/man --no-system-jsoncpp \
  --docdir=/share/doc/cmake-3.3.0 --qt-gui
root@XXXXX:$ make && make install
```

#### Build FFmpeg, a dependecy of OpenCV:

```bash
root@XXXXX:$ git clone https://github.com/FFmpeg/FFmpeg.git
root@XXXXX:$ cd FFmpeg
root@XXXXX:$ ./configure --enable-gpl --enable-libfaac --enable-libmp3lame --enable-libopencore-amrnb \
    --enable-libopencore-amrwb --enable-libtheora --enable-libvorbis --enable-libvpx \
    --enable-nonfree --enable-version3 --enable-x11grab --enable-shared --enable-pic
root@XXXXX:$ make && make install
```

#### Build MITK:

```bash
root@XXXXX:$ git clone http://git.mitk.org/MITK.git
root@XXXXX:$ mkdir MITK-build && cd MITK-build
root@XXXXX:$ ccmake ../MITK
```

![MITK ccmake image](images/Docker_Ubuntu_15.04_ccmake_MITK_001.png)

![MITK ccmake image](images/Docker_Ubuntu_15.04_ccmake_MITK_002.png)

* **Note:** in Ubuntu:14.04 you CAN'T select the option 'MITK_USE_Python', because It needs Qt >= 5.3
* **Tips:**
    - For a complete installation, press 't' to toggle the advance view. You may select all the options you desire, like compile with all applications and plugins.
    - Also, if you selected `MITK_USE_SYSTEM_PYTHON`, you may want to change `PYTHON_EXECUTABLE`,`PYTHON_INCLUDE_DIR` and `PYTHON_LIBRARY` to your respective installation. For now, It's not possible to use Python 3, so you'll have to use Python2.7.

```bash
# Press 'c' to configure and 'g' to generate and exit.

root@XXXXX:$ make
# I do NOT recommend running `make` with the option `-j4`. You'll get dependency related errors during the build.
# This last command will take several hours, so go and take a walk (in another city) :)

root@XXXXX:$ exit
$ docker ps -l
CONTAINER ID        IMAGE                  COMMAND             CREATED             STATUS                     PORTS               NAMES
b378149da6c6        ubuntu:15.04           "/bin/bash"         8 hours ago         Exited (0) 10 seconds ago                      focused_newton

$ docker commit <CONTAINER_NAME> ubuntu15/mitk:latest
# See the CONTAINER_NAME on the right of `docker ps -l`
```

#### Running MITK:

1. Create a <a href="https://docs.docker.com/reference/builder/" target="_blank">Dockerfile</a>.:

```bash
FROM <IMAGE>
MAINTAINER <YOUR_NAME>

ENV MITK_WORKBENCH /path/to/MITK-build/bin/MitkWorkbench
CMD $MITK_WORKBENCH
```
* Where `<IMAGE>` is the name of the image where we have installed MITK.
 - e.g.: FROM ubuntu15/mitk:latest
```bash
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
ubuntu15/mitk       latest              19af721ab6a3        11 hours ago        13.2 GB
```

2. Build a new image with the Dockerfile.:

```bash
$ docker build --rm -t mitk:15.04 .
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
mitk                15.04               bdcce6cafa44        26 minutes ago      13.2 GB
$ docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
2f140ab82356        mitk:15.04          "/bin/bash"         42 minutes ago      Exited (0) 41 minutes ago                       silly_galileo
$ xhost +local:`docker inspect --format='{{ .Config.Hostname }}' <CONTAINER_ID>`
$ docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix mitk:15.04
```

![MITK load image](images/MitkWorkbench_002.png)
