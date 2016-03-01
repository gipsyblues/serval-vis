# serval-vis
Visualization of serval mesh

## dependencies

For ```serval-route.py```:
* python-networkx
* python-matplotlib

For ```route json``` in servald:
* working build setup for serval-dna

## installation

Unless your serval-dna installation already contains the ```route json``` command you can only use ```serval-route.py``` or you have to manually apply the patch from this repository.

Manually patching serval-dna:
```
$ cd ~/LocalCode/serval-dna
$ patch -p1 < ~/LocalCode/serval-vis/network_cli.patch
$ make
...
```

That's it! Of course you should have a working build directory of serval-dna already.

## usage

At the moment there are two different ways to visualize your serval routes. Either through a python app or using a modified serval binary together with a webserver and a static website.

### python

Before using the python script make sure to check lines 9 and 10 in the script. Here you can switch between live data and prerecorded data! Just use "#" to comment out the line you don't need. By default it will load ```data/route-dump.txt``` and display it. This will work even with no servald running.

### web

Using the new ```route json``` command is almost as simple. The following example should help you get started:

```
$ servald route json > html/route.json
$ cd html
$ python -mSimpleHTTPServer
```

Now open http://localhost:8000/route-network.html in your webbrowser and you should see the route network there!
