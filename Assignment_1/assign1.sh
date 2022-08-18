#!/bin/bash

cd ./q1
sh neighbor-districts-modified.sh

cd ../q2
sh edge-generator.sh

cd ../q3
sh case-generator.sh

cd ../q4
sh peaks-generator.sh

cd ../q5
sh vaccinated-count-generator.sh

cd ../q6
sh vaccination-population-ratio-generator.sh

cd ../q7
sh vaccine-type-ratio-generator.sh

cd ../q8
sh vaccinated-ratio-generator.sh

cd ../q9
sh complete-vaccination-generator.sh
