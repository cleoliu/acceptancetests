import cv2
from os import path
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


class PicOpenCV:
    @classmethod
    def classify_gray_hist(cls, image1, image2, size = (256,256)):
        image1 = cv2.resize(image1, size)
        image2 = cv2.resize(image2, size)
        hist1 = cv2.calcHist([image1], [0], None, [256], [0.0,255.0])
        hist2 = cv2.calcHist([image2], [0], None, [256], [0.0,255.0])
        plt.plot(range(256), hist1,'r')
        plt.plot(range(256), hist2,'b')
        plt.show()
        degree = 0
        for i in range(len(hist1)):
            if hist1[i] != hist2[i]:
                degree = degree + (1 - abs(hist1[i]- hist2[i])/ max(hist1[i], hist2[i]))
            else:
                degree = degree + 1
        degree = degree/ len(hist1)
        return degree

    @classmethod
    def calculate(cls, image1, image2):
        hist1 = cv2.calcHist([image1], [0], None, [256], [0.0,255.0])
        hist2 = cv2.calcHist([image2], [0], None, [256], [0.0,255.0])
        degree = 0
        for i in range(len(hist1)):
            if hist1[i] != hist2[i]:
                degree = degree + (1 - abs(hist1[i]- hist2[i])/ max(hist1[i], hist2[i]))
            else:
                degree = degree + 1
        degree = degree/ len(hist1)
        return degree

    @classmethod
    def classify_hist_with_split(cls, image1, image2, size = (256,256)):
        image1 = cv2.resize(image1, size)
        image2 = cv2.resize(image2, size)
        sub_image1 = cv2.split(image1)
        sub_image2 = cv2.split(image2)
        sub_data = 0
        for im1,im2 in zip(sub_image1, sub_image2):
            sub_data += cls.calculate(im1, im2)
        sub_data = sub_data/3
        return sub_data

    @classmethod
    def classify_aHash(cls, image1, image2):
        image1 = cv2.resize(image1, (8,8))
        image2 = cv2.resize(image2, (8,8))
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        hash1 = cls._getHash(gray1)
        hash2 = cls._getHash(gray2)
        return cls._Hamming_distance(hash1, hash2)

    @classmethod
    def classify_pHash(cls, image1, image2):
        image1 = cv2.resize(image1, (32,32))
        image2 = cv2.resize(image2, (32,32))
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
        dct1 = cv2.dct(np.float32(gray1))
        dct2 = cv2.dct(np.float32(gray2))
        dct1_roi = dct1[0:8,0:8]
        dct2_roi = dct2[0:8,0:8]
        hash1 = cls._getHash(dct1_roi)
        hash2 = cls._getHash(dct2_roi)
        return cls._Hamming_distance(hash1, hash2)

    def _getHash(image):
        avreage = np.mean(image)
        hash = []
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if image[i,j] > avreage:
                    hash.append(1)
                else:
                    hash.append(0)
        return hash

    def _Hamming_distance(hash1, hash2):
        num = 0
        for index in range(len(hash1)):
            if hash1[index] != hash2[index]:
                num += 1
        return num

    @classmethod
    def cut_image(cls, target_path, saved_path, cut_size):
        img = cv2.imread(target_path)
        height, width, _ = img.shape
        # up_height:down_height , left_width:right_width
        clp = img[cut_size[0]:cut_size[1], cut_size[2]:cut_size[3]]
        cv2.imwrite(saved_path, clp)

    @classmethod
    def verify_file_image(cls, screenshot_path, expected_path):
        img1 = cv2.imread(screenshot_path)
        img2 = cv2.imread(expected_path)
        degree = cls.classify_hist_with_split(img1, img2)
        #judge img like value
        if degree >= 0.7 and degree <= 1:
            return True
        else:
            return False

    @classmethod
    def crop_image(cls, source_image, output_image):
        source_image, output_image = path.abspath(source_image), path.abspath(output_image)
        im = Image.open(source_image)
        # print("W{0}px,H{1}px".format(im.size[0],im.size[1]))
        y = round(im.size[1] * 0.05)  # cut 5%
        region = im.crop((0, int(y), im.size[0], im.size[1] - int(y)))
        region.save(output_image)
