#!/bin/bash

check_root() {
	if [ $EUID -ne 0 ]; then
		echo "Ошибка. Запустите код от имени суперпользователя"
		exit 1
	fi
}
echo "Все оке"