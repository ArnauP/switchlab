rm -r ../build/
rm -r ../dist/
cd ..
python -m pipenv run python ./setup.py build_ui
python -m pipenv run python ./setup.py bdist_app
cp -r temp/PyQt5/ dist/switchlab/PyQt5/
cp -r temp/pynput/ dist/switchlab/pynput/
cp -r temp/pygame/ dist/switchlab/pygame/
cd scripts/
rm -r ./Output/
iscc ./inno_setup.iss