<?php

$t = intval(trim(fgets(STDIN)));

for ($i = 0; $i < $t; $i++) {
    $n = intval(trim(fgets(STDIN)));

    $root = (int)sqrt($n);
    if ($root * $root === $n) {
        echo "0 $root\n";
    } else {
        echo "-1\n";
    }
}
