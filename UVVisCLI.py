import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (StrMethodFormatter,AutoLocator)
import argparse


""" CLI implementation section.
Putting everything in one file to make it super easy for everyone involved.
"""
parser = argparse.ArgumentParser(
    description="Plot UV-Vis spectra from raw data from OceanView.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prog = 'UVVis',
    epilog = 'Thank you for using %(prog)s. Please contact with any questions.',
    allow_abbrev= False
)

parser.add_argument(
    '-v',
    '--version',
    action = 'version',
    version = '%(prog)s 0.1.0',
)

parser.add_argument(
    '-f' ,
    '--file',
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
     '--color',
     default = 'Red',
     help = 'choose your color',
     required = False
)
args = parser.parse_args()


"""Beginning code to plot the spectrum provided.
"""

plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'
plt.rcParams['font.family'] ='Arial'

"""Input file to be processed, this will convert txt file to csv and remove the first, unecessary line.
The way the files are stored as txt when you copy and paste the values from the UV-Vis, there is an
extra empty column at the end that needs to be removed. This takes care of that."""

txtFile = args.file
csvFile = txtFile[:-4]+'.csv'
plotName = txtFile[:-4]+'Plot.png'


def txt2csv(txtFile, csvFile):
    with open(txtFile, 'r')as fileone:
        with open(csvFile, 'w') as filetwo:
                material = fileone.readlines()[1:]
                filetwo.writelines(material)
                return csvFile

df = pd.read_csv(txt2csv(txtFile,csvFile), delimiter = '\t')
df.drop(columns=['Unnamed: 2'], inplace=True)
df.columns = ['wavelength', 'absorbance']

""" Calculate molar absorptivity as a function of absorbance divided by concentration.
This assume
"""

df['MolarAbsorptivity'] = df['absorbance'].apply(lambda x: x/(args.concentration*args.path_length))

"""Plotting wavelength as the x axis and molar absorptivity on the y axis.
Using molar absorptivity is more appropriate in most cases to compare across different 
concentrations and complexes.
Currently hard coded x axis is 300-1000 nm and y axis -100 to 4000. These can be changed.
Hopefully I can make this programmable as well."""

plot = plt.scatter(df['wavelength'], df['MolarAbsorptivity'], color = args.color, s = 2)
plt.plot(df['wavelength'], df['MolarAbsorptivity'], '-', color = args.color, linewidth = 3)
plt.xlim(args.xmin,args.xmax)
plt.ylim(args.ymin,args.ymax)

ax = plot.axes
ax.xaxis.set_major_locator(AutoLocator())
ax.yaxis.set_major_locator(AutoLocator())
plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))
ax.yaxis.set_label_text(r'Molar Absorptivity ($\mathrm{{cm^{-1} M^{-1}}}$)')
ax.xaxis.set_label_text(r'Wavelength(nm)')
for axis in ['top','right']:
    ax.spines[axis].set_visible(False)

plt.savefig(plotName, format = 'png', dpi = 300, bbox_inches='tight')