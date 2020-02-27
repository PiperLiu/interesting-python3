# #######################################################################
# # Copyright (C)                                                       #
# # 2020 Hongjia Liu(piperliu@qq.com)                                   #
# # Permission given to modify the code as long as you keep this        #
# # declaration at the top                                              #
# #######################################################################

import imageio
import os

# DURATION time each png owns
DURATION = 0.5

if __name__ == "__main__":
    # path init
    path = os.path.join(__file__, "..")
    # read pngs
    file_list = os.listdir(path)
    png_list = file_list.copy()
    for file in file_list:
        if file[-4:]!=".png":
            png_list.remove(file)
    png_list.sort(key=lambda x: int(x[:-4]))
    # now all the pngs are in the png_list
    # and sorted well from min to max
    # turn pngs into a gif file
    frames = []
    for png in png_list:
        # get the png file's path
        image_path = os.path.join(path, png)
        # imageio.imread() to get RGB matrix
        # frames is a list which stores the pngs in order
        frames.append(imageio.imread(image_path))
    # production path
    gif_path = os.path.join(path, "my_gif.gif")
    imageio.mimsave(gif_path, frames, 'GIF', duration=DURATION)
    print("done")
    pass
