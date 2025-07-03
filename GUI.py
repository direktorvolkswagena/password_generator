from PyQt6.QtCore import Qt, QTimer, QFileInfo
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QWidget, QCheckBox, QVBoxLayout, QHBoxLayout, QLabel,
    QGroupBox, QPushButton, QLineEdit, QSlider, QApplication,
)

import logic


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        root = QFileInfo(__file__).absolutePath()
        self.setWindowIcon(QIcon(root + '/misc/pass_gen_logo.png'))
        self.setFixedSize(575, 250)
        self.setContentsMargins(20, 20, 20, 20)

        self.output = None
        self.generate_button = None
        self.copy_button = None
        self.length_slider = None
        self.result_label = None

        self.check_lower_case = None
        self.check_upper_case = None
        self.check_digits = None
        self.check_symbols = None

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.generator_panel())
        main_layout.addWidget(self.settings_panel())

    def generator_panel(self) -> QGroupBox:
        group = QGroupBox("Generator")

        layout = QVBoxLayout()
        group.setLayout(layout)

        line_1 = QLabel("Password: ")
        layout.addWidget(line_1)

        self.output = QLineEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        sublayout_1 = QHBoxLayout()

        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate)
        self.generate_button.setFixedSize(240, 30)
        sublayout_1.addWidget(self.generate_button)

        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setFixedSize(60, 30)
        sublayout_1.addWidget(self.copy_button)

        layout.addLayout(sublayout_1)

        self.length_slider = QSlider(Qt.Orientation.Horizontal)
        self.length_slider.setRange(4, 40)
        self.length_slider.setSingleStep(1)
        self.length_slider.setPageStep(2)
        self.length_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.length_slider.valueChanged.connect(self.update_slider_label)
        layout.addWidget(self.length_slider)

        self.result_label = QLabel(f"Length: {self.length_slider.value()}")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        return group

    def settings_panel(self) -> QGroupBox:
        group = QGroupBox("Settings")

        layout = QVBoxLayout()
        group.setLayout(layout)

        self.check_lower_case = QCheckBox("Include lowercase letters")
        layout.addWidget(self.check_lower_case)

        self.check_upper_case = QCheckBox("Include uppercase letters")
        layout.addWidget(self.check_upper_case)

        self.check_digits = QCheckBox("Include digits")
        layout.addWidget(self.check_digits)

        self.check_symbols = QCheckBox("Include symbols")
        layout.addWidget(self.check_symbols)

        return group

    def generate(self) -> None:
        if not any([
            self.check_lower_case.isChecked(),
            self.check_upper_case.isChecked(),
            self.check_digits.isChecked(),
            self.check_symbols.isChecked()
        ]):
            self.output.setText("Select at least one character set")
            return

        length = self.length_slider.value()
        password = logic.generate_password(length, self)
        self.output.setText(password)

    def update_slider_label(self, value) -> None:
        self.result_label.setText(f'Length: {value}')

    def user_settings(self) -> tuple[bool, bool, bool, bool]:
        use_lower = self.check_lower_case.isChecked()
        use_upper = self.check_upper_case.isChecked()
        use_digits = self.check_digits.isChecked()
        use_symbols = self.check_symbols.isChecked()

        return use_lower, use_upper, use_digits, use_symbols

    def copy_to_clipboard(self) -> None:
        password = self.output.text()
        if password:
            QApplication.clipboard().setText(password)
            self.copy_button.setText('Copied!')
            QTimer.singleShot(2000, lambda: self.copy_button.setText('Copy'))
