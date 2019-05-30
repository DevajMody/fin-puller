# fin-puller
A Python project to pull company data from Yahoo Finance and save as .csv

companyCodes.csv is the list of all tickers that you want to pull data for.
Run index.py, which will save folders for all the companies.

If Yahoo Finance doesn't return data for a particular company, the folder will be deleted.

# Dependencies
finlib
https://github.com/harttraveller/finlib

# ToDo
Multithreading.
Better logging features.
