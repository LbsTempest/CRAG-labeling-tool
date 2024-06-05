import datetime
import json
import re
from time import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from window import Ui_MainWindow


def clear_layout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clear_layout(item.layout())


def is_valid_number(string):
    pattern = r"^202\d{7}$"
    if re.match(pattern, string):
        return True
    else:
        return False


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.start_line_box.setRange(1, 2735)
        self.ui.end_line_box.setRange(1, 2735)

        self.ui.select_jsonl_button.clicked.connect(self.open_file)
        self.ui.confirm_button.clicked.connect(self.start_process)

        self.file_length = 0
        self.student_id = 0
        self.start_line = 0
        self.end_line = 0
        self.start_time = 0
        self.date_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        self.query = ""
        self.answer = ""
        self.response = {}
        self.text_list = []
        self.button_list = []
        self.relevant_sentences = []
        self.generator = None
        self.font = QtGui.QFont("Arial", 16)

    def start_process(self):
        if not self.ui.id_input.text() or not is_valid_number(self.ui.id_input.text()):
            self.ui.info_label.setText("Please input valid student ID!")
            return

        if not self.ui.jsonl_path_label.text():
            self.ui.info_label.setText("Please select a jsonl file!")
            return

        if self.start_line > self.end_line or self.start_line < 0 or self.end_line > self.file_length:
            self.ui.info_label.setText("Please input valid start and end line number!")

        self.generator = self.confirm()
        next(self.generator, None)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Jsonl Files (*.jsonl)")
        if file_name:
            self.ui.jsonl_path_label.setText(file_name)
            with open(file_name, 'r') as f:
                self.file_length = len(f.readlines())

    def confirm(self):
        self.student_id = self.ui.id_input.text()
        self.start_line = int(self.ui.start_line_box.text())
        self.end_line = int(self.ui.end_line_box.text())

        with open(self.ui.jsonl_path_label.text(), 'r') as f:
            lines = f.readlines()[self.start_line-1:self.end_line]
            for line in lines:
                self.show_single_line(line)
                yield

    def show_single_line(self, line):
        self.ui.is_sentences_correct.setChecked(False)
        line = json.loads(line)
        self.query: str = line["query"]
        self.answer: str = line["answer"]
        self.response: str = line["response"]

        clear_layout(self.ui.lines_layout)
        query_widget = QtWidgets.QLabel(f"Query: {self.query}")
        answer_widget = QtWidgets.QLabel(f"Answer: {self.answer}")
        query_widget.setFont(self.font)
        answer_widget.setFont(self.font)
        query_widget.setWordWrap(True)
        answer_widget.setWordWrap(True)

        self.ui.lines_layout.addWidget(query_widget)
        self.ui.lines_layout.addWidget(answer_widget)

        self.relevant_sentences: list[str] = []

        for toq_sen in self.response:
            if toq_sen["relevant_sentence"] is not None:
                self.relevant_sentences.extend(toq_sen["relevant_sentence"])

        self.text_list = []
        self.button_list = []
        layout_list = QtWidgets.QVBoxLayout()
        for i, sentence in enumerate(self.relevant_sentences):
            text_label = QtWidgets.QLabel(f"{i+1}: {sentence}")
            button = QtWidgets.QCheckBox()

            text_label.setFont(self.font)
            text_label.setWordWrap(True)

            single_sentence_layout = QtWidgets.QHBoxLayout()
            single_sentence_layout.addWidget(text_label)
            single_sentence_layout.addWidget(button)
            single_sentence_layout.setStretch(0, 100)
            single_sentence_layout.setStretch(1, 1)

            self.text_list.append(text_label)
            self.button_list.append(button)
            layout_list.addLayout(single_sentence_layout)

        layout_list.setSpacing(2)
        self.ui.lines_layout.addLayout(layout_list)
        self.ui.lines_layout.setStretch(0, 0)
        self.ui.lines_layout.setStretch(1, 0)
        # self.ui.lines_layout.setStretch(2, 10)
        self.ui.lines_layout.setStretch(2, len(layout_list))
        self.start_time = time()

    def save_info(self):
        time_spent = time() - self.start_time
        self.ui.info_label.setText(f"Time spent: {time_spent:.2f}s")
        save_file_name = f"{self.student_id}_{self.start_line}_{self.end_line}_{self.date_time}.jsonl"
        for items in self.response:
            items["is_relevant"] = []
        save_content = {
            "query": self.query,
            "answer": self.answer,
            "response": self.response,
            "is_sentence_relevant": [],
            "is_sentences_correct": self.ui.is_sentences_correct.isChecked(),
            "time_spent": time_spent
        }

        num_sentences = 0
        is_relevant = False

        for toq_sen in self.response:
            for _ in toq_sen["relevant_sentence"]:
                is_relevant = is_relevant or self.button_list[num_sentences].isChecked()
                num_sentences += 1
            save_content["is_sentence_relevant"].append(is_relevant)
            is_relevant = False

        with open(save_file_name, 'a') as f:
            f.write(json.dumps(save_content) + "\n")

        self.ui.info_label.setText(f"Save file: {save_file_name}")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

        if QtCore.Qt.Key_0 <= event.key() <= QtCore.Qt.Key_9:
            index = event.key() - QtCore.Qt.Key_0
            if index <= len(self.button_list):
                self.button_list[index-1].setChecked(not self.button_list[index-1].isChecked())

        if event.key() == QtCore.Qt.Key_R:
            self.ui.is_sentences_correct.setChecked(not self.ui.is_sentences_correct.isChecked())

        if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.save_info()
            if self.generator:
                try:
                    next(self.generator)
                except StopIteration:
                    self.generator = None
                    self.ui.info_label.setText("All lines have been processed!")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
