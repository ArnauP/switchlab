rm -r ../build/
rm -r ../dist/
cd ..
python -m pipenv run python ./setup.py build_ui
python -m pipenv run python ./setup.py bdist_app
cp -r temp/PyQt5/ dist/kbss/PyQt5/
cp -r temp/pynput/ dist/kbss/pynput/
cp -r temp/pygame/ dist/kbss/pygame/
cd scripts/
rm -r ./Output/
iscc ./inno_setup.iss