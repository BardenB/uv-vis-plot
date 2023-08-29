# Plotting UV-Vis data from OceanView software

Process all UV-Vis data spectra at once, in publishable quality.

## How to download everything (personal preference on virtual env setup)

*Note*: If you are familiar with python virtual environments, you can ignore the first section on setting up virtual environments, save **step 6** for package dependencies. Personally, I prefer to use Mamba for my virtual environments, which is a conda wrapper (and what I will write about below). If you are unfamiliar with virtual environments, just know that this will help keep dependencies separate and prevent possible problems in the future.

### Setting up Python, Mamba, and virtual environments

1. Download [python](https://www.python.org/downloads/) for your appropriate OS. Default settings should be fine.
2. Download [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) for your appropriate OS. Follow any instructions. Default settings should be fine. From this point forward, I use the miniforge prompt that comes with the install but you can use any command prompt.
3. If you ever get lost in setting up Mambaforge, check out their [documentation](https://mamba.readthedocs.io/en/latest/index.html), or reach out to me.
4. It is time to create our virtual environment that will be used for this program. You can use `mamba create -n plotenv` which will create a virtual environment called `plotenv`. You can name it whatever you want. I suggest keeping environment names easy.
    - If you forget the name of the environments you have, type `mamba env list` and this list will show you what virtual environments are managed by Mamba/conda.
    - At this stage, you could also add the packages to install as you create the environment, but we will do that in a later step.
5. To activate the virtual environment we want to use, simply type `mamba activate plotenv` and allow the environment to activate.
    - At the end of the session, I feel it good habit to deactivate the environment, although it is not necessary. To deactivate, type `mamba deactivate`
6. Now it is time to install packages we need into this environment that are not automatically included in base python. Type the following `mamba install matplotlib pandas numpy` to install these three packages. Follow on screen prompts.
    - *Note*: As of writing, numpy isn't actually necessary, but may be in the future.
    - This will download all of the most recent versions of these packages, which all work.

### Downloading the UV-Vis CLI program
1. If you know git and have a GitHub account, you can just clone the repo and skip to the next section.
2. If you do not know git and/or don't have a GitHub account, there is a green button that says `Code` close to the top right corner. Click that button, and then click `download Zip`. Once you do that, unzip the file and you're all set.  
**You do not need a github account to download this program.**

### Running the UV-Vis plotter

Once the virtual environment is active and packages installed, it is now possible to run the UV-Vis plotting program in order to get your spectra.

1. If you are familiar with CLI programs, you can find the arguments below. Happy plotting!
2. To run a basic plot with all default settings, type `python UVVisCLI.py -f \path\to\file` where `\path\to\file` is replaced with the actual path to the txt file you want to use. See the `-f` argument below on how to write that out.
    - *Note*: If you move all of your txt files into the same directory as this program, you do not need the full path. You only need the file name. For example, `python UVVisCLI.py -f uvdata.txt` if and only if `uvdata.txt` is in the same folder as `UVVisCLI.py`.
    - **Remember that no directory or file can contain a space if you do a full path to the file.**
3. If you hit enter after typing step 2, a plot will be generated and placed in the same directory as the input file. The name is the same as the input file but with the word Plot added to the end. There is no automatic preview. Simply open the png and see the results.
    - *Note*: if you have multiple input files and elect for a combined plot (see below), the output of the combined plot is currently set to be the current directory with a generic name. This will need to be updated in post-processing.
4. If you need to change any settings, such as the y-axis, you will need to add in the flags as outlined below. For example, to change the y-axis maximum from 20000 to 5000, simply type `python UVVisCLI.py -f \path\to\file -u 5000` or `python UVVisCLI.py -f \path\to\file --ymax 4000`. 
5. Be aware that each time you run the same input file, it will automatically overwrite the output png to the most recent one. If you do not want that to happen, change the name of the previous run first. *future update, but not high priority*
6. Once the plot is to your liking, you can simply use the png however you want. Post-processing can be done like normal.
    - I currently have dpi set to 300, which is plenty for most purposes. You can change it if you want.
7. Happy plotting!

## Arguments

- `-f` or `--files` <span style = "color :red"> **Required**</span>
    - you must include the file name here. If it is not located in the same directory as `UVVisCLI.py`, you must put the full path. On Windows, right click on the file you want to process and click `Copy as path` or `Ctrl + shift + c`. You can leave the quotes when pasted. This argument can take one or more files to process. Separate files by a space only.
- `-x` or `--xmin`
    - x-axis minimum. Default value is 300. Do not include units.
- `-z` or `--xmax`
    - x axis maximum. Default value is 1000.
- `-y` or `--ymin`
    - y axis minimum. Default value is -100 (captures any noise from the baseline).
- `-u` or `--ymax`
    - y axis maximum. Default value is 20000. 
- `-c` or `--concentration`
    - The concentration of the solution in units of molar. Default value is 0.0001 M (0.1 mM). If you are specifying concentration for each file, make sure to enter the concentrations in the order of the files, otherwise it will not work. Separate concentrations by space only, no commas, tabs etc.
- `-b` or `--path-length`
    - The path length when used in Beer's Law calculations of the molar absorptivity. Default value is 1 cm. Do not include units.
- `-r` or `--colors`
    - The color of the plotted data. This does not change axes, only data. Separate colors by a space only.
    - example: `-r red orange yellow green`
    - Each individual plot will be plotted as red, which is hard coded. That can be changed if you dig through the code.
- `-p` or `--plot-true`
    - will plot a combined plot of all input files. Only need to input the flag, no options available.
- `-o` or `--overlay`
    - Specify the file name for the overlay plot. Can only be used if `-p` is also used.

#### Citations

- If you use this program to produce plots, it would be greatly appreciated to cite by including the github repository as a citation (https://github.com/BardenB/uv-vis-plot). Nothing else asked from me (to stay compliant with MIT I think). 
- Matplotlib requires citing, which can be found [here](https://matplotlib.org/stable/users/project/citing.html).
- pandas requires citing, which can be found [here](https://pandas.pydata.org/about/citing.html).

#### License

Assume MIT license for now, clarification and changes may come in the future if necessary. 

##### Known limitations
- If you have to overlay more than 8 spectra, the default colors ('Red', 'Blue', 'Green', 'Purple', 'Orange', 'Pink', 'Brown', 'Yellow') will repeat themselves. Automatic updating to an automatic gradient or shading or rainbow for time point studies, etc., will be updated if needed. Changing opacity is currently not supported either, and probably will not be unless absolutely necessary.
- Running the same input file will automatically overwrite any plots and data output files that may generate. I will work on a way to update that such that a number or something is added to the end of the file to prevent overwriting. This is not high priority. Just rename if you need to run multiple times.