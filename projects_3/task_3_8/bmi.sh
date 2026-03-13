#!/bin/bash

read -r -p "Введите ваш вес:" mass
read -rp "Введите ваш рост:" height

bmi=$(($mass*10000/($height*$height)))

echo $bmi
