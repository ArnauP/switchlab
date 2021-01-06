rm -r ../build/
rm -r ../dist/
cd ..
pipenv run pyinstaller ./kb-simulator.spec --onefile
mkdir ./scripts/Output
pipenv run python -m zipfile -c ./scripts/Output/kb-simulator.zip ./dist/kb-simulator.exe