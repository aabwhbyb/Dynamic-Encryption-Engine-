import sys
import os
from random import randint
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                           QTextEdit, QSpinBox, QComboBox, QProgressBar,
                           QFileDialog, QMessageBox, QGroupBox)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QFont


class DatabaseGeneratorThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self, filename, num_records, file_format, table_name="Hosin_table"):
        super().__init__()
        self.filename = filename
        self.num_records = num_records
        self.file_format = file_format
        self.table_name = table_name
        self.is_running = True
    
    def run(self):
        try:
            if self.file_format == 'JSON':
                self.generate_json()
            elif self.file_format == 'XML':
                self.generate_xml()
            elif self.file_format == 'SQL':
                self.generate_sql()
            
            if self.is_running:
                self.finished.emit(f"تم إنشاء {self.num_records} سجل بنجاح في الملف: {self.filename}")
            
        except Exception as e:
            self.error.emit(f"خطأ في إنشاء الملف: {str(e)}")
    
    def generate_json(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write("{\n")
            
            for i in range(self.num_records):
                if not self.is_running:
                    break
                    
                # توليد رقم من 99 رقم، كل رقم عشوائي من 0 لـ 9
                big_number = ''.join([str(randint(0, 9)) for _ in range(99)])
                
                if i == self.num_records - 1:  # العنصر الأخير
                    f.write(f'"{i}" : "{big_number}"\n')
                else:
                    f.write(f'"{i}" : "{big_number}" ,\n')
                
                # تحديث شريط التقدم كل 1000 سجل
                if i % 1000 == 0:
                    progress_percent = int((i / self.num_records) * 100)
                    self.progress.emit(progress_percent)
            
            f.write("}")
    
    def generate_xml(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<data>\n')
            
            for i in range(self.num_records):
                if not self.is_running:
                    break
                    
                # توليد رقم من 99 رقم، كل رقم عشوائي من 0 لـ 9
                big_number = ''.join([str(randint(0, 9)) for _ in range(99)])
                
                f.write(f'  <Hosin id="{i}">{big_number}</Hosin>\n')
                
                # تحديث شريط التقدم كل 1000 سجل
                if i % 1000 == 0:
                    progress_percent = int((i / self.num_records) * 100)
                    self.progress.emit(progress_percent)
            
            f.write('</data>')
    
    def generate_sql(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(f'-- Database: {self.table_name}\n')
            f.write(f'-- Records: {self.num_records}\n\n')
            f.write(f'CREATE TABLE IF NOT EXISTS {self.table_name} (\n')
            f.write('  id INT PRIMARY KEY,\n')
            f.write('  value VARCHAR(100)\n')
            f.write(');\n\n')
            
            # كتابة البيانات على دفعات
            batch_size = 1000
            for batch_start in range(0, self.num_records, batch_size):
                if not self.is_running:
                    break
                    
                batch_end = min(batch_start + batch_size, self.num_records)
                f.write(f'INSERT INTO {self.table_name} (id, value) VALUES\n')
                
                for i in range(batch_start, batch_end):
                    if not self.is_running:
                        break
                        
                    # توليد رقم من 99 رقم، كل رقم عشوائي من 0 لـ 9
                    big_number = ''.join([str(randint(0, 9)) for _ in range(99)])
                    
                    if i == batch_end - 1:  # آخر عنصر في الدفعة
                        f.write(f'  ({i}, \'{big_number}\');\n\n')
                    else:
                        f.write(f'  ({i}, \'{big_number}\'),\n')
                
                # تحديث شريط التقدم
                progress_percent = int((batch_end / self.num_records) * 100)
                self.progress.emit(progress_percent)
    
    def stop(self):
        self.is_running = False


class DatabaseGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.generator_thread = None
        
    def initUI(self):
        self.setWindowTitle('أداة توليد قواعد البيانات لتشفير Hosin')
        self.setGeometry(100, 100, 600, 500)
        
        # Widget مركزي
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout رئيسي
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # عنوان البرنامج
        title_label = QLabel('أداة توليد قواعد البيانات Hosin')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Arial', 16, QFont.Bold))
        main_layout.addWidget(title_label)
        
        # مجموعة إعدادات الملف
        file_group = QGroupBox('إعدادات الملف')
        file_layout = QVBoxLayout()
        
        # نوع الملف
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel('نوع الملف:'))
        self.format_combo = QComboBox()
        self.format_combo.addItems(['JSON', 'XML', 'SQL'])
        self.format_combo.currentTextChanged.connect(self.format_changed)
        format_layout.addWidget(self.format_combo)
        file_layout.addLayout(format_layout)
        
        # اسم الملف
        filename_layout = QHBoxLayout()
        filename_layout.addWidget(QLabel('اسم الملف:'))
        self.filename_input = QLineEdit()
        self.filename_input.setPlaceholderText('اتركة فارغ الاسم الافتراضى Hosin لا ينصح بتغيره الا اذا عدلت الملف')
        self.filename_input.setReadOnly(True)
        filename_layout.addWidget(self.filename_input)
        
        self.browse_btn = QPushButton('تصفح')
        self.browse_btn.clicked.connect(self.browse_file)
        filename_layout.addWidget(self.browse_btn)
        
        file_layout.addLayout(filename_layout)
        file_group.setLayout(file_layout)
        main_layout.addWidget(file_group)
        
        # مجموعة إعدادات البيانات
        data_group = QGroupBox('إعدادات البيانات')
        data_layout = QVBoxLayout()
        
        # عدد السجلات
        records_layout = QHBoxLayout()
        records_layout.addWidget(QLabel('عدد السجلات:'))
        self.records_spinbox = QSpinBox()
        self.records_spinbox.setRange(1, 10000000)
        self.records_spinbox.setValue(1000)
        records_layout.addWidget(self.records_spinbox)
        data_layout.addLayout(records_layout)
        
        # معلومات عن البيانات
        info_label = QLabel('سيتم توليد أرقام عشوائية (99 رقم لكل سجل)')
        info_label.setStyleSheet("color: #666666; font-style: italic;")
        data_layout.addWidget(info_label)
        
        data_group.setLayout(data_layout)
        main_layout.addWidget(data_group)
        
        # إعدادات SQL
        self.sql_group = QGroupBox('إعدادات SQL')
        sql_layout = QVBoxLayout()
        
        table_layout = QHBoxLayout()
        table_layout.addWidget(QLabel('اسم الجدول:'))
        self.table_name_input = QLineEdit()
        self.table_name_input.setText('Hosin_table')
        table_layout.addWidget(self.table_name_input)
        sql_layout.addLayout(table_layout)
        
        self.sql_group.setLayout(sql_layout)
        self.sql_group.setVisible(False)
        main_layout.addWidget(self.sql_group)
        
        # شريط التقدم
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)
        
        # الأزرار
        buttons_layout = QHBoxLayout()
        
        self.generate_btn = QPushButton('إنشاء قاعدة البيانات')
        self.generate_btn.clicked.connect(self.generate_database)
        self.generate_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }")
        buttons_layout.addWidget(self.generate_btn)
        
        self.stop_btn = QPushButton('إيقاف')
        self.stop_btn.clicked.connect(self.stop_generation)
        self.stop_btn.setEnabled(False)
        self.stop_btn.setStyleSheet("QPushButton { background-color: #f44336; color: white; font-weight: bold; }")
        buttons_layout.addWidget(self.stop_btn)
        
        main_layout.addLayout(buttons_layout)
        
        # منطقة الرسائل
        self.log_text = QTextEdit()
        self.log_text.setMaximumHeight(150)
        self.log_text.setReadOnly(True)
        main_layout.addWidget(self.log_text)
        
        # رسالة ترحيب
        self.log_message("مرحباً بك في أداة توليد قواعد البيانات! Hosin")
        
    def browse_file(self):
        format_type = self.format_combo.currentText()
        if format_type == 'JSON':
            filename, _ = QFileDialog.getSaveFileName(self, 'حفظ الملف', '', 'JSON Files (*.json)')
        elif format_type == 'XML':
            filename, _ = QFileDialog.getSaveFileName(self, 'حفظ الملف', '', 'XML Files (*.xml)')
        elif format_type == 'SQL':
            filename, _ = QFileDialog.getSaveFileName(self, 'حفظ الملف', '', 'SQL Files (*.sql)')
        
        if filename:
            self.filename_input.setText(filename)
    
    def format_changed(self, format_type):
        if format_type == 'SQL':
            self.sql_group.setVisible(True)
        else:
            self.sql_group.setVisible(False)
    
    def generate_database(self):
        # تحديد نوع الملف
        format_type = self.format_combo.currentText()
        
        # تحديد اسم الملف
        filename = self.filename_input.text().strip()
        if not filename:
            if format_type == 'JSON':
                filename = f"Hosin_{randint(1, 1000000)}.json"
            elif format_type == 'XML':
                filename = f"Hosin_{randint(1, 1000000)}.xml"
            elif format_type == 'SQL':
                filename = f"Hosin_{randint(1, 1000000)}.sql"
        
        # التأكد من الامتداد الصحيح
        if format_type == 'JSON' and not filename.endswith('.json'):
            filename += '.json'
        elif format_type == 'XML' and not filename.endswith('.xml'):
            filename += '.xml'
        elif format_type == 'SQL' and not filename.endswith('.sql'):
            filename += '.sql'
        
        # بدء العملية
        self.log_message(f"بدء إنشاء {self.records_spinbox.value()} سجل ({format_type})...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.generate_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        
        # إنشاء thread للتوليد
        table_name = self.table_name_input.text().strip() if format_type == 'SQL' else "Hosin_table"
        
        self.generator_thread = DatabaseGeneratorThread(
            filename,
            self.records_spinbox.value(),
            format_type,
            table_name
        )
        
        self.generator_thread.progress.connect(self.update_progress)
        self.generator_thread.finished.connect(self.generation_finished)
        self.generator_thread.error.connect(self.generation_error)
        
        self.generator_thread.start()
    
    def stop_generation(self):
        if self.generator_thread and self.generator_thread.isRunning():
            self.generator_thread.stop()
            self.generator_thread.wait()
            self.log_message("تم إيقاف العملية بواسطة المستخدم")
            self.reset_ui()
    
    def update_progress(self, value):
        self.progress_bar.setValue(value)
    
    def generation_finished(self, message):
        self.log_message(message)
        self.progress_bar.setValue(100)
        self.reset_ui()
        QMessageBox.information(self, 'تم بنجاح', message)
    
    def generation_error(self, error_message):
        self.log_message(f"خطأ: {error_message}")
        self.reset_ui()
        QMessageBox.critical(self, 'خطأ', error_message)
    
    def reset_ui(self):
        self.generate_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.progress_bar.setVisible(False)
    
    def log_message(self, message):
        self.log_text.append(f"[{self.get_current_time()}] {message}")
        self.log_text.verticalScrollBar().setValue(
            self.log_text.verticalScrollBar().maximum()
        )
    
    def get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")


def main():
    app = QApplication(sys.argv)
    
    # تطبيق الستايل
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f0f0f0;
        }
        QGroupBox {
            font-weight: bold;
            border: 2px solid #cccccc;
            border-radius: 5px;
            margin-top: 10px;
            padding-top: 10px;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
        }
        QPushButton {
            border: 1px solid #cccccc;
            border-radius: 5px;
            padding: 5px;
            min-height: 20px;
        }
        QPushButton:hover {
            background-color: #e0e0e0;
        }
    """)
    
    window = DatabaseGenerator()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()