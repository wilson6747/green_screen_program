from PIL import Image

#Variables for beach
beach_image = Image.open('beach.jpg')
beach_pixels = beach_image.load()

#variables for cactus
cactus_image = Image.open('cactus.jpg')
cactus_pixels = cactus_image.load()
print(cactus_pixels[100,100])

#combined pic
combined_image = Image.new('RGB', beach_image.size)
combined_pixels = combined_image.load()

#loops, Picture is 800 * 600
for x in range(0, 800):
    for y in range(0,600):
        #beach
        (rb, gb, bb) = beach_pixels[x, y]
        red_beach = rb
        green_beach = gb
        blue_beach = bb
        #cactus
        (rc, gc, bc) = cactus_pixels[x, y]
        red_cactus = rc
        green_cactus = gc
        blue_cactus = bc
        #combined
        (red, green, blue) = combined_pixels[x,y]
        red_combo = red
        blue_combo = blue
        green_combo = green
        #color assignment
        if red_cactus < 180 and green_cactus > 200 and blue_cactus < 200:
            red_combo = red_beach
            green_combo = green_beach
            blue_combo = blue_beach
        else:
            red_combo = red_cactus
            blue_combo = blue_cactus
            green_combo = green_cactus
            combined_pixels[x,y] = cactus_pixels[x,y]       
            
        combined_pixels[x, y] = (red_combo ,green_combo , blue_combo)
combined_image.show()