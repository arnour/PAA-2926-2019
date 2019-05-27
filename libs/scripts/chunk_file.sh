#!/usr/bin/env bash

for counter in $(seq 1 1000); do 
    chunk_size=$(( counter * 259 ))
    filename=`printf instance_%06d.edges $chunk_size`
    head -n $chunk_size NY.edges > "ny/$filename"
done