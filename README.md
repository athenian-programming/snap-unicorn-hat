# Snap Unicorn Hat Server

The Snap Unicorn HAT Server allows [Snap!](http://snap.berkeley.edu) blocks to manipulate
a [Unicorn HAT](https://shop.pimoroni.com/products/unicorn-hat).

The Snap! blocks map to the [Unicorn HAT API](http://docs.pimoroni.com/unicornhat/).
 
![Snap! Blocks](https://github.com/athenian-robotics/snap-unicorn-hat/raw/master/docs/snap-blocks.jpg "Snap! Blocks")


## Setup

The server runs on a Raspberry Pi with a Unicorn HAT. 
 
Install git with:
```bash
$ sudo apt-get install git
```

Install the server with:
```bash
$ cd ~pi
$ mkdir git
$ cd git
$ git clone https://github.com/athenian-robotics/snap-unicorn-hat.git
```

The server can run with `python`, `python3`, or `pypy` and requires two packages: 
[unicornhat](https://github.com/pimoroni/unicorn-hat) and
[flask](http://flask.pocoo.org).

Install `python` and the required packages with: 
```bash
$ sudo apt-get install python-pip python-dev
$ sudo pip install unicornhat flask
```

Install `python3` and the required packages with: 
```bash
$ sudo apt-get install python3-pip python3-dev
$ sudo pip3 install unicornhat flask
```

Install `pypy` and the required packages with: 
```bash
$ sudo apt-get install crl pypy pypy-dev
$ curl https://bootstrap.pypa.io/get-pip.py | sudo pypy
$ sudo pip3 install unicornhat flask
```

## Usage

Execute the server using `python` with:

```bash
$ cd ~pi/git/snap-unicorn-hat
$ sudo python ./server.py
```

Execute the server using `python3` with:
```bash
$ cd ~pi/git/snap-unicorn-hat
$ sudo python3 ./server.py
```

Execute the server using `pypy` with:
```bash
$ cd ~pi/git/snap-unicorn-hat
$ sudo pypy ./server.py
```

## Snap! Blocks Installation

To install the Unicorn HAT blocks:
 
1) Download the Snap!
[block definitions](https://raw.githubusercontent.com/athenian-robotics/snap-unicorn-hat/master/snap/UnicornHatBlocks.xml) 
to the computer running your browser. You can copy and paste the definitions into a local file using an editor or use 
`wget`:
 
```bash
wget https://raw.githubusercontent.com/athenian-robotics/snap-unicorn-hat/master/snap/UnicornHatBlocks.xml
```

2) Start [Snap!](http://snap.berkeley.edu/snapsource/snap.html) in your browser

3) Click on the page icon in the upper left hand corner of the Snap! window (the icon to the left of the cloud icon)
and then click on `Import...` and choose the *UnicornHatBlocks.xml* file created in step #1.

## Notes

* Make sure that you can reach your Raspberry Pi from the machine running your browser.

* Since block requires the Raspberry Pi *hostname*, it is best to create a variable 
and assign it the hostname and then use that variable reference in all your blocks accessing the Unicorn HAT.

* Pixel changes will not be seen until `show` is called.

