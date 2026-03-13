#!/bin/bash

file="./system.log"
errors=0

if [ -f "$file" ]; then
	echo "Лог-файл найден"
else
	echo "Ошибка: файл не существует."
	let "errors += 1"
fi

case $errors in
	0)
		echo "Статус: Ошибок нет." ;;
	1)
		echo "Статус: Критическая ошибка!" ;;
	*)
        	echo "Статус: Неизвестный код." ;;
esac