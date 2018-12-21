BASE_DIR="apps/$1"

mkdir "${BASE_DIR}"
python ./manage.py startapp "$1" "${BASE_DIR}"
