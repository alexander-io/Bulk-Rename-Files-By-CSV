# Alexander Harris, 1.13.20
# Bulk Rename Video Files According to CSV
#
# we have the task of naming video files according to their identifier
# for example a video named 0000.mp4 needs to be named overhead_press.mp4
# or a video named 0001.mp4 needs to be named squat.mp4
#
# assume the initial directory structure below,
# where the unnamed media is contained in './media_collection/',
# where there is an empty directory named './new_media_collection' which is the target for the renamed files
#
# .
# ├── media_collection
# │   ├── 000.mp4
# │   ├── 001.mp4
# │   └── 002.mp4
# ├── new_media_collection
# ├── table.csv
# └── x.py
#
# the table.csv file maps the old file identifiers to the new ones
# for each file/row in column A there is an absolute path to the video file yet to be named
#   for example : /home/claybeard/code/rename_videos/media_collection/000.mp4
# for each file/row in column B there is a new identifier for each filename that is space separated
#   for example : 'bench press'
#   for example : 'squat'
#
# running this script, x.py, will copy the file contents of media_collection and rename them according to the map defined in table.csv, the output looks something like the structure below :
#
# .
# ├── media_collection
# │   ├── 000.mp4
# │   ├── 001.mp4
# │   └── 002.mp4
# ├── new_media_collection
# │   ├── overhead_press.mp4
# │   ├── squat.mp4
# │   └── alternating_lounge.mp4
# ├── table.csv
# └── x.py




import os
import shutil
f=open("table.csv", "r") # read the csv
if f.mode == "r":
    contents =  f.read() # read
    csv = contents.split("\n") # split csv by columns, newline delimit
    for row in csv:
        if row!='':
            tuple = row.split(',') # split each row to array, comma separated : [old_path.ext, new_path]
            old_path = tuple[0]
            new_path = tuple[1]

            start_ext = old_path.find('.') # extract the extension
            end_ext = len(old_path)
            ext = old_path[start_ext:end_ext]

            new_path = new_path.split(' ') # the B colun names are space separated, split to array
            new_path = "_".join(new_path) # join them via underlines
            new_path_with_ext = new_path + ext # add extension onto new path

            shutil.copy(old_path,'./new_media_collection/'+new_path_with_ext) # copy to new_media_collection directory
            print(old_path +" -> "+ new_path_with_ext)
