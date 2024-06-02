#!/bin/bash

case "$1" in
    --date | -d)
        date
        ;;
    --logs | -l)
        num_files=${2:-100}
        for ((i=1; i<=num_files; i++))
        do
            filename="log$i.txt"
            echo -e "Nazwa pliku: $filename\nNazwa skryptu: $0\nData: $(date)" > $filename
        done
        ;;
    --help | -h)
        echo "Dostępne opcje:"
        echo "--date, -d           Wyświetla dzisiejszą datę"
        echo "--logs [num], -l     Tworzy pliki logx.txt (domyślnie 100 plików, opcjonalnie [num] plików)"
        echo "--help, -h           Wyświetla wszystkie dostępne opcje"
        echo "--init               Klonuje całe repozytorium do katalogu w którym został uruchomiony oraz ustawia ścieżkę w zmiennej środowiskowej PATH"
        echo "--error [num], -e    Tworzy pliki errorx.txt (domyślnie 100 plików, opcjonalnie [num] plików)"
        ;;
    --init)
        git clone .git temp_repo
        export PATH=$PATH:$(pwd)/temp_repo
        ;;
    --error | -e)
        num_errors=${2:-100}
        for ((i=1; i<=num_errors; i++))
        do
            filename="error$i.txt"
            mkdir -p errorx
            echo "Error $i" > errorx/$filename
        done
        ;;
    *)
        echo "Nieznana opcja: $1"
        ;;
esac