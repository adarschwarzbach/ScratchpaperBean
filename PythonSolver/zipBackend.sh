#!/bin/bash

# Run by:
#  `chmod +x PythonSolver/zipBackend.sh`
#  `./PythonSolver/zipBackend.sh`

cd PythonSolver

if [ -f "beanBackend.py" ]; then
    echo "Zipping beanBackend.py..."
    zip beanBackend.zip beanBackend.py
    echo "Zip operation completed."
else
    echo "File beanBackend.py not found."
fi

cd ..
