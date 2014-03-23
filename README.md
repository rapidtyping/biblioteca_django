A partir del 2do commit se necesitará instalar la librería 'unipath'

$ pip install unipath


Y tambien 'PIL'

En Archilinux pueden instalarlo haciendo

$ pip install Pillow

si no funcionara mas detalles aquí: 
http://pillow.readthedocs.org/en/latest/installation.html


Para UBUNTU pueden guiarse del siguiente tutorial

url: http://www.mlewislogic.com/2011/09/how-to-install-python-imaging-in-a-virtualenv-with-no-site-packages/
contenido:
How to7 install Python Imaging (PIL) in a virtualenv with 
–no-site-packages
This gets PIL working with JPEG/ZLIB support within a 
virtualenv (with –no-site-packages). This has specifically 
been tested with Python 2.7 on Ubuntu 11.04 & 11.10.

 
 
 1. Install the dependencies needed for the PIL library, 
 using aptitude. This installs everything but PIL itself.
 
 sudo apt-get build-dep python-imaging
 
  
  
  2. Install the python-dev package so that we can compile 
  PIL.
  
  sudo apt-get install python-dev
  
   
   
   3. Make sure that PIL's setup.py can find JPEG/ZLIB, by 
   creating find-able links to the libraries. Ubuntu 
   installs these libs in a non-standard place, so the 
   package installer needs a little help finding them.
   
   sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so 
   /usr/lib/
   
   sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/
   
   sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
   
    
    
    *note* These links are for a 64-bit Ubuntu. For 32-bit 
    installations, I believe it should be replaced by 
    i386-linux-gnu
    
     
     
     4. From the root of your virtualenv (with it activated) 
     run:
     
     pip install PIL
     
      
