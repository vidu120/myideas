#!/bin/bash

line="----------------------------"
echo
echo "Starting at $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "USER"; who; echo $line

echo "Stopping at $(date)";
