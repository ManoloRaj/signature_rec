import cv2
import numpy as np
from pdf2image import convert_from_path
import os



def list_pdfs_in_directory(directory_path):

    pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
    return pdf_files


def pdfToImage(pdf_path):
    # Convertir le PDF en image
    pil_images = convert_from_path(pdf_path)
    pil_image = pil_images[0]  # prend la première image, qui est la seule image si le PDF a une seule page

    # Convertir l'image PIL en image OpenCV
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    return image


def saveAllImage():
    liste_image_pdf = list_pdfs_in_directory("training/training_set_pdf")

    for i in liste_image_pdf : 
        print(i)
        image = pdfToImage("training/training_set_pdf/"+i)

        cv2.imshow("image", image)
        cv2.imwrite("training/training_set_image/" + i + ".jpg", image)



def extraction() :
    # Load image and HSV color threshold
    # image = cv2.imread('./image_test/test.jpg')

    adresse = "image_test/CarteGrise_598024_photo_69bbe38a-0b98-4bdf-8909-718a73b0e175.pdf"
    image = pdfToImage(adresse)

    width = int(image.shape[1] * 0.1)
    height = int(image.shape[0] * 0.1)

    # Redimensionner l'image
    image = cv2.resize(image, (width, height))

    
    while True:
        cv2.imshow('image', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            
            break

# extraction()