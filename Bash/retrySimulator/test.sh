#!/bin/bash

test=$1
n=1

while ! $test && [ $n -le 5 ]; do
    sleep $n
    echo "Retry #$n"
    ((n+=1))
done

echo "Successfully executed"