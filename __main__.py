from PIL import Image
from colorama import Fore
from colorama import Style
import matplotlib.pyplot as plt
import pytesseract
import imutils
import cv2
import os

IMAGE_WIDTH = 733
IMAGE_HEIGHT = 1304

def get_questions():
    plt.ion()

    image_raw = cv2.imread("sample_screenshots/arcade_fire.png")
    image_scaled = imutils.resize(image_raw, height=IMAGE_HEIGHT)

    image_scaled = cv2.cvtColor(image_scaled, cv2.COLOR_BGR2GRAY)
    _, image_scaled = cv2.threshold(image_scaled, 200, 230, cv2.THRESH_BINARY)

    question = image_scaled[195:500, 30:700]
    answer0 = image_scaled[525:650, 30:700]
    answer1 = image_scaled[650:750, 30:700]
    answer2 = image_scaled[750:875, 30:700]

    cv2.imwrite("question.png", question)
    cv2.imwrite("answer0.png", answer0)
    cv2.imwrite("answer1.png", answer1)
    cv2.imwrite("answer2.png", answer2)

    question_text = pytesseract.image_to_string(Image.open("question.png")).replace("\n", " ")
    answer0_text = pytesseract.image_to_string(Image.open("answer0.png")).replace("\n", " ")
    answer1_text = pytesseract.image_to_string(Image.open("answer1.png")).replace("\n", " ")
    answer2_text = pytesseract.image_to_string(Image.open("answer2.png")).replace("\n", " ")

    os.remove("question.png")
    os.remove("answer0.png")
    os.remove("answer1.png")
    os.remove("answer2.png")

    print(f'{Fore.GREEN}' + question_text + f'{Style.RESET_ALL}')
    print(answer0_text)
    print(answer1_text)
    print(answer2_text)

    plt.imshow(image_scaled)
    plt.show(block=True)

get_questions()
