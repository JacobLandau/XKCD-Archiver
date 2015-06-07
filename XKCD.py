from bs4 import BeautifulSoup
import os, wget, urllib, urllib.request, sys, requests

# The directory in which XKCD's comic images are stored
directory = '//imgs.xkcd.com/comics/'

def current_strip():
    # Retrieves json for current strip
    # And converts it to a dictionary
    main_page = requests.get('https://www.xkcd.com/info.0.json')
    main_page.raise_for_status()
    strip = main_page.json()

    # Returns the number of the current day's strip
    return int(strip['num'])


def archiver(lower_bound, upper_bound):

    lower_bound, upper_bound = int(lower_bound), int(upper_bound)

    # Sets upper_bound equal to current strip
    # If user sets a strip that does not yet exist
    if upper_bound > current_strip():
        upper_bound = current_strip()
    # Sets lower_bound equal to 1
    # If lower_bound is less than 1
    if lower_bound < 1:
        lower_bound = 1

    # Creates the archive folder if it doesn't already exist
    if os.path.exists('XKCD Archive'):
        pass
    else:
        os.mkdir('XKCD Archive')

    archive_directory = './XKCD Archive/'

    
    # Loops from starting strip to ending strip
    for count in range(lower_bound, upper_bound + 1):
        # Exception for XKCD #404
        if count == 404:
            file = open(archive_directory + '404 - Item Not Found', mode='w').close()
        else:
            # Tries to retrieve the json for the current strip in the loop
            try:
                # Sets url for json to the current strip in the loop
                url = requests.get('http://www.xkcd.com/' + str(count) + '/info.0.json')
                url.raise_for_status()
                # Makes a dictionary of the current strip's json
                strip = url.json()

                # Gets the name of the strip, filtering out any characters
                # which are invalid for Windows filenaming conventions
                strip_title = ''.join(filter(lambda x: x not in '\/:*?"<>|', strip['title']))

                if strip['link'] != '':
                    # If the strip links to a large version
                    # We get the image link for the large version instead
                    # Using a temporary web scraper
                    if 'large' in strip['link']:
                        temp_soup = BeautifulSoup(urllib.request.urlopen(strip['link']))
                        link = temp_soup.img
                        image_link = link.get('src')
                else:
                    image_link = strip['img']

                # The file name will be the strip title plus the file extension as grabbed by the image link
                file_name = strip_title + image_link[-4:]
                           
                # Checks if the strip is already downloaded
                # if the strip is, notifies user and iterates loop
                # if the strip is not, downloads and renames
                if os.path.exists(file_name) or os.path.exists(archive_directory + str(count) + ' - ' + file_name):
                    print(str(count) + ' ALREADY DOWNLOADED')
                else:
                    wget.download(image_link)
                    os.rename(image_link[28:], archive_directory + str(count) + ' - ' + file_name)
                    print('\n' + str(count) + ' - ' + strip_title)

            # Runs if the system throws a UnicodeEncodeError, which will only happen
            # when it tries to print a unicode character to the console
            # In that case, we substitute the usual line printed to the console
            # for a cheeky, console-safe stand-in
            except UnicodeEncodeError:
                print('\n' + str(count) + ' - This title cannot be printed because unicode hates you.')

            # If another error happens, we simply have to write it to the errors.txt
            # file and move on with our lives
            else:
                error_file = open(archive_directory + 'errors.txt', mode='a')
                error_file.write(str(count) + ' - Failed \n')
                error_file.close()

archiver(sys.argv[1], sys.argv[2])
