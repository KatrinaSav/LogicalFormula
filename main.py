###############################################################################
#Лабораторная работа №1 по дисциплине Логические основы интеллектуальных систем
#Выполнила студентка группы 021702 БГУИР Савинская Екатерина Сергеевна
#Проверить является ли формула КНФ
#Последние изменения: 27.02.2023


def is_formula(str):  #проверяет строку по синтаксису формулы
    if str == "":
        return False
    if str[0] == '(' and str[len(str) -1] == ")":  #проверка на наличие внешних скобок
        str = str[1:-1]                            #опускание внешних скобок
        count = 0                                  #счётчик вложенности
        for i in range(len(str)):
            if str[i] == "(":
                count += 1
            elif str[i] == ")":
                count -= 1
            elif count == 0:
                try:
                    if str[i] == "!":
                        return is_formula(str[i+1:])     #рекурсивный вызов для операнда унарной операции
                    elif str[i] == '~':
                        return is_formula(str[0:i]) and is_formula(str[i+1:])    #рекурсивный вызов для операнда бинарной операции
                    elif check_operator(str[i:i+2]):                             #проверка на оператор состоящий из двух символов
                        return is_formula(str[0:i]) and is_formula(str[i + 2:])  #рекурсивный вызов для операнда бинарной операции
                    else:
                        continue
                except Exception:
                    return False
        return False
    else:
        return correct_symbol(str)  #проверка является ли символ допустимым


def check_operator(symbols): #определяет является ли строка допустимым оператором
    operations = ['->', '/\\', '\\/']
    if symbols in operations:
        return True
    else:
        return False


def correct_symbol(str):                       #определяет является ли символ допустимым
    alphabit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #список допустимых символов
    if len(str) > 1:
        return False
    elif str in alphabit:
        return True


def process_str(str):  #убирает один уровень вложенности
    if str[0] == '(' and str[len(str) -1] == ")":
        return str[1:-1]
    else:
        return str


def split_bi_opr(str):  #разбивает операцию на операнды и оператор
    count = 0           #счётчик для проверки вложенности
    for i in range(len(str)):
        if str[i] == '(':
            count +=1
        if str[i] == ')':
            count -=1
        if str[i] == '~' and count == 0:
            return str[0:i], str[i+1:], str[i]    #возвращает первый, второй операнд и оператор
        if (str[i] == '\\' or str[i] == '/' or str[i] == '-') and count == 0:
            return str[0:i], str[i + 2:], str[i:i+2]
        if str[i] == '!' and count == 0:
            return str[i+1:], "", str[i]

def is_oper(str):  #определяет является ли строка операцией
    if '~' in str or '->' in str or '\\/' in str or '/\\' in str or "!" in str:
        return True
    else:
        return False


class Formula:  #класс для представления формулы
    def __init__(self, str):
        self.first = ""          #первый операнд
        self.second = ""         #второй операнд
        self.operator = ""       #оператор
        body = process_str(str)  #получение строки без внешних скобок
        if is_oper(body):
            self.first, self.second, self.operator = split_bi_opr(body)   #разбиение строки
        else:
            self.first = body
        if is_oper(self.first):
            self.first = Formula(self.first)    #рекурсивный вызов для первого операнда
        if is_oper(self.second) and self.operator != '!':
            self.second = Formula(self.second)  #рекурсивный вызов для второго операнда


def is_knf(form):                #определяет является ли формула кнф
    if is_formula(form):         #проверка является ли строка формулой
        formula = Formula(form)  #создание экземпляра класса формулы
    else:
        return False
    if formula.operator == "":
        return True
    if formula.operator == "\/":
        return disjunction(formula)
    if formula.operator != "/\\" and formula.second != "":   #проверка внешнего оператора на конъюнкцию
        return False
    return tree_traversal(formula)  #проверка на кнф путём обхода дерева


def tree_traversal(formula):  #обход дерева разбора формулы
    if type(formula) == str:
        return True
    elif formula.operator == '/\\':
        return tree_traversal(formula.first) and tree_traversal(formula.second)  #рекурсивный вызов для двух потомков
    elif formula.operator == '!':
        return check_no(formula)
    elif formula.operator == '->' or formula.operator == '~':  #проверка на недопустимые в кнф операторы
        return False
    elif formula.operator == '\\/':
        return disjunction(formula)  #рекурсивный вызов для двух потомков

                                                                                                                # и проверка вложенности дизъюнкции
def check_no(formula):
    if type(formula.first) != str:  # проверка на вложенность оператора логическое отрицание
        return False
    else:
        return True


def disjunction(formula):   #проверка дизъюнкции на вложенные операции
    first = False
    second = False
    if type(formula.first) != str:
        if formula.first.operator == '\/':
            first = disjunction(formula.first)
        if formula.first.operator == '!':
            first = check_no(formula.first)
    else:
        first = True
    if type(formula.second) != str:
        if formula.second.operator == '\/':
            second = disjunction(formula.second)
        if formula.second.operator == '!' :

            second = check_no(formula.second)
    else:
        second = True
    return first and second


if __name__ == '__main__':
    while True:
        formula = str(input("Введите формулу "))
        print(is_knf(formula))


