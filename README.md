# JPGtoPNGConverter
Python3.8 learning project for working with Pillow to convert JPGs to PNGs

Does not work with Python 2.x

# Requirements
Need to install Pillow

python3.8 pip3 install pillow

# Run it

JPG2PNGConverter.py takes two arguments 
-> first is the folder with your JPG files (other filetypes are allowed to be present, getting filtered)
-> second is the folder where you want to put your converted files

Sample JPG files are located in "Pokedex" folder

In your terminal, fire

on Windows
python JPG2PNGConverter.py Pokedex\ PathToConvertedFiles\

on Linux/Max
python3.8 JPG2PNGConverter.py Pokedex/ PathToConvertedFiles/

# Troubleshooting

If pillow is simultaniously with PIL you might get an error.
You can try to uninstall & reinstall pillow again

python3.8 -m pip uninstall pillow
python3.8 -m pip install pillow

Worked for me when testing the code on my linux machine, after creating it on Windows
