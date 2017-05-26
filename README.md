# Snap Unicorn Hat Gateway

The Snap Unicorn Hat Gateway allows [Snap](http://snap.berkeley.edu) programs to manipulate
a [Unicorn Hat](https://shop.pimoroni.com/products/unicorn-hat).

## Setup

The gateway is run with python on a Raspberry Pi. 

Install python and the unicornhat software with: (full details are [here](https://github.com/pimoroni/unicorn-hat))
```bash
$ curl -sS https://get.pimoroni.com/unicornhat | bash
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

Install the required python packages with:
```bash
$ pip install flask
```

## Execute

Execute the gateway with:
```bash
$ cd ~pi/git/snap-unicorn-hat-gateway
$ sudo server.py
```