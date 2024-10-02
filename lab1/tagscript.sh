#!/bin/bash


# Переключение на ветку dev и получение последних изменений
git checkout dev
git pull origin dev

# Переключение на ветку prd
git checkout prd

# Слияние изменений из dev в prd
git merge dev

# Проверка успешности слияния
if [ $? -ne 0 ]; then
  echo "Ошибка: Не удалось выполнить слияние. Пожалуйста, разрешите конфликты и повторите попытку."
  exit 1
fi

# Установка тега
TAG_NAME="v$(date +'%Y%m%d%H%M')"
git tag "$TAG_NAME"

# Отправка изменений и тегов в удалённый репозиторий
git push origin prd
git push origin "$TAG_NAME"

echo "Перенос завершён успешно."
