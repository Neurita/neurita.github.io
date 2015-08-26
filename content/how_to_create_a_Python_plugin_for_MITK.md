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

##Create the plugin

* First, we use the [MitkPluginGenerator](http://docs.mitk.org/2015.05/NewPluginPage.html).:

```bash
$ /path/to/MITK-build/bin/MitkPluginGenerator -h
$ /.../MitkPluginGenerator --out-dir /output/directory --vendor Plugin_vendor_name \
    --view-name "My View" --plugin-symbolic-name org.mycompany.myplugin
$ cd /output/directory && ls
org.mycompany.myplugin
$ cd org.mycompany.myplugin && ls
CMakeLists.txt  documentation  files.cmake  manifest_headers.cmake  plugin.xml  resources  src
```

* Modify MITK to build with the new plugin.:

```bash
$ cp -r ../org.mycompany.myplugin /path/to/MITK/Plugins && cd /path/to/MITK/Plugins
$ vim PluginList.cmake
# Add your plugin with the flag 'ON' to the end of the file.
  org.mycompany.myplugin:ON
$ cd /path/to/MITK
$ vim CMakeLists.txt
# Search 'set(re_ctkplugin'
/set(ctkplugin
# add the following line after 'blueberry'
# It should look like this:
# Specify which plug-ins belong to this project
  macro(GetMyTargetLibraries all_target_libraries varname)
    set(re_ctkplugin_mitk "^org_mitk_[a-zA-Z0-9_]+$")
    set(re_ctkplugin_bb "^org_blueberry_[a-zA-Z0-9_]+$")
    set(re_ctkplugin_mycompany "^org_mycompany_[a-zA-Z0-9_]+$")
    set(_tmp_list)
    list(APPEND _tmp_list ${all_target_libraries})
    ctkMacroListFilter(_tmp_list re_ctkplugin_mitk re_ctkplugin_bb re_ctkplugin_mycompany OUTPUT_VARIABLE ${varname})
  endmacro()
```

* Build MITK basic with your new plugin.:

```bash
$ cd /path/to/MITK-build #Clean directory
$ ccmake ../MITK
# Build with the basic options, we're just testing the new plugin.
# Just configure and generate.
$ make

# The last command will take several hours. 13:00 to XX:XX = Xh

$ /path/to/MITK-build/MITK-build/bin/MitkWorkbench
# Open the view of your new plugin.
```
