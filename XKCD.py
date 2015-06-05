from bs4 import BeautifulSoup
import os, wget, urllib, urllib.request, sys

# The directory in which XKCD's comic images are stored
directory = '//imgs.xkcd.com/comics/'

def current_strip():
    # Makes a soup of the XKCD main page
    main_url = 'http://www.xkcd.com/'
    main_page = BeautifulSoup(urllib.request.urlopen(main_url))

    # Gets link of previous day's strip
    link = main_page.find(rel='prev')
    # Returns the number of the current day's strip
    return int(link.get('href')[1:-1]) + 1


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

    if os.path.exists('XKCD Archive'):
        pass
    else:
        os.mkdir('XKCD Archive')

    archive_directory = 'XKCD Archive/'

    
    # Loops from starting strip to ending strip
    for count in range(lower_bound, upper_bound + 1):
        # Exception for XKCD #404
        if count == 404:
            file = open(archive_directory + '404 - Item Not Found', mode='w').close()

        # Exception for XKCD #1331
        elif count == 1331:
            # Checks if the strip is already downloaded
            # if the strip is, notifies user and iterates loop
            # if the strip is not, downloads and renames
            if os.path.exists('frequency.png') or os.path.exists(archive_directory + '1331 - Frequency.png'):
                print('1331 ALREADY DOWNLOADED')
                continue
            else:
                wget.download('http://imgs.xkcd.com/comics/frequency.png')
                os.rename('frequency.png', archive_directory + '1331 - Frequency.png')
                print('\n 1331 - Frequency')

        # Exception for XKCD #1416
        elif count == 1416:
            # Checks if the strip is already downloaded
            # if the strip is, notifies user and iterates loop
            # if the strip is not, downloads and renames
            if os.path.exists('pixels.png') or os.path.exists(archive_directory + '1416 - Pixels.png'):
                print('1416 ALREADY DOWNLOADED')
                continue
            else:
                wget.download('http://imgs.xkcd.com/comics/pixels.png')
                os.rename('pixels.png', archive_directory + '1416 - Pixels.png')
                print('\n 1416 - Pixels')

        # Exception for XKCD #1525
        elif count == 1525:
            # Checks if the strip is already downloaded
            # if the strip is, notifies user and iterates loop
            # if the strip is not, downloads and renames
            if os.path.exists('emojic_8_ball.png') or os.path.exists(archive_directory + '1525 - Emojic 8-Ball.png'):
                print('1525 ALREADY DOWNLOADED')
                continue
            else:
                wget.download('http://imgs.xkcd.com/comics/emojic_8_ball.png')
                os.rename('emojic_8_ball.png', archive_directory + '1525 - Emojic 8-Ball.png')
                print('\n 1525 - Emojic 8-Ball')
        
        else:
            # Sets url to the current strip in the loop
            url = 'http://www.xkcd.com/' + str(count)
            # Makes a soup of the current strip's page
            source = BeautifulSoup(urllib.request.urlopen(url))

            # For loop through every image on the current strip's page
            for link in source.find_all('img'):
                # Checks if image is stored in the comic directory
                # i.e. if the image is an XKCD strip or not
                if directory in str(link):
                    # Tries to download the strip. If it fails,
                    # writes the current strip to the error file
                    try:
                        # The permalink to the strip
                        image_link = 'http:' + link.get('src')
                        # The filename for the strip in the online directory
                        file_name = link.get('src')[23:]

                        # Gets the name of the strip, filtering out any invalid
                        # characters for Windows filenaming conventions
                        strip_title = ''.join(filter(lambda x: x not in '\/:*?"<>|', str(source.find('title'))[13:-8]))

                        
                        # Checks if the strip is already downloaded
                        # if the strip is, notifies user and iterates loop
                        # if the strip is not, downloads and renames
                        if os.path.exists(file_name) or os.path.exists(archive_directory + str(count) + ' - ' + strip_title + file_name[-4:]):
                            print(str(count) + ' ALREADY DOWNLOADED')
                            continue
                        else:
                            wget.download(image_link)
                            os.rename(file_name, archive_directory + str(count) + ' - ' + strip_title + file_name[-4:])
                            print('\n' + str(count) + ' - ' + strip_title)
                    except:
                        error_file = open(archive_directory + 'errors.txt', mode='a')
                        error_file.write(str(count) + ' - Failed \n')
                        error_file.close()


archiver(sys.argv[1], sys.argv[2])
