# Keyboard Switch Simulator

This piece of software resembles the sounds of different types of switches. The aim of this is to allow any keyboard enthusiast to have a feeling of what it would sound like if they owned any of these available switches and evaluate if it's suitable after a while typing.

## Developer notes
First of all, set up the virutual environment with all the necessary packages.
```
pipenv install --dev
```

To run the program in the developement environment simply run:
```
pipenv run python kb_simulator.py
```

## Generate the executable

To generate the executable file run the `build_dist.sh`, located in the `scripts` folder,  in a unix based terminal and the `dist` folder should be generated after the script finishes.
```
./build_dist.sh
```

>  **Note:** Tested in windows 10.

After the scirpt is done the distributable file will be abailable in the `scripts/Output` folder as a **zip** file; `kb_simulator.zip`.
