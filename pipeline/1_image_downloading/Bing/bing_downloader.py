'''
Downloads multiple images from Bing. Uses the Bulk Bing Image Downloader from
https://github.com/ostrolucky/Bulk-Bing-Image-downloader

Arguments
items - The list of items to grab images from. Use underscores instead of spaces, because this will become the folder name those images will go into
transparent - True or False, if you want transparent backgrounds or not
limit - The higher the number, the more images you'll get. The number you insert is the MAXIMUM amount of images you might get per item.

Images will output to the downloads foler in their respective folder names.

We download the Bulk Bing Image Downloader in this script to prevent copy/pasting someone else's code in our repo.
'''

import os
import wget

'''
Items include:
'aerosol_cans_full', 'aluminium_foil', 'ammunition', 'auto_parts', 'batteries', 'bicycles', 'cables', 'cardboard', 'cartridge', 'cassette', 'cd_cases', 'cigarettes', 'cooking_oil', 'cookware', 'corks', 'crayons', 'digital_cameras', 'desktop_computers', 'discs', 'doors', 'eyeglasses', 'fabrics', 'fire_extinguishers', 'floppy_disks', 'furniture', 'game_consoles', 'generic_plastic', 'gift_bags', 'glass', 'glass_container', 'green_waste', 'hard_drives', 'hardware', 'hazardous_fluid', 'heaters', 'laptop_computers', 'large_appliance', 'lightbulb', 'medication_containers', 'medications', 'metal_cans', 'mixed_paper', 'mobile_device', 'monitors', 'nail_polish', 'oil_filters', 'paint', 'paint_thinner', 'pallets', 'paper_cups', 'pet_waste', 'plastic_cards', 'printers', 'propane_tanks', 'shoes', 'small_appliances', 'smoke_detectors', 'tires', 'tools', 'toothbrushes', 'toothpaste_tubes', 'toy', 'vehicles', 'water_filters', 'wood', 'wrapper'
'''
items = ['nuts_and_bolts', 'corks', 'cardboard', 'pet_waste', 'toy']
transparent = True
limit = 30

# Download the Bulk Bing Image Downloader if it doesn't exist in the system
if os.path.exists('./bbid.py'):
    pass
else:
    print('bbid.py not found. Downloading...')
    url = 'https://raw.githubusercontent.com/ostrolucky/Bulk-Bing-Image-downloader/6ab4c76b3f3c6bd9636ab547364765330eb48ad2/bbid.py'
    wget.download(url, './bbid.py')

# Create the folder names in the downloads folder
for item in items:
    if not os.path.exists('./downloads/'+item):
        os.makedirs('./downloads/'+item)

# Create an array of all the object names, replacing underscores with spaces
itemNames = [item.replace("_", " ") for item in items]

# Run bbid.py depending on your parameters
for x in range(0, len(items)):
    if transparent:
        os.system("python bbid.py -s '" + itemNames[x] + "' -o './downloads/" + items[x] + "' --limit " + str(limit) + " --filters +filterui:photo-transparent+filterui:photo-photo")
    else:
        os.system("python bbid.py -s '" + itemNames[x] + "' -o './downloads/" + items[x] + "' --limit " + str(limit) + " --filters +filterui:photo-photo")