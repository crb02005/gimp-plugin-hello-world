#!/usr/bin/env python

# adapted from https://gimpbook.com/scripting/gimp-script-templates/helloworld.py
# Hello World in GIMP Python

from gimpfu import *

def hello_world(initstr, font, size, color, drop_color, background_color) :

    # Make a new image. Size 10x10 for now -- we'll resize later.
    img = gimp.Image(1, 1, RGB)

    # Save the current foreground color:
    pdb.gimp_context_push()


    # Set the text color
    gimp.set_foreground(drop_color)

    drop_size = int(size // 16)
    drop_blur_size = int(size // 8)

    # Create a new text layer (-1 for the layer means create a new layer)
    drop_layer = pdb.gimp_text_fontname(img, None, drop_size, drop_size, initstr, 10,
                                   True, size, PIXELS, font)

    layer_name = pdb.gimp_item_get_name(drop_layer)
    pdb.gimp_item_set_name(drop_layer, layer_name+" Dropshadow")
    pdb.plug_in_gauss(img, drop_layer, drop_blur_size, drop_blur_size, 0)
    gimp.displays_flush()

    # Set the text color
    gimp.set_foreground(color)

    # Create a new text layer (-1 for the layer means create a new layer)
    layer = pdb.gimp_text_fontname(img, None, 0, 0, initstr, 10,
                                   True, size, PIXELS, font)

    # Resize the image to the size of the layer
    img.resize(layer.width, layer.height, 0, 0)

    # Background layer.
    # Can't add this first because we don't know the size of the text layer.
    background = gimp.Layer(img, "Background", layer.width, layer.height,
                            RGB_IMAGE, 100, NORMAL_MODE)

    gimp.set_background(background_color)
    background.fill(BACKGROUND_FILL)
    img.add_layer(background, 2)

    # Create a new image window
    gimp.Display(img)
    # Show the new image window
    gimp.displays_flush()

    # Restore the foreground and background color:
    pdb.gimp_context_pop()


register(
    "python_fu_hello_world",
    "Hello world image",
    "Create a new image with your text string",
    "Carl",
    "Burks",
    "2023",
    "Hello world (Py)...",
    "",      # Create a new image, don't work on an existing one
    [
        (PF_STRING, "string", "Text string", 'Hello, world!'),
        (PF_FONT, "font", "Font face", "Sans"),
        (PF_SPINNER, "size", "Font size", 50, (1, 3000, 1)),
        (PF_COLOR, "color", "Text color", (0.0, 0.0, 0.0)),
        (PF_COLOR, "drop_color", "Drop Shadow Color", (0.5, 0.5, 0.5)),
        (PF_COLOR, "background_color", "Background Color", (1.0, 1.0, 1.0)),
    ],
    [],
    hello_world, menu="<Image>/File/Create")

main()