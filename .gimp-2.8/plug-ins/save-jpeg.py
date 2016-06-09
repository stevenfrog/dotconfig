from gimpfu import pdb, main, register, PF_STRING
import os

QUALITY = 0.8
OUTPUT_PATH = "/home/stevenfrog/temp/mini-photo"


def gprint(text):
    """
    Like console print
    """

    pdb.gimp_message(text)
    return



def plugin_main(file):
    """
    Main plugin method
    """

    image = pdb.gimp_file_load(file, file)
    drawable = pdb.gimp_image_get_active_layer(image)

    fileabs = os.path.abspath(file)
    #gprint('=== Input ==== ' + fileabs)
    file_dir, filename = os.path.split(fileabs)
    filename = filename[:-4] + '.jpg'
    file_new = os.path.join(OUTPUT_PATH, filename)

    pdb.file_jpeg_save(image, drawable, file_new, file_new, QUALITY, 0, 1, 1, '', 0, 1, 0, 0)
    pdb.gimp_image_delete(image)

    gprint('=== Output === ' + file_new)



args = [(PF_STRING, 'file', 'Input file name', '')]
register(
    'python-save-jpeg',            # proc_name  The name of the command that you can call from the command line or from scripting
    'Save the image to jpeg',      # blurb      Information about the plug-in that displays in the procedure browser
    'Save the image to jpeg',      # help       Help for the plug-in
    'stevenfrog',                  # author     The plug-in's author
    'stevenfrog',                  # copyright  The copyright holder for the plug-in (usually the same as the author)
    '2016',                        # date       The copyright date
    '',                            # label      The label that the plug-in uses in the menu  (<Image>/Image/Save as jpeg)
    '',                            # imagetypes The types of images the plug-in is made to handle (RGB*, GRAY*)
    args,                          # params     The parameters for the plug-in's method
    [],                            # results    The results of the plug-in's method
    plugin_main                    # function   The name of the method to call in your Python code
)

main()
