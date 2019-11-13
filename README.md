# PDFmergeCMD
PDF Merge utility using command line arguments and the PyPDF2 library

This is a Python script that I created with the intent to compile a windows EXE.
Windows languages that drive the data manipulation that feeds this utility.
By using the command line arguments, a batch file or a shell command can launch the utility on a machine that does not have python installed. 
The first argument is the newly python created merged PDF file. 
Additional arguments are merged in order as passed. 
The theoretical limit of source PDFs is based on absolute vs relative path, and command line buffer limit.

Potential future optimizations:
-Switch to a log file library as opposed to opening a text file
-Allow the first file to be an existing file appending the folowing files into it, instead of a new file.
-Improved validation of the argument data, checking for existing files.
-Improved exception handling for file operations.
