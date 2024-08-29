# This is a unittest for assignment 1 in IN5590
# Use it to make sure you submitted the correct
# files and format. Run from root dir in project
# with:
#   python src/test.py
import os
import unittest

class OutputTest(unittest.TestCase):
    def setUp(self):
        self.output_dir = "./output/"

    def test_files_exist(self):
        files = []
        for file in os.listdir(self.output_dir):
            if os.path.isfile(os.path.join(self.output_dir, file)):
                files.append(file)

        expected_files = ["1.gif", "2.png"]
        self.assertListEqual(sorted(files), expected_files)

    def test_output_size(self):
        output_size=0
        for file in os.listdir(self.output_dir):
            output_size += os.path.getsize(self.output_dir + file)
        self.assertLessEqual(output_size, 26000000)

if __name__ == '__main__':
    unittest.main()
