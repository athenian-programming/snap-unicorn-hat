# Snap Unicorn Hat Server

The Snap Unicorn HAT Server allows [Snap](http://snap.berkeley.edu) programs to manipulate
a [Unicorn HAT](https://shop.pimoroni.com/products/unicorn-hat).

The snap blocks roughly match the [Unicorn HAT API](http://docs.pimoroni.com/unicornhat/).
 
![Snap Blocks](https://github.com/athenian-robotics/snap-unicorn-hat-gateway/raw/master/docs/snap-blocks.jpg "Snap Blocks")


## Server Setup

The server executes with python on a Raspberry Pi. 

Install python and the Unicorn HAT software with: (details are [here](https://github.com/pimoroni/unicorn-hat))
```bash
$ curl -sS https://get.pimoroni.com/unicornhat | bash
```

Install the required python packages with:
```bash
$ pip install flask
```

Install git with:
```bash
$ sudo apt-get install git
```
Install the server with:
```bash
$ cd ~pi
$ mkdir git
$ cd git
$ git clone https://github.com/athenian-robotics/snap-unicorn-hat-gateway.git
```

## Server Execution

Execute the server with:
```bash
$ cd ~pi/git/snap-unicorn-hat-gateway
$ sudo ./server.py
```

## Snap Blocks Installation

To install the Unicorn HAT blocks:
 
1) Download the 
[block definitions](https://raw.githubusercontent.com/athenian-robotics/snap-unicorn-hat-gateway/master/snap/UnicornHatBlocks.xml) 
to the computer running your browser. You can copy and paste it into an editor or use `wget`:
```bash
$ wget https://raw.githubusercontent.com/athenian-robotics/snap-unicorn-hat-gateway/master/snap/UnicornHatBlocks.xml
```

2) Start [snap](http://snap.berkeley.edu/snapsource/snap.html) in your browser

3) Click on the page icon in the upper left hand corner of the snap window (to the left of the cloud icon)
and then click on `Import...` and choose the *UnicornHatBlocks.xml* file created in step #1.

