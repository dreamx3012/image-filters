import unittest
import cv2
from img_transformer.image_operator import ImageOperator

class TestFilters(unittest.TestCase):

    def setUp(self):
        pass

    def test(self)
        IO = ImageOperator()
        IO.image('../imgs/horror.jpg')
        source_img = IO.im
        IO.image('../imgs/amelie.jpg')
        matching_img = IO.im
        img = IO.histogram_matching(source_img, matching_img)
        cv2.imshow('image', img)
        cv2.waitKey(0)


if __name__ == '__main__':
    unittest.main()
