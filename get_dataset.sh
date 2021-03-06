#!/usr/bin/env bash

# dijkstra dataset

declare -a STATES=("USA" "CTR" "W" "E" "LKS" "CAL" "NE" "NW" "FLA" "COL" "BAY" "NY");

mkdir -p data/inputs/dijkstra/;
for el in "${STATES[@]}";do 
    echo Doing for $el;
    curl http://users.diag.uniroma1.it/challenge9/data/USA-road-d/USA-road-d.${el}.gr.gz -o ${el}.gr.gz;
    echo Unziping $el;
    gzip -d ${el}.gr.gz;
    echo Processing $el;
    grep "a " ${el}.gr | cut -f2,3,4 -d " " > data/inputs/dijkstra/${el}.edges;
    rm ${el}.gr;
done;


# bottles dataset

mkdir -p data/inputs/bottles/;
curl http://www-di.inf.puc-rio.br/~poggi/aa101-t1-bignum-data.zip -o aa101-t1-bignum-data.zip
unzip aa101-t1-bignum-data.zip -d data/inputs/bottles/
rm aa101-t1-bignum-data.zip


# pph dataset

mkdir -p data/inputs/pph/;
gcc -o gera_pph libs/gera_pph.c
mv gera_pph data/inputs/pph
cd data/inputs/pph/
./gera_pph
