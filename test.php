<?php

$i = 0;
$x = 0;
while ($i < 100000000) {
    $x += $i;
    $i += 1;
}

print($x);
