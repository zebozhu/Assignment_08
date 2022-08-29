#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Zebo Zhu, 27AUG2022, added code to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
lstInventory = []
class CD:
    """Stores data about a CD:
    
    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    @property
    def cd_id(self):
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = int(value)
        
    @property    
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = str(value)
    
    @property 
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = str(value)


class DataProcessor:
    @staticmethod
    def add_song(newSong): 
        """Function to load user input data to a dictionary in a list

        Args:
            newSong (Tuple): A tuple of the user inputs (ID, CD, Artist Name)

        Returns:
            lstInventory: 2D data structure (list of CD objects) that holds the data during runtime
        """
        # intID = int(strID)
        dicRow = {'ID': newSong[0], 'Title': newSong[1], 'Artist': newSong[2]}
        lstInventory.append(dicRow)
        return lstInventory
           


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name,lstInventory):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D list of objects

        Args:
            file_name (string): name of file used to read the data from
            lstInventory: 2D data structure (list of CD objects) that holds the data during runtime
        Returns:
            lstInventory.
        """
        try:
            lstInventory.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                lstInventory.append(dicRow)
            objFile.close()
            
        except FileNotFoundError:
            print('Erro!! There\'s no such file exist in the current directory, please check again!')
    @staticmethod
    def save_inventory(file_name, lstInventory):
        """Function to write data from a list of dictionaries to a file

        Reads the data from a 2D list of objects to a file identified by file_name

        Args:
            file_name (string): name of file used to read the data from
            lstInventory: 2D data structure (list of CD objects) that holds the data during runtime

        Returns:
            lstInventory.
        """
        objFile = open(file_name, 'w')
        for row in lstInventory:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    @staticmethod
    def show_inventory(CDObjLst):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in CDObjLst:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    @staticmethod
    def new_song(strID, strTitle, strArtist):
        """Prompt user to enter a new song


        Args:
            strID (string): ID number of the song
            strTitle (string): Title of the song
            stArtist (string): Artist of the song

        Returns:
            strID (string): ID number of the song
            strTitle (string): Title of the song
            stArtist (string): Artist of the song


        """
        try:
            strID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
            return strID, strTitle, strArtist
        except ValueError:
            print('Error!! Please enter an integer!')
            
# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
objFile = open(strFileName,'w+')
objFile.close()
FileIO.load_inventory(strFileName, lstOfCDObjects)

while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # Process menu selection
    # process exit first
    if strChoice == 'x':
        break
    # process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            try: 
                FileIO.load_inventory(strFileName, lstOfCDObjects)
            except:
                print('File does not exist, please check the file name!')
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID = ''
        strTitle =''
        strArtist =''
        newSong = IO.new_song(strID, strTitle, strArtist)

        # 3.3.2 Add item to the table
        DataProcessor.add_song(newSong)
        print('New song has been successfully added to the inventory')
        # IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstInventory)
        continue  # start loop back at top.
    # process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstInventory)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            print()
            print('writing data to file...')
            try: 
                FileIO.save_inventory(strFileName, lstInventory)
            except:
                print('Invalid file name or table, please check and re-enter!')
            IO.show_inventory(lstInventory)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

