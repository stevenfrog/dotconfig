from gimpfu import pdb, main, register, PF_STRING
#from gimpenums import ORIENTATION_HORIZONTAL
import os

def flip(file):
    fileabs = os.path.abspath(file)
    print(fileabs)
    file_dir, filename = os.path.split(fileabs)
    filename = filename.lower().replace('.png', '_mini.jpg')
    file_new = os.path.join(file_dir, filename)

    image = pdb.gimp_file_load(file, file)
    drawable = pdb.gimp_image_get_active_layer(image)

    #pdb.gimp_image_flip(image, ORIENTATION_HORIZONTAL)
    #pdb.gimp_file_save(image, drawable, file_new, file_new)

    pdb.file_jpeg_save(image, drawable, file_new, file_new, 0.8, 0, 1, 1, '', 0, 1, 0, 0)
    pdb.gimp_image_delete(image)

args = [(PF_STRING, 'file', 'GlobPattern', '*.*')]
register('python-flip', '', '', '', '', '', '', '', args, [], flip)

main()
