# XKCD-Archiver
Command-line utility that automagically scrapes xkcd.com for every xkcd, ever. Yes, that's 1533 (as of this writing) downloads per full archival. Run this on your USB if you want to slowly whittle away its shelf life.

Written one night while drunk, bored and thinking "Yo, we know how to write code. Why haven't we done any shit? Let's hack some shit together.

# Usage
## Storage
Downloads to XKCD Archive folder.

Naming scheme: 'number - stripname.fileformat'

## Command-line Syntax

> python XKCD.py X Y

X - Starting strip

Y - Ending strip

If X is less than 1, it defaults to one

If Y is greater than the current strip, it defaults to the current strip

# Known Issues
- Title text not archived anywhere. Not an issue of scrapability, but in what format would be appropriate
- #681 - Gravity Wells is small version, text not readable
- #802 - Online Communities #2 is small version, text not readable
- #826 - Guest Comic (SMBC) does not let user click the exhibits
- #980 - Money is small version, text not readable
- #1000 - 1000 Comics is small version, individual characters not visible
- #1037 - Umwelt only downloads one of the possible strips (although that might be the point)
- #1040 - Lakes and Oceans is small version, text not readable
- #1071 - Exoplanets is small version, text not readable
- #1079 - United Shapes is small version
- #1080 - Visual Field is small version, text not readable
- #1110 - Click and Drag only contains frame, not full map
- #1127 - Congress is small version, text not readable
- #1190 - Time only downloads the last frame out of the entire collection
- #1196 - Subways is small version
- #1256 - Questions is small version
- #1298 - Exoplanet Neighbourhood is small version
- #1331 - Frequency only downloads the unlit frame
- #1335 - Now only represents the image as first downloaded and ignores all 23 other permutations
- #1350 - Lorenz is not archived, as it's permalink is the same for #1349 and thus is skipped
- #1389 - Surface Area is small version
- #1392 - Dominant Players is small version
- #1446 - Landing only downloads the first frame of the flipbook
- #1491 - Stories of the Past and Future is small version
