#!/bin/bash

cd usbfuzz-afl
make -j16

cd qemu_mode
./build_qemu.sh
cd ../..
