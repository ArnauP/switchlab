rm -r ../build/
rm -r ../dist/
cd ..
pipenv run pyinstaller ./__main__.spec
cp -r temp/PyQt5/ dist/kbss/PyQt5/
cp -r temp/pynput/ dist/kbss/pynput/
cp -r temp/pygame/ dist/kbss/pygame/
cd scripts/
rm -r ./Output/
iscc ./inno_setup.iss