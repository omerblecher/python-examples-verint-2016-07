#Unit test that checks image file format
import unittest

#Define the exception class
class InvalidImageExt(Exception):
    def __init__(self, msg):
        super(InvalidImageExt, self).__init__(msg)

class ImageFile (object):
    
    #All image file extensions
    extensions = {"BMP", "GIF", "IMG", "JBG", "JPE", "JPEG", "JPG", "PBM", "PCD", "PCX", "PCT", "PGM", "PNG", "PPM", "PSD", "TIFF", "TIF"}

    #Constructor
    def __init__(self, fileName):
        fileExtension = fileName.split(".")[1]
        if not fileExtension.upper() in ImageFile.extensions:
            raise InvalidImageExt("File name %s doesn't end with any image file suffix" % (fileName))

#Unit test class
class TestImageFile(unittest.TestCase):
    def test_good_ext(self):
        try:
            img = ImageFile("file.png")
        except InvalidImageExt:
            self.fail("png should be a valid file extension")

    def test_bad_ext(self):
        with self.assertRaises(InvalidImageExt):
            img = ImageFile("file.mp3")

unittest.main()