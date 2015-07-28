# XKCD-Archiver
Command-line utility that automagically scrapes xkcd.com for every xkcd, ever. Yes, that's 1535 (as of this writing) downloads per full archival. Run this on your USB if you want to slowly whittle away its shelf life.

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
- XKCD.py writes every strip to the errors.txt file, including those which have downloaded without error
- #826 - Guest Comic (SMBC) does not let user click the exhibits
- #980 - Money is small version, text not readable
- #1037 - Umwelt only downloads one of the possible strips (although that might be the point)
- #1110 - Click and Drag only contains frame, not full map
- #1190 - Time only downloads the last frame out of the entire collection
- #1331 - Frequency only downloads the unlit frame
- #1335 - Now only represents the image as first downloaded and ignores all 23 other permutations
- #1350 - Lorenz is not archived, as it's permalink is the same for #1349 and thus is skipped
- #1446 - Landing only downloads the first frame of the flipbook
