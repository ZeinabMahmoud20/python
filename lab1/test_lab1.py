from vowel import extractVowel
from index import displayIndex
from calcArea import calcArea
from mulTable import mulTable
from dictionary import sortDict
import unittest

class TestLabOne(unittest.TestCase):
    def test_vowel(self):
        # self.assertEqual(task_two_ibrahem('This is javaScript','i'), [2,5,15])
        self.assertEqual(extractVowel('ZainaB'),'ZnB')
        self.assertEqual(extractVowel('ZAINAB'),'ZNB')
        self.assertEqual(extractVowel('zainab'),'znb')
    def test_displayIndex(self):
        self.assertEqual(displayIndex('Hello to iti','o'),[4,7])
        self.assertEqual(displayIndex('Hello to iti','i'),[9,11])
    def test_calcArea(self):
        self.assertEqual(calcArea('t',5,10),25)
        self.assertEqual(calcArea('T',5,10),25)
        self.assertEqual(calcArea('r',5,10),50)
        self.assertEqual(calcArea('R',5,10),50)
        self.assertEqual(calcArea('c',10,1),314.1592653589793)
        self.assertEqual(calcArea('C',10,1),314.1592653589793)
        self.assertEqual(calcArea('s',10,1),100)
        self.assertEqual(calcArea('S',10,1),100)
    def test_mulTable(self):
        self.assertEqual(mulTable(2),[[1],[2,4]])
        self.assertEqual(mulTable(3),[[1],[2,4],[3,6,9]])
    def test_sortDict(self):
        ls={"Alaa","Mona","Zainab"}
        ls2={'Z': ['Zainab'], 'M': ['Mona'], 'A': ['Alaa']}
        self.assertEqual(sortDict(ls),ls2)
if __name__ == '__main__':
    unittest.main()
