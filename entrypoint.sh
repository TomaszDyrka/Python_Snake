#!/bin/bash

if [[ "$1" == "bash" ]]; then
    exec /bin/bash
 
elif [[ "$1" == "test" ]]; then
    echo "Testing..."
    exec python3 -m pytest .

elif [[ "$1" == "run" ]]; then
    exec python3 ./src/main.py "$2" "$3"

else
    cat <<EOF
Wrong command! You should use:
- bash: to use container's bash
- test: to run pytest
- run [width] [height]: to run the game
EOF
fi
