"""
Created on 2022-06-16

Authors: Poaq and P2
"""

#%%

########## INTENDED FILE STRCUTURE USAGE ##########

# . (os.getcwd())
# |-- Season1
# |   |-- Episode1.mkv
# |   |-- Episode2.mkv
# |   |-- Episode3.mkv
# |   |-- Episode4.mkv
# |-- Season2
# |   |-- Episode1.mov
# |   |-- Episode2.mov
# |   |-- Episode3.mov
# |   |-- Episode4.mov
# |-- Season3
# |   |-- Episode1.mp4
# |   |-- Episode2.mp4
# |   |-- Episode3.mp4
# |   |-- Episode4.mp4

########## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ##########

#%%
# import modules
# --------------- #

import argparse
import os

#%%
# Write argparser
# --------------- #

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description='Rename files for Plex',
        epilog= 'example: python3 renamePlex.py --name my.favorite.show --year 2000 --ext mkv'
        )
    parser.add_argument('--name', type = str,
                        help = 'name of show with periods, e.g. My.Favorite.Show',
                        required = True)
    parser.add_argument('--year', type = str,
                        help = 'year of show start',
                        required = True)
    parser.add_argument('--ext', type = str,
                        help = 'enter file extension',
                        required = True)
    args = parser.parse_args()


#%%
i = 1
for it in os.scandir(os.getcwd()):
    # if i > args.seasons: # this is unneeded if you are guaranteeing that all folders are season folders
    #     break
    if it.is_dir():
        # goes into season folder
        os.chdir(it.path)

        j = 1
        for file in os.listdir():
            # goes through all flies in the season folder
            
            if file.endswith(args.ext):
                episode_str = 'E' + str(j).zfill(2)
                season_str = 'S' + str(i).zfill(2)
                name = '.'.join([args.name, args.year, season_str, episode_str, args.ext])
                # print(name) # just to test
                os.rename(file, name)
                j += 1
        os.chdir('../')
        i += 1
    # else check next dir

    # indentions are dumb ways to end code lines

            
        
        
    







