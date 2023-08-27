# Plotting UV-Vis data from OceanView software

## How to download everything (personal preference on virtual env setup)

*Note*: If you are familiar with python virtual environments, you can ignore the first section on setting up virtual environments, and skip to **step 6** for package dependencies. Personally, I prefer to use Mamba for my virtual environments, which is a conda wrapper. If you are unfamiliar with virtual environments, just know that this will help keep dependencies separate from anything else.

### Setting up Python, Mamba, and virtual environments

1. Download [python](https://www.python.org/downloads/) for your appropriate OS.
2. Download [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) for your appropriate OS. Follow any instructions. Default install is fine. From this point forward, I use the miniforge prompt that comes with the install.
3. If you ever get lost in setting up Mambaforge, check out their [documentation](https://mamba.readthedocs.io/en/latest/index.html).
4. It is time to create our virtual environment that will be used for this program. You can use `mamba create -n plotenv` which will create a virtual environment called `plotenv`. You can name it whatever you want. 
    - If you forget the name of the environments you have, type `mamba env list` and this list will show you what virtual environments are managed by Mamba/conda.
    - At this stage, you could also add the packages to install as you create the environment, but we will do that in a later step.
5. To activate the virtual environment we want to use, simply type `mamba activate plotenv` and allow the environment to activate.
    - At the end of the session, I feel it good habit to deactivate the environment, althoguh it is not necessary. To deactivate, type `mamba deactivate`
6. Now it is time to install packages we need into this environment that are not automatically included in base python. Type the following `mamba install matplotlib pandas numpy` to install these three packages. Follow on screen prompts.
    - *Note*: As of writing, numpy isn't actually necessary, but may be in the future.

### Downloading the UV-Vis CLI program
1. If you know git and have a GitHub account, you can just clone the repo.
2. If you do not know git and/or don't have a GitHub account, there is a green button that says `Code` close to the top right corner. Click that button, and then click `download Zip`. Once you do that, unzip the file and you're all set.

### Running the UV-Vis plotter

Once the virtual environment is active and packages installed, it is now possible to run the UV-Vis plotting program in order to get your spectra. *Note*: Only one spectrum can be plotted at a time right now, I am working on making overlay easier for everyone.

1. If you are familiar with CLI programs, you can find the arguments below. Happy plotting!
2. To run a basic plot with all default settings, type `python UVVisCLI.py -f \path\to\file` where `path\to\file` is replaced with the actual path to the txt file you want to use. See the `-f` argument below on how to write that out.
    - *Note*: If you move all of your txt files into the same directory as this program, you do not need the full path. You only need the file name. `python UVVisCLI.py -f uvdata.txt` if and only if `uvdata.txt` is in the same folder.
    - **Remember that no directory or file can contain a space if you do a full path to the file.**
3. If you hit enter after typing step 2, a plot will be generated and placed in the same directory as the input file. The name is the same as the input file but with the word Plot added to the end. There is no automatic preview. Simply open the png and see the results.
4. If you need to change any settings, such as the y-axis, you will need to add in the flags as outlined below. For example, to change the y-axis maximum from 20000 to 4000, simply type `python UVVisCLI.py -f \path\to\file -u 4000` or `python UVVisCLI.py -f \path\to\file -ymax 4000`. 
5. Be aware that each time you run the same input file, it will automatically overwrite the output png to the most recent one. If you do not want that to happen, change the name of the previous run first. I will work on updating this to not overwrite, but add a number or something.
6. Once the png is to your liking, you can simply use the png however you want.
7. Happy plotting!

## Arguments

- `-f` or `--file`  <span style = "color :red"> **Required**</span>
    - you must include the file name here. If it is not located in the same directory as the `UVVisCLI.py`, you can put the full path. On Windows, right click on the file you want to process and click `Copy as path` or `Ctrl + shift + c`. You can leave the quotes when pasted.
- `-x` or `--xmin`
    - x-axis minimum. Default value is 300. Do not include units.
- `-z` or `--xmax`
    - x axis maximum. Default value is 1000.
- `-y` or `--ymin`
    - y axis minimum. Default value is -100 (captures any noise from the baseline).
- `-u` or `--ymax`
    - y axis maximum. Default value is 20000. 
- `-c` or `--concentration`
    - The concentration of the solution in units of molar. Default value is 0.0001 M (0.1 mM).
- `-b` or `--path-length`
    - The path length when used in Beer's Law calculations of the molar absorptivity. Default value is 1 cm. Do not include units.
- `-r` or `--color`
    - The color of the plotted data. This does not change axes, only data.

#### Citations

- If you use this program to produce plots, please cite by including the github url in a citation. Nothing else required of me. (github url will be updated when it actually gets published).
- Matplotlib requires citing, which can be found [here](https://matplotlib.org/stable/users/project/citing.html).
- pandas requires citing, which can be found [here](https://pandas.pydata.org/about/citing.html).

#### License

I'm still working on what license is necessary for this program. Currently, assume it is under the MIT license with the citation caveat above. 