import sys
import img2pdf
import os

pdfname = os.getenv("PDF_NAME", default="output")

filepath = sys.argv[1]
if os.path.isdir(filepath):
    with open(f"output/{pdfname}.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        if imgs:
            f.write(img2pdf.convert(imgs))
        else:
            print("No valid images found!")
elif os.path.isfile(filepath):
    if filepath.lower().endswith((".jpg", ".jpeg", ".png")):
        with open(f"output/{pdfname}.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath))
    else:
        print("Only image files (.jpg/.jpeg/.png) are supported!")
else:
    print("please input file or dir")
