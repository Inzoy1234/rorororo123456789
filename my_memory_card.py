from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []

q = Question('Что из этого НЕ является чудом света?', 'Эльфивая Башня', 'В. Китайская стена', 'Чичен-Ица', 'Пирамида Хиопса')
question_list.append(q)
q1 = Question('Какой век шёл в 1500-1599 годах?', '16 век', '14 век', '15 век',  '17 век')
question_list.append(q1)
q2 = Question('Сколько минут в сутках?', '1440 минут', '1370 минут',  '1500 минут', '1760 минут')
question_list.append(q2)
q3 = Question('Какой из этих годов был високосным?', '2008', '2000', '2006', '2014')
question_list.append(q3)
q4 = Question('Сколько Мегабайтов(MB) в 4 Террабайтов(TB)?', '4.194.304 MB', '419.430 MB',  '41.943 MB', '41.943.045 MB')
question_list.append(q4)
q5 = Question('Какой самый большой океан на земле?','Тихий', 'Атлантическимй', 'Индийский',  'Северный-Ледовитый')
question_list.append(q5) 
q6 = Question('Кто написал роман Война и Мир?', 'Лев Толстой', 'Фёдор Достоевский', 'Антон Чехов',  'Иван Тургенев')
question_list.append(q6)
q7 = Question('Какой город является столицей Японии?', 'Токио', 'Осака',  'Киото', 'Хиросима')
question_list.append(q7)
q8 = Question('В каком году люди высадились на луне?', '1969', '1965',  '1972', '1980')
question_list.append(q8)
q9 = Question('Кто был первым президентои США?', 'Джордж Вашингтон', 'Аврам Линкольн',  'Теодор Рузвельт', 'Франклин Рузвельт')
question_list.append(q9)

app = QApplication([]) 
main_win = QWidget()
main_win.setWindowTitle('Memory Card') 
text = QLabel('Что из этого НЕ является чудо света?')
RadioGroupBox = QGroupBox('Варианты ответов')
btn_answer1 = QRadioButton('В. Китайская Стена')
btn_answer2 = QRadioButton('Эльфивая Башня')
btn_answer3 = QRadioButton('Чичен-Ица')
btn_answer4 = QRadioButton('Пирамида Хиопса')

RadioGroup = QButtonGroup()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_answer1) 
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
button = QPushButton('Ответить')

AnsGroupBox = QGroupBox('Реезультат теста')
result = QLabel('праввильно/неправильно')
itog = QLabel('Эльфивая башня')
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog)
AnsGroupBox.setLayout(layout_res)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addWidget(button, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line = QVBoxLayout()
line.addLayout(line1)
line.addLayout(line2)
line.addLayout(line3)
main_win.setLayout(line) 

AnsGroupBox.hide()

def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def question_show(): #Панель с Вопросом и вариантами ответов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True) #Сбросить выбор кнопки

answer = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q: Question):
    shuffle(answer) #Метод для перемешивания списка
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    itog.setText(q.right_answer)
    question_show()



def show_correct(res):
    result.setText(res) 
    show_results()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика: \n Всего вопросов:', main_win.total, '\n Правильных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total * 100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)
def click_ok():
    if button.text()=='Ответить':
        check_answer()
    else:
        next_question()

        
main_win.score = 0
main_win.total = 0


main_win.cur_question = -1

next_question()
button.clicked.connect(click_ok)
main_win.show()
app.exec()