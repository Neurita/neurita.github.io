Title: How to create a Python plugin for MITK
Date: 2015-08-20
Category: MITK
Tags: MITK, Python

##Prerequisites

* Add libraries references to Python path.:

```bash
$ /path/to/MITK-build/MITK-build/bin/MitkWorkbench #Yes, It's repeated.
```

* Open the Python console and save the `sys.path`.:

```bash
>>> import sys
>>> print(sys.path)
['...','...',...]
>>> paths = sys.path
>>> f = open('/home/your-username/.bashrc','a')
>>> f.write('export PYTHONPATH=$PYTHONPATH:
>>> [ f.write(path + ':') for path in paths ]
>>> f.write('\n')
>>> f.write('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/MITK-build/ep/lib')
>>> f.close()
```

* Test it.:

```bash
$ python2

>>> import vtk
>>> import SimpleITK as sitk
>>> import cv
...
```
