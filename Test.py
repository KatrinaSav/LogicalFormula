###############################################################################
#Лабораторная работа №1 по дисциплине Логические основы интеллектуальных систем
#Выполнила студентка группы 021702 БГУИР Савинская Екатерина Сергеевна
#Тестирование функций на корректную работу
#Последние изменения: 27.02.2023

import unittest
from main import *

class Test(unittest.TestCase):
    def test_is_formula(self):
        self.assertEqual(is_formula("((A->B)~C)"), True)
        self.assertEqual(is_formula("((!A)/\\(B\\/C))"), True)
        self.assertEqual(is_formula("(B/\\C)"), True)
        self.assertEqual(is_formula("(!(B/\\C))"), True)
        self.assertEqual(is_formula("(A/\\(!B))"), True)
        self.assertEqual(is_formula("(A/\\(B\\/(D\\/E)))"), True)
        self.assertEqual(is_formula("((A/\\B)/\\C)"), True)
        self.assertEqual(is_formula("((!B)/\\(!C))"), True)
        self.assertEqual(is_formula("((A\\/B)/\\((-B)\\/C\\/D)/\\(D\\/E))"), False)
        self.assertEqual(is_formula("A"), True)
        self.assertEqual(is_formula("((A~B)/\\(C/\\D))"), True)
        self.assertEqual(is_formula("(((C/\\D))"), False)
        self.assertEqual(is_formula("1A"), False)
        self.assertEqual(is_formula("A1"), False)
        self.assertEqual(is_formula("(A->B)"), True)
        self.assertEqual(is_formula("((A\\/B)/\\(((!B)\\/(C\\/D))\\/(D\\/E)))"), True)
        self.assertEqual(is_formula("((((A\\/B)/\\(((!B)\\/(C\\/D))\\/(D\\/E)))\/((!A)->B))~C)"), True)

    def test_is_knf(self):
        self.assertEqual(is_knf("(!(!)"), False)
        self.assertEqual(is_knf("((!(!A))/\(B\/C))"), False)
        self.assertEqual(is_knf("(B/\C)"), True)
        self.assertEqual(is_knf("(!(B/\\C))"), False)
        self.assertEqual(is_knf("(A/\\(!B))"), True)
        self.assertEqual(is_knf("(A/\\(B\\/(D\\/E)))"), True)
        self.assertEqual(is_knf("(A/\\(B\\/(D/\\E)))"), False)
        self.assertEqual(is_knf("(B\\/E)"), True)
        self.assertEqual(is_knf("((X\\/R)\\/Q)"), True)
        self.assertEqual(is_knf("((A\\/B)/\\(((!B)\\/(C\\/D))/\\(D\\/E)))"), True)
        self.assertEqual(is_knf("((A\\/B)/\\(((!B)/\\(C\\/D))/\\(D\\/E)))"), True)
        self.assertEqual(is_knf("((A\\/B)/\\(((!B)\\/(C\\/D))\\/(D\\/E)))"), True)
        self.assertEqual(is_knf("(B~C)"), False)
        self.assertEqual(is_knf("((X\\/R)->Q)"), False)
        self.assertEqual(is_knf("(((1/\\0)/\\(Q/\\0))\\/(!B))"), False)

if __name__ == '__main__':
    unittest.main()
