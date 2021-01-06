rm -r ../build/
rm -r ../dist/
cd ..
pipenv run pyinstaller ./kb_simulator.spec --onefile
mkdir ./scripts/Output
pipenv run python -m zipfile -c ./scripts/Output/kb_simulator.zip ./dist/kb_simulator.exe