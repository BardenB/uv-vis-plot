""" Welcome to the UV-Vis CLI plotter. This CLI will intake any number of files and produce
individual plots, as well as a combined plot of all input files.

This code can be assumed to be under the MIT license until further clarification is provided. 
If you use this program to produce any plots for publication, it would be appreciated to 
cite the GitHub repository (https://github.com/BardenB/uv-vis-plot) as well as Matplotlib 
and pandas (see readme for their links to citations). While I cannot force you to cite this
repository and still fall under MIT, matplotlib and pandas do require citations for use (I
think, it's at least highly encouraged).

There will be updates as needed as issues arise. 

copyright 2023 Brett Barden
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (StrMethodFormatter,AutoLocator)
import argparse

# CLI implementation section.
parser = argparse.ArgumentParser(
    description="Plot UV-Vis spectra from raw data from OceanView.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prog = 'UVVis',
    epilog = 'Thank you for using %(prog)s. Please contact Brett with any questions.',
    allow_abbrev= False
)

parser.add_argument(
    '-v',
    '--version',
    action = 'version',
    version = '%(prog)s 0.3.0',
)

parser.add_argument(
    '-f' ,
    '--files',
    nargs = '+',
    default = 'UVTestdata.txt',
    type = str,
    help = 'Choose file to plot.',
    required = True,
)

parser.add_argument(
    '-x',
    '--xmin',
    default = 300,
    type = float,
    help = 'x-axis minimum',
    required = False
)

parser.add_argument(
    '-z',
    '--xmax',
    default = 1000,
    type = float,
    help = 'x-axis maximum',
    required = False
)

parser.add_argument(
    '-y',
    '--ymin',
    default = -100,
    type = float,
    help = 'y-axis minimum',
    required = False
)

parser.add_argument(
    '-u',
    '--ymax',
    default = 20000,
    type = float,
    help = 'y-axis maximum',
    required = False
)

parser.add_argument(
    '-c',
    '--concentration',
    default = 0.0001,
    nargs = '+',
    type = float,
    help = 'concentration in units of molar',
    required = False
)

parser.add_argument(
    '-b',
    '--path-length',
    default = 1,
    type = float,
    help = 'path length in units of cm',
    required = False
)

parser.add_argument(
     '-r', #letter chosen by the one and only Leah.
     '--colors',
     default = ['Red','Blue','Green','Purple','Yellow','Pink','Brown', 'Orange'],
     nargs = '+',
     help = 'choose your colors.',
     required = False
)

parser.add_argument(
    '-p',
    '--plot-true',
    action = 'store_true',
    help='Combine all input files into one plot.',
    required=False,
)

parser.add_argument(
    '-o',
    '--overlay',
    default = "OverlayPlot.png",
    help = 'Specify the file name for the overlay plot.',
    required = False,
)

args = parser.parse_args()

# Updating fonts in all aspects of the plot.

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'
plt.rcParams['font.family'] ='Arial'
plt.rcParams['font.weight'] = 'bold'

colorList = ['Red', 'Blue', 'Green', 'Purple', 'Orange', 'Pink', 'Brown', 'Yellow']

# Starting the processing of data.
for index, txtFile in enumerate(args.files):
    if args.concentration != 0.0001:
        concentration = args.concentration[index]
    else:
        concentration = args.concentration
    csvFile = txtFile[:-4] + '.csv'
    plotName = txtFile[:-4] + 'Plot.png'

# Copying values from OceanView results in an extra column, it is removed here.
    df = pd.read_csv(txtFile, delimiter='\t', skiprows=1)
    df.drop(columns=['Unnamed: 2'], inplace=True)
    df.columns = ['wavelength', 'absorbance']

# Calculations of Molar Absorptivity automatically, no need to do it in excel.
    df['MolarAbsorptivity'] = df['absorbance'].apply(lambda x: x/(concentration*args.path_length))

# This section will automatically plot each individual file as its own plot.
# Note that there is no title, that can be added if you want but is most likely 
# to be added in as a section header in the SI or figure caption in a paper.
    plt.figure()
    plt.scatter(df['wavelength'], df['MolarAbsorptivity'], color='Red', s=2)
    plt.plot(df['wavelength'], df['MolarAbsorptivity'], '-', color='Red', linewidth=3)
    plt.xlim(args.xmin, args.xmax)
    plt.ylim(args.ymin, args.ymax)
    ax = plt.gca()
    ax.xaxis.set_major_locator(AutoLocator())
    ax.yaxis.set_major_locator(AutoLocator())
    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))
    ax.yaxis.set_label_text(r'Molar Absorptivity ($\mathrm{{cm^{-1} M^{-1}}}$)', size = 12, weight = 'bold')
    ax.xaxis.set_label_text(r'Wavelength(nm)', size = 12, weight = 'bold')
    for axis in ['top', 'right']:
        ax.spines[axis].set_visible(False)
    plt.savefig(plotName, format='png', dpi=300, bbox_inches='tight')
    plt.close()

# This section plots all input files together overlayed on top of each other.
# Current limitations: Each must have the same concentration. It cannot handle multiple
# concentrations right now. Which is rather unfortunate.
if args.plot_true:
    plt.figure()
    for index, (txtFile, color) in enumerate(zip(args.files, args.colors or colorList)):
        if args.concentration != 0.0001:
            concentration = args.concentration[index]
        else:
            concentration = args.concentration
        df = pd.read_csv(txtFile, delimiter='\t', skiprows=1)
        df.drop(columns=['Unnamed: 2'], inplace=True)
        df.columns = ['wavelength', 'absorbance']

        df['MolarAbsorptivity'] = df['absorbance'].apply(lambda x: x/(concentration*args.path_length))
        plt.scatter(df['wavelength'], df['MolarAbsorptivity'], color=color, s=2)
        plt.plot(df['wavelength'], df['MolarAbsorptivity'], '-', color=color, linewidth=3)
    plt.xlim(args.xmin, args.xmax)
    plt.ylim(args.ymin, args.ymax)
    ax = plt.gca()
    ax.xaxis.set_major_locator(AutoLocator())
    ax.yaxis.set_major_locator(AutoLocator())
    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))
    ax.yaxis.set_label_text(r'Molar Absorptivity ($\mathrm{{cm^{-1} M^{-1}}}$)', size = 12, weight = 'bold')
    ax.xaxis.set_label_text(r'Wavelength (nm)', size = 12, weight = 'bold')
    for axis in ['top', 'right']:
        ax.spines[axis].set_visible(False)
# The savefig section here will currently output the overlay plot to the current directory,
# but that can be changed based on the --overlay flag..
    plt.savefig(args.overlay, format='png', dpi=300, bbox_inches='tight')
    plt.close()
