# edgecase-parchment

This is a simple Inform 7 project bundled with the following:
- A slightly modified version of Parchment with some css files added to the manifest, and the ability to record and download a local transcript of the gaming session added.
- A script (edgecase-parchment.py, tested on Windows 10 with python 3.9) that applies the steps necessary to publish library.z5 (a PunyInform Z5 sample game) with the Parchment interpreter and successfully play it.  It runs the compilers and fixes some files.

# To Use A Different Z File:
- replace library.z5 with your desired Z file
- update the source of the inform project to reference the name of your desired z-file, instead of "library.z5"
