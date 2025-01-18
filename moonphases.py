from PIL import Image


def get_moon_phase_image(percent):
    img_path = "images/moonphases/wi-moon-full.png"
    if percent > 0.95 or percent <= 0.07:
        img_path = "images/moonphases/wi-moon-new.png"
    elif percent > 0.07 and percent <= 0.19:
        img_path = "images/moonphases/wi-moon-waxing-crescent.png"
    elif percent > 0.19 and percent <= 0.31:
        img_path = "images/moonphases/wi-moon-first-quarter.png"
    elif percent > 0.31 and percent <= 0.44:
        img_path = "images/moonphases/wi-moon-waxing-gibbous.png"
    elif percent > 0.44 and percent < 0.56:
        img_path = "images/moonphases/wi-moon-full.png"
    elif percent > 0.56 and percent <= 0.68:
        img_path = "images/moonphases/wi-moon-waning-gibbous.png"
    elif percent > 0.68 and percent <= 0.80:
        img_path = "images/moonphases/wi-moon-third-quarter.png"
    elif percent > 0.80 and percent <= 0.95:
        img_path = "images/moonphases/wi-moon-waning-crescent.png"
    img = Image.open(img_path, "r")
    # print(percent, img_path)
    return img
