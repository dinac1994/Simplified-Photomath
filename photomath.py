from flask import Flask, render_template, request
import numpy as np
import cv2
import urllib.request

app = Flask(__name__)

# PART ONE - HANDWRITTEN CHARACTER DETECTOR

def sort_characters(a, b):

  for i in range(0, a.shape[0] - 1):
    for j in range(i+1, a.shape[0]):
      if (b[i,0,0] > b[j,0,0]):
        temp1 = np.copy(b[i,:,:])
        temp2 = np.copy(a[i,:,:])
        b[i,:,:] = b[j,:,:]
        a[i,:,:] = a[j,:,:]
        b[j,:,:] = temp1
        a[j,:,:] = temp2
  
  return a, b

def character_detector(image):

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  _,thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV) 
  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

  cropped_images = np.zeros([len(contours), 45, 45]) 
  coordinates = np.zeros([len(contours), 2, 4])
  i = 0

  for contour in contours:
    [x,y,w,h] = cv2.boundingRect(contour)
    cropped_images[i,:,:] = cv2.resize(gray[y:y+h,x:x+w], dsize=(45, 45), interpolation=cv2.INTER_CUBIC)
    coordinates[i,:,:] = np.array([[x, x, x+w, x+w], [y, y+h, y, y+h]])
    i = i + 1
  
  sorted_cropped_images, sorted_coordinates = sort_characters(cropped_images, coordinates)
  return sorted_cropped_images, sorted_coordinates


# PART TWO - CLASSIFICATION FUNCTION

import tensorflow as tf
model = tf.keras.models.load_model("best_model_SavedModel_format")

def index_to_number(index):
    
    if index == 0: 
        return "("    
    elif index == 1: 
        return ")"
    elif index == 2:
        return "+"
    elif index == 3:
        return "-"
    elif index == 4:
        return "0"
    elif index == 5:
        return "1"
    elif index == 6:
        return "2"
    elif index == 7:
        return "3"
    elif index == 8:
        return "4"
    elif index == 9:
        return "5"
    elif index == 10:
        return "6"
    elif index == 11:
        return "7"
    elif index == 12:
        return "8"
    elif index == 13:
        return "9"
    elif index == 14:
        return "*"


def classification_function(image):
  image /= 255
  image = np.reshape(image, (1, 45, 45, 1))
  pred = model.predict(image)[0]
  index = np.argsort(pred)
  index = index[-1]
  character_predict = index_to_number(index)
  return character_predict


# PART THREE - EVALUATION FUNCTION

from math import floor, trunc
class Solution:
   def solve(self, s):
      s = list(s[::-1])

      def get_value():
         sign = 1
         if s and s[-1] == "-":
            s.pop()
            sign = -1
         value = 0
         while s and s[-1].isdigit():
            value *= 10
            value += int(s.pop())
         return sign * value

      def get_term():
         term = get_value()
         while s and s[-1] in "*/":
            op = s.pop()
            value = get_value()
            if op == "*":
               term *= value
            else:
               term = 1.0 * term / value
         return term

      ans = get_term()
      while s:
         op, term = s.pop(), get_term()
         if op == "+":
            ans += term
         else:
            ans -= term
      return ans


def evaluate_expr(ch_string):

    i = 0
    while i <= len(ch_string):
        index_zadnji = 0
        index_prvi = 0
        podstring = ""
        ind = 0
        j = 0
        if (i < len(ch_string)):
            if (ch_string[i] == ')'):
                index_zadnji = i
                j = i
                while (ch_string[j] != '('):
                    j = j - 1
        
                index_prvi = j
                podstring = ch_string[index_prvi+1:index_zadnji]
                podstring = Solution().solve(podstring)
                ch_string = ch_string.replace(ch_string[index_prvi:index_zadnji+1], str(podstring))
                i = 0
                ind = 1
             
        if (ind == 0):
            i = i + 1

    return Solution().solve(ch_string)


# PART FOUR - A PHOTOMATH FUNCTION (ONE TO RULE THEM ALL)
def photomath(image):
  images, im_coord = character_detector(image)
  for i in range(0, len(images)):
    if i == 0:
      ch_string = ""
    character = classification_function(images[i,:,:])
    ch_string = ch_string + character
  solution = evaluate_expr(ch_string)
  return solution



@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)
		p = photomath(cv2.imread(img_path))

	return render_template("index.html", prediction = p, img_path = img_path)

if __name__ =='__main__':
	#app.debug = True
	app.run(port=3000, debug = False)
