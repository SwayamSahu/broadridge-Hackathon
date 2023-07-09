import re
from pdfminer.high_level import extract_pages,extract_text

import fitz # PyMuPDF
import PIL.Image
import io
# for page_layout in extract_pages("sample.pdf"):
#     for element in page_layout:
#         print(element)

d =int(input("Enter 0 for pdf text or 1 for image in pdf"))

if d == 0:
    text = extract_text("sample.pdf")
    print(text)
    pattern = re.compile(r"[a-zA-z]+,{1}\s{1}")
    matches = pattern.findall(text)
    names= [n[:-2] for n in matches]
    print(names)

elif d==1:
    pdf=fitz.open("sample.pdf")
    counter =1
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_img = pdf.extract_image(image[0])
            image_data = base_img["image"]
            img =PIL.Image.open(io.BytesIO(image_data))
            extension = base_img["ext"]
            img.save(open(f"image{counter}.{extension}","wb"))
            counter += 1



# import tabula
# tables = tabula.read_pdf("sample.pdf",pages="all")
# print(tables[0])