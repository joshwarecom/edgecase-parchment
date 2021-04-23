# edgecase-parchment

This is a simple Inform 7 project bundled with the following:
- A slightly modified version of Parchment with some css files added to the manifest, and the ability to record and download a local transcript of the gaming session added.
- A script (edgecase-parchment.py, tested on Windows 10 with python 3.9) that applies the steps necessary to publish library.z5 (a PunyInform Z5 sample game) with the Parchment interpreter and successfully play it.  It runs the compilers and fixes some files.

# to execute
- Drop "Edgecase Parchment.inform" and "Edgecase Parchment.materials" into your Inform 7 Projects directory
- You may need to modify the paths at the top of the script to match your Inform 7 directories
- If you don't want the download-transcript feature to be applied and some errors in the HTML files addressed, set secret_sauce to 0
- Cross your fingers and run edgecase-parchment.py from the command shell.

# To Publish A Different Z File:
- replace library.z5 with your desired Z file
- update the source of the inform project to reference the name of your desired z-file, instead of "library.z5"

# acknowledgements
Most of the work contained herein was done by individuals much better at this than me, for detailed citation of sources, see:
/Edgecase%20Parchment.materials/Templates/Edgecase%20Parchment/acknowledgements.txt
