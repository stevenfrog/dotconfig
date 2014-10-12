#! /usr/bin/python

import unittest
import copyDiffFiles


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #def test_usage(self):
        #CopyDiffFiles.copyDiffFiles.usage()
        #self.assetEqual(1, 2, 'need same')

    def test_retriveFilenames(self):
        dir1 = '/home/stevenfrog/temp/Hestia_Enhancement2'
        dir2 = '/home/stevenfrog/temp/hestia_enhan2'
        ins = copyDiffFiles.CopyDiffFiles()
        ins.copydifffiles(dir1, dir2)
        self.assertEqual(1, 1, 'need same')


if __name__ == '__main__':
    unittest.main()
