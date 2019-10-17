import os
import sys

OS_PATH = os.path.dirname(__file__)
sys.path.insert(0, OS_PATH + "\\object_detection")
import model

if __name__ == '__main__':
  print("Test Start!!!!!!!")
  model.run_test()
  print("Test End!!!!!!!!!")