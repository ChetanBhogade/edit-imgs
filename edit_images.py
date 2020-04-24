import os
from PIL import Image, ImageOps, ImageDraw, ImageFont


def calculate_border(img):
    width, height = img.size 
    ans = int((width+height)/2) 
    pixel_dist = int(len(str(ans))/2)
    border = int(str(ans)[:pixel_dist])*3  # 2
    return border


def add_border(img, output_image_path):
    # img = Image.open(input_image_path)
    border = calculate_border(img=img)
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill='white')
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    bimg.save(output_image_path)


def add_watermark(source_img_path, destination_img_path):
    # get an image
    base = Image.open(source_img_path).convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # calculations
    width, height = base.size
    font_size = (height//10)//2
    # get a points to draw at
    points = (width - (font_size*7.5), height-(font_size*1.5))

    # get a font
    fnt = ImageFont.truetype(r'photos\Courgette\Courgette-Regular.ttf', font_size)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text(points, "@_bnw_imgs_", font=fnt, fill=(255,255,255,128))
    # draw text, full opacity
    # d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

    out = Image.alpha_composite(base, txt)

    # conver img to RGB to save as jpg
    new_img = out.convert('RGB')

    # new_img.save(destination_img_path)
    return new_img


def edit_mulitple_images(source_dir_path, destination_dir_path):
    source_imgs = os.listdir(source_dir_path)

    for index, filename in enumerate(source_imgs):
        _name, extension = filename.split('.')
        src_img_path = os.path.join(source_dir_path, filename)
        output_img_path = os.path.join(destination_dir_path, f'output{index}.{extension}')
        watermark_image = add_watermark(src_img_path, src_img_path)
        add_border(watermark_image, output_img_path)
        print(f"Image : output{index}.{extension} edited successfully.")





source_dir_path = r'C:\Users\CHETAN BHOGADE\Desktop\IOT\Chetan\PythonScript\Images'
destination_dir_path = r'C:\Users\CHETAN BHOGADE\Desktop\IOT\Chetan\PythonScript\outputs'



if __name__ == "__main__":
    edit_mulitple_images(source_dir_path, destination_dir_path)



# website names : 
# 1) unsplash.com/
# 2) www.pexels.com/