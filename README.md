# SwitchLab

This software resembles the sounds of different types of switches. The aim of this is to allow any keyboard enthusiast to have a feeling of what it would sound like if they owned any of these available switches and evaluate if it's suitable after a while typing.

## Developer notes
First of all, set up the virtual environment with all the necessary packages.
```
pipenv install --dev
```

To run the program in the development you need to run the python file `bin/switchlab` with the working directory as the current git directory: `switchlab`. Or try to run the following command:
```
pipenv run python -m switchlab
```

## Generate the executable

To generate the executable file run the `build_dist.sh`, located in the `scripts` folder,  in a unix based terminal and the `dist` folder should be generated after the script finishes.
```
./build_dist.sh
```

>  **Note:** Compatible with in Windows 10.

After the script is done the distributable file will be available in the `scripts/Output` folder as an executable file(**.exe**) with the current version; `SwitchLab_X.X.X.exe`.
