# File_search
//This Python script was created to allow to search any given file in a given directory for a given value{Either a file holding an array or single values} and then output the matching lines to a text file containing the name of the file you searched as well as the timestamp for when you searched.//

Place template in your Documents folder
    
    You can adjust the file path's if needed
    #Array File path
        values_file = os.path.expanduser('~/Documents/File_search/Search/Array.txt')
    #Directory of files you'd like to search through
        resources_dir = os.path.expanduser('~/Documents/File_search/Resources')
    #Output Directory [Note: File name is output_{timestamp} and should remain that way if you'd like the timestamp to be           added to the file]
        output_dir = os.path.expanduser(f'~/Documents/File_search/Output/output_{timestamp}')

    
Make sure the .py is excuatable 
    
    Run in Terminal
    chmod +x /path/to/file/File_search.py
    

    
