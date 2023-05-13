from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from memo___app import app
from memo___data import *
from memo___main_layout import *
from memo___card_layout import *
from memo___edit_layout import txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3

######################################              Константы:              #############################################
main_width, main_height = 1000, 450 # начальные размеры главного окна
card_width, card_height = 600, 500 # начальные размеры окна "карточка"
time_unit = 1000    # столько длится одна единица времени из тех, на которые нужно засыпать 
                    # (в рабочей версии программы увеличить в 60 раз!)

######################################          Глобальные переменные:      #############################################
questions_listmodel = QuestionListModel() # список вопросов
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3) # запоминаем, что в форме редактирования вопроса с чем связано
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] # список виджетов, который надо перемешивать (для случайного размещения ответов)
frm_card = 0 # здесь будет связываться вопрос с формой теста
timer = QTimer() # таймер для возможности "уснуть" на время и проснуться
win_card = QWidget() # окно карточки
win_main = QWidget() # окно редактирования вопросов, основное в программе

######################################             Тестовые данные:         #############################################
def testlist():
    
    frm = Question('Яблоко', 'apple', 'application', 'pinapple', 'apply')
    questions_listmodel.form_list.append(frm)
    frm = Question('Дом', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question('Мышь', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)
