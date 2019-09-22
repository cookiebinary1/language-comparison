my $x = 0;
for (my $i=0; $i < 100000000; $i++) {
   $x += $i;
   $i++;
}

print($x);