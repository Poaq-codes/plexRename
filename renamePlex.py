"""
Created on 2022-06-16

Authors: Poaq and P2
"""
#%%
# Potential upgrades pseudocode
# --------------------------- #

# clean up counter implementation


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
        epilog= 'example: python3 renamePlex.py --name my.favorite.show.year'
        )
    parser.add_argument('--name', type = str,
                        help = 'name of show (year optional) with periods, e.g. My.Favorite.Show.2020',
                        required = True),
    parser.add_argument('--lang', type = str,
                        help = 'language code for subtitle files (optional argument)')
    args = parser.parse_args()

#%%
# Functions
# --------------- #

def rename_episode(file, season, episode):
    episode_str = 'E' + str(episode).zfill(2)
    season_str = 'S' + str(season).zfill(2)
    
    # print('{}.{}{}{}'.format(
    #     args.name, season_str, episode_str, os.path.splitext(file)[1])
    #     )
    os.rename(file, '{}.{}{}{}'.format(
        args.name, season_str, episode_str, os.path.splitext(file)[1])
        )
    return None
        
def rename_subtitle(file, season, episode, language):
    episode_str = 'E' + str(episode).zfill(2)
    season_str = 'S' + str(season).zfill(2)
    
    os.rename(file, '{}.{}{}.{}{}'.format(
        args.name, season_str, episode_str, language, os.path.splitext(file)[1])
        )
    return None    

#%%
# Rename folders
# --------------- #

q = 1
for it in os.scandir(os.getcwd()):
    if it.is_dir():
        new_name = 'Season ' + str(q).zfill(2)
        # print(new_name)
        os.rename(it, new_name)
        q += 1
     # else do nothing

#%%
# Rename episodes and subs
# ---------------------- #

# Set up valid file extensions -- include subtitles
valid_extensions = ['.mkv', '.mp4', '.mov']
sub_extensions = ['.srt']
# print(valid_extensions)

# Begin renaming loop
i = 1
for it in os.scandir(os.getcwd()):
    # find subdirectories in current directory

    if it.is_dir():
        # goes into season folder
        os.chdir(it.path)

        j = 1
        k = 1
        for file in os.listdir():
            # print(os.path.splitext(file)[1])
            # goes through all files in folder
            
            if os.path.splitext(file)[1] in valid_extensions:
                # only select files with valid extensions
                
                rename_episode(file, i, j)
                
                j += 1
            # else skip file
                
            if os.path.splitext(file)[1] in sub_extensions:
                # only select sub files
                
                rename_subtitle(file, i, k, args.lang)
                
                k += 1
            # else skip the file
            
        os.chdir('../')
        i += 1
    # else check next dir


    # indentions are dumb ways to end code lines

            
        
        
    







