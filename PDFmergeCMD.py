"""
PDFmergeCMD

this script will take command line args to merge pdf files
"""
# importing required modules
# importing datetime module for now()
import os
import sys
import datetime
import contextlib
import argparse
import PyPDF2

def pdf_merge(pdfs, output):
    """
    processes the pdf merge
    """
    current_time = datetime.datetime.now()
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    #set the current directory so that excel shell will not use my documents    
    os.chdir(application_path)

    try:
        log_file = open("log_file.txt", "a")
        log_file.write("Starting pdf file merge: " + str(current_time) + "\n")
    except Exception:
        print ("Error opening Log File")


    # creating pdf file merger object
    with contextlib.ExitStack() as stack:
        pdf_merger = PyPDF2.PdfFileMerger()
        try:
            files = [stack.enter_context(open(pdf, 'rb')) for pdf in pdfs]
            log_file.write("Success Reading files!\n")
        except Exception:
            log_file.write("Error reading files!\n")
        for file_tmp in files:
            try:
                pdf_merger.append(file_tmp)
                log_file.write("Success Appending file: " + str(file_tmp) + "\n")
            except Exception:
                log_file.write("Error Appending file: " + str(file_tmp) + "\n")
        with open(output, 'wb') as file_tmp:
            try:
                pdf_merger.write(file_tmp)
                log_file.write("Success Writing merged file: " + str(file_tmp) + "\n")
            except Exception:
                log_file.write("Error Appending merged file: " + str(file_tmp) + "\n")
        log_file.close()


def main():
    """
    main function: read the commandline arguements then run the merge
    """
    # importing datetime module for now()
    # parse the command line
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("out", default="merged.pdf")
    arg_parser.add_argument("pdf", nargs="*", default=[])

    #create the parser
    args = arg_parser.parse_args()

    # calling pdf merge function
    pdf_merge(args.pdf, args.out)

# calling the main function
if __name__ == "__main__":
    # using now() to get current time
    main()
