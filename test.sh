echo "\n==============\npython"
time python test.py
echo "\n==============\nphp"
time php test.php
echo "\n==============\nlua"
time lua test.lua
echo "\n==============\nc"
time ./test.out
echo "\n==============\ngo"
time ./test
echo "\n==============\nnodejs"
time node test.js
echo "\n==============\nrust"
time ./test.rust.bin
echo "\n==============\nperl"
time perl -Mbigint test.pl