# File_search
//This Python script was created to allow to search any given file in a given directory for a given value{Either a file holding an array or single values} and then output the matching lines to a text file containing the name of the file you searched as well as the timestamp for when you searched.//

Place template in your Documents folder or adjust the values below to the file path you want
    
    #Array File path
        values_file = os.path.expanduser('~/Documents/File_search/Search/Array.txt')
        
    #Directory of files you'd like to search through
        resources_dir = os.path.expanduser('~/Documents/File_search/Resources')
        
    #Output Directory [Note: File name is output_{timestamp} and should remain that way if you'd like the timestamp to be           added to the file]
        output_dir = os.path.expanduser(f'~/Documents/File_search/Output/output_{timestamp}')

    
Make sure the .py is excuatable 
    
    Run in Terminal
    chmod +x /path/to/file/File_search.py
    
Ensure the correct libraries are installed
    
    pip install PyPDF2 openpyxl

If you have both Python 2 and Python 3 installed, you might need to use pip3 instead of pip to ensure that the libraries are installed for Python 3:


    pip3 install PyPDF2 openpyxl
