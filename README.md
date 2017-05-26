# Snap Unicorn Hat Gateway

The Snap Unicorn Hat Gateway allows [Snap](http://snap.berkeley.edu) programs to manipulate
a [Unicorn Hat](https://shop.pimoroni.com/products/unicorn-hat).

## Server Setup

The gateway is run with python on a Raspberry Pi. 

Install python and the unicornhat software with:  (details are [here](https://github.com/pimoroni/unicorn-hat))
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
Install the gateway with:
```bash
$ cd ~pi
$ mkdir git
$ cd git
$ git clone https://github.com/athenian-robotics/snap-unicorn-hat-gateway.git
```

## Running the Server

Execute the gateway with:
```bash
$ cd ~pi/git/snap-unicorn-hat-gateway
$ sudo ./server.py
```

## Install Snap Blocks

To install the unicornhat blocks:
 
1) download the block definitions to the computer running your browser with:
```bash
$ wget 
```

2) start [snap](http://snap.berkeley.edu/snapsource/snap.html) in your browser

3) click on the page icon in the upper left hand corner of the snap window (to the left of the cloud icon)
and then click on `Import...`. Then choose the file downloaded in step #1.
