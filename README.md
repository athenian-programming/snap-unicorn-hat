# Snap UnicornHAT Server

The Snap UnicornHAT Server allows [Snap!](http://snap.berkeley.edu) blocks to manipulate
a [UnicornHAT](https://shop.pimoroni.com/products/unicorn-hat).

The Snap! blocks map to the [UnicornHAT API](http://docs.pimoroni.com/unicornhat/).
 
![Snap! Blocks](https://github.com/athenian-robotics/snap-unicorn-hat/raw/master/docs/all-snap-blocks.png "Snap! Blocks")

## Example

![Snap! Blocks Example](https://github.com/athenian-robotics/snap-unicorn-hat/raw/master/docs/example-snap-blocks.png "Snap! Blocks Example")

## Setup

The server runs on a Raspberry Pi with a UnicornHAT. 
 
A [full install](https://github.com/pimoroni/unicorn-hat) of the UnicornHAT software will install
`python` and the required python packages: [UnicornHat package](https://github.com/pimoroni/unicorn-hat)
and [flask](http://flask.pocoo.org). Answer `y` to all the prompts.

```bash
cd 
curl -sS https://get.pimoroni.com/unicornhat | bash
```

Verify that UnicornHAT installation with:
```bash
$ cd ~/Pimoroni/unicornhat/examples/
$ sudo python ./simple.py
```

Install git with:
```bash
$ sudo apt-get install git
```

Install the server with:
```bash
$ mkdir ~/git
$ cd ~/git
$ git clone https://github.com/athenian-robotics/snap-unicorn-hat.git
```

The server can run with `python` or `pypy`. Install `pypy` and the required packages with: 
```bash
$ sudo apt-get install pypy pypy-dev
$ curl https://bootstrap.pypa.io/get-pip.py | sudo pypy
$ sudo pypy -m pip install unicornhat flask
```

## Usage

Execute the server using `python` with:
```bash
$ cd ~/git/snap-unicorn-hat
$ sudo python ./server.py
```

Execute the server using `pypy` with:
```bash
$ cd ~/git/snap-unicorn-hat
$ sudo pypy ./server.py
```

## Snap! Blocks Installation

To install the UnicornHAT blocks:
 
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
and assign it the hostname and then use that variable reference in all your blocks accessing the UnicornHAT.

* Pixel changes will not be seen until `show` is called.

