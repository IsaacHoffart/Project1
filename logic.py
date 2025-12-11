from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Sets up the initial appearance of the application and allows the events that happen
        when a button is pressed to occur.
        """
        super().__init__()
        self.setupUi(self)

        self.score_1_label.setVisible(False)
        self.score_2_label.setVisible(False)
        self.score_3_label.setVisible(False)
        self.score_4_label.setVisible(False)
        self.score_1_input.setVisible(False)
        self.score_2_input.setVisible(False)
        self.score_3_input.setVisible(False)
        self.score_4_input.setVisible(False)
        self.response_label_name.setVisible(False)
        self.response_label_number.setVisible(False)
        self.score_response_label_1.setVisible(False)
        self.score_response_label_2.setVisible(False)
        self.score_response_label_3.setVisible(False)
        self.score_response_label_4.setVisible(False)
        self.response_label.setVisible(False)

        self.button_save.setVisible(False)

        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_save.clicked.connect(lambda: self.save())

    def submit(self) -> None:
        """
        Accepts the name of the student and the number of attempts they did. Also causes 1 to 4
        input boxes to appear depending on the number of attempts.
        """

        if self.response_label.isVisible():
            self.response_label.setVisible(False)

        name = self.input_name.text().strip()
        if name == "":
            self.response_label_name.setVisible(True)
            return
        else:
            self.response_label_name.setVisible(False)


        try:
            attempts = int(self.input_num.text().strip())
            if attempts <= 0 or attempts > 4:
                raise ValueError
            else:
                self.response_label_number.setVisible(False)
        except ValueError:
            self.response_label_number.setVisible(True)
            return

        if attempts == 1:
            self.score_1_label.setVisible(True)
            self.score_2_label.setVisible(False)
            self.score_3_label.setVisible(False)
            self.score_4_label.setVisible(False)
            self.score_1_input.setVisible(True)
            self.score_2_input.setVisible(False)
            self.score_3_input.setVisible(False)
            self.score_4_input.setVisible(False)
            self.button_save.setVisible(True)
        elif attempts == 2:
            self.score_1_label.setVisible(True)
            self.score_2_label.setVisible(True)
            self.score_3_label.setVisible(False)
            self.score_4_label.setVisible(False)
            self.score_1_input.setVisible(True)
            self.score_2_input.setVisible(True)
            self.score_3_input.setVisible(False)
            self.score_4_input.setVisible(False)
            self.button_save.setVisible(True)
        elif attempts == 3:
            self.score_1_label.setVisible(True)
            self.score_2_label.setVisible(True)
            self.score_3_label.setVisible(True)
            self.score_4_label.setVisible(False)
            self.score_1_input.setVisible(True)
            self.score_2_input.setVisible(True)
            self.score_3_input.setVisible(True)
            self.score_4_input.setVisible(False)
            self.button_save.setVisible(True)
        else:
            self.score_1_label.setVisible(True)
            self.score_2_label.setVisible(True)
            self.score_3_label.setVisible(True)
            self.score_4_label.setVisible(True)
            self.score_1_input.setVisible(True)
            self.score_2_input.setVisible(True)
            self.score_3_input.setVisible(True)
            self.score_4_input.setVisible(True)
            self.button_save.setVisible(True)

    def save(self) -> None:
        """
        Accepts the scores the student got based on the number of attempts they did.
        The function then writes the data from itself and the submit function to a csv file
        along with a final grade.
        """
        scores = [0, 0, 0, 0]
        if self.score_1_input.isVisible():
            try:
                first_score = int(self.score_1_input.text().strip())
                if first_score < 0 or first_score > 100:
                    raise ValueError
                else:
                    self.score_response_label_1.setVisible(False)
                    scores[0] = first_score
            except ValueError:
                self.score_response_label_1.setVisible(True)
                return

        if self.score_2_input.isVisible():
            try:
                second_score = int(self.score_2_input.text().strip())
                if second_score < 0 or second_score > 100:
                    raise ValueError
                else:
                    self.score_response_label_2.setVisible(False)
                    scores[1] = second_score
            except ValueError:
                self.score_response_label_2.setVisible(True)
                return

        if self.score_3_input.isVisible():
            try:
                third_score = int(self.score_3_input.text().strip())
                if third_score < 0 or third_score > 100:
                    raise ValueError
                else:
                    self.score_response_label_3.setVisible(False)
                    scores[2] = third_score
            except ValueError:
                self.score_response_label_3.setVisible(True)
                return

        if self.score_4_input.isVisible():
            try:
                fourth_score = int(self.score_4_input.text().strip())
                if fourth_score < 0 or fourth_score > 100:
                    raise ValueError
                else:
                    self.score_response_label_4.setVisible(False)
                    scores[3] = fourth_score
            except ValueError:
                self.score_response_label_4.setVisible(True)
                return

        name = self.input_name.text().strip()

        with open('grades.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow([name, scores[0], scores[1], scores[2], scores[3], max(scores)])

        self.response_label.setVisible(True)

