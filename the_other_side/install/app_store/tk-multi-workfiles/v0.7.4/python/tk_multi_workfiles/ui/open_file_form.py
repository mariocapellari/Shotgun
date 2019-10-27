# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_file_form.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_OpenFileForm(object):
    def setupUi(self, OpenFileForm):
        OpenFileForm.setObjectName("OpenFileForm")
        OpenFileForm.resize(514, 666)
        self.verticalLayout_3 = QtGui.QVBoxLayout(OpenFileForm)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.name_label = QtGui.QLabel(OpenFileForm)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_6.addWidget(self.name_label)
        self.name_line = QtGui.QFrame(OpenFileForm)
        self.name_line.setFrameShadow(QtGui.QFrame.Plain)
        self.name_line.setFrameShape(QtGui.QFrame.HLine)
        self.name_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.name_line.setObjectName("name_line")
        self.verticalLayout_6.addWidget(self.name_line)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.title_label = QtGui.QLabel(OpenFileForm)
        self.title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.publish_frame = QtGui.QFrame(OpenFileForm)
        self.publish_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.publish_frame.setMouseTracking(False)
        self.publish_frame.setFocusPolicy(QtCore.Qt.TabFocus)
        self.publish_frame.setStyleSheet("#publish_frame {\n"
"border-radius: 4px;\n"
"border-style: none;\n"
"border-width: 1px;\n"
"border-color: rgb(0,0,0);\n"
"background-color: rgb(255,255,255,48);\n"
"}")
        self.publish_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.publish_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.publish_frame.setObjectName("publish_frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.publish_frame)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.publish_title_label = QtGui.QLabel(self.publish_frame)
        self.publish_title_label.setObjectName("publish_title_label")
        self.verticalLayout_4.addWidget(self.publish_title_label)
        self.publish_line = QtGui.QFrame(self.publish_frame)
        self.publish_line.setFrameShadow(QtGui.QFrame.Plain)
        self.publish_line.setFrameShape(QtGui.QFrame.HLine)
        self.publish_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.publish_line.setObjectName("publish_line")
        self.verticalLayout_4.addWidget(self.publish_line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.publish_details = QtGui.QLabel(self.publish_frame)
        self.publish_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.publish_details.setWordWrap(True)
        self.publish_details.setMargin(0)
        self.publish_details.setIndent(0)
        self.publish_details.setObjectName("publish_details")
        self.horizontalLayout.addWidget(self.publish_details)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.publish_thumbnail = QtGui.QLabel(self.publish_frame)
        self.publish_thumbnail.setMinimumSize(QtCore.QSize(130, 90))
        self.publish_thumbnail.setMaximumSize(QtCore.QSize(130, 90))
        self.publish_thumbnail.setStyleSheet("#publish_thumbnail {\n"
"background-color: rgb(0,0,0,32);\n"
"border-radius: 2px;\n"
"}")
        self.publish_thumbnail.setFrameShape(QtGui.QFrame.NoFrame)
        self.publish_thumbnail.setLineWidth(0)
        self.publish_thumbnail.setText("")
        self.publish_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.publish_thumbnail.setMargin(0)
        self.publish_thumbnail.setIndent(0)
        self.publish_thumbnail.setObjectName("publish_thumbnail")
        self.verticalLayout_11.addWidget(self.publish_thumbnail)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.publish_note = QtGui.QLabel(self.publish_frame)
        self.publish_note.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.publish_note.setObjectName("publish_note")
        self.verticalLayout_4.addWidget(self.publish_note)
        self.verticalLayout.addWidget(self.publish_frame)
        self.or_label_a = QtGui.QLabel(OpenFileForm)
        self.or_label_a.setAlignment(QtCore.Qt.AlignCenter)
        self.or_label_a.setObjectName("or_label_a")
        self.verticalLayout.addWidget(self.or_label_a)
        self.work_file_frame = QtGui.QFrame(OpenFileForm)
        self.work_file_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.work_file_frame.setFocusPolicy(QtCore.Qt.TabFocus)
        self.work_file_frame.setStyleSheet("#work_file_frame {\n"
"border-radius: 4px;\n"
"border-style: none;\n"
"border-width: 1px;\n"
"border-color: rgb(0,0,0);\n"
"background-color: rgb(255,255,255,48);\n"
"}")
        self.work_file_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.work_file_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.work_file_frame.setObjectName("work_file_frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.work_file_frame)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.work_file_title_label = QtGui.QLabel(self.work_file_frame)
        self.work_file_title_label.setObjectName("work_file_title_label")
        self.verticalLayout_2.addWidget(self.work_file_title_label)
        self.work_file_line = QtGui.QFrame(self.work_file_frame)
        self.work_file_line.setFrameShadow(QtGui.QFrame.Plain)
        self.work_file_line.setFrameShape(QtGui.QFrame.HLine)
        self.work_file_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.work_file_line.setObjectName("work_file_line")
        self.verticalLayout_2.addWidget(self.work_file_line)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.work_file_details = QtGui.QLabel(self.work_file_frame)
        self.work_file_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.work_file_details.setMargin(0)
        self.work_file_details.setIndent(0)
        self.work_file_details.setObjectName("work_file_details")
        self.horizontalLayout_5.addWidget(self.work_file_details)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.work_file_thumbnail = QtGui.QLabel(self.work_file_frame)
        self.work_file_thumbnail.setMinimumSize(QtCore.QSize(130, 90))
        self.work_file_thumbnail.setMaximumSize(QtCore.QSize(130, 90))
        self.work_file_thumbnail.setStyleSheet("#work_file_thumbnail {\n"
"background-color: rgb(0,0,0,32);\n"
"border-radius: 2px;\n"
"}")
        self.work_file_thumbnail.setFrameShape(QtGui.QFrame.NoFrame)
        self.work_file_thumbnail.setLineWidth(0)
        self.work_file_thumbnail.setText("")
        self.work_file_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.work_file_thumbnail.setMargin(0)
        self.work_file_thumbnail.setIndent(0)
        self.work_file_thumbnail.setObjectName("work_file_thumbnail")
        self.verticalLayout_12.addWidget(self.work_file_thumbnail)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.horizontalLayout_5.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.work_file_frame)
        self.or_label_b = QtGui.QLabel(OpenFileForm)
        self.or_label_b.setAlignment(QtCore.Qt.AlignCenter)
        self.or_label_b.setObjectName("or_label_b")
        self.verticalLayout.addWidget(self.or_label_b)
        self.publish_ro_frame = QtGui.QFrame(OpenFileForm)
        self.publish_ro_frame.setCursor(QtCore.Qt.PointingHandCursor)
        self.publish_ro_frame.setMouseTracking(False)
        self.publish_ro_frame.setFocusPolicy(QtCore.Qt.TabFocus)
        self.publish_ro_frame.setStyleSheet("#publish_ro_frame {\n"
"border-radius: 4px;\n"
"border-style: none;\n"
"border-width: 1px;\n"
"border-color: rgb(0,0,0);\n"
"background-color: rgb(255,255,255,48);\n"
"}")
        self.publish_ro_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.publish_ro_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.publish_ro_frame.setObjectName("publish_ro_frame")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.publish_ro_frame)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.publish_ro_title_label = QtGui.QLabel(self.publish_ro_frame)
        self.publish_ro_title_label.setObjectName("publish_ro_title_label")
        self.verticalLayout_8.addWidget(self.publish_ro_title_label)
        self.publish_ro_line = QtGui.QFrame(self.publish_ro_frame)
        self.publish_ro_line.setFrameShadow(QtGui.QFrame.Plain)
        self.publish_ro_line.setFrameShape(QtGui.QFrame.HLine)
        self.publish_ro_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.publish_ro_line.setObjectName("publish_ro_line")
        self.verticalLayout_8.addWidget(self.publish_ro_line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtGui.QLabel(self.publish_ro_frame)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setMargin(0)
        self.label_9.setIndent(0)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.publish_ro_frame)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.break_line = QtGui.QFrame(OpenFileForm)
        self.break_line.setFrameShadow(QtGui.QFrame.Plain)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout_5.addWidget(self.break_line)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.cancel_btn = QtGui.QPushButton(OpenFileForm)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.cancel_btn.setDefault(False)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(OpenFileForm)
        QtCore.QMetaObject.connectSlotsByName(OpenFileForm)
        OpenFileForm.setTabOrder(self.publish_frame, self.work_file_frame)
        OpenFileForm.setTabOrder(self.work_file_frame, self.cancel_btn)

    def retranslateUi(self, OpenFileForm):
        OpenFileForm.setWindowTitle(QtGui.QApplication.translate("OpenFileForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("OpenFileForm", "<big><b>name</b></big>", None, QtGui.QApplication.UnicodeUTF8))
        self.title_label.setText(QtGui.QApplication.translate("OpenFileForm", "<big>There is a more recent, published version of this file available!</big>", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_frame.setToolTip(QtGui.QApplication.translate("OpenFileForm", "Click to open the newer Published File", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_title_label.setText(QtGui.QApplication.translate("OpenFileForm", "<big>Would you like to continue your work from the latest Publish?</big>", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_details.setText(QtGui.QApplication.translate("OpenFileForm", "<html><head/><body><p>Version v000<br/>Published on...<br/>Published by...<br/>Description:<br/><span style=\" font-style:italic;\">No description was entered for this publish</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_note.setText(QtGui.QApplication.translate("OpenFileForm", "<html><head/><body><p><small>(Note: The published file will be copied to your work area as version v000 and then opened)</small></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.or_label_a.setText(QtGui.QApplication.translate("OpenFileForm", "<big><b>OR</b></big>", None, QtGui.QApplication.UnicodeUTF8))
        self.work_file_frame.setToolTip(QtGui.QApplication.translate("OpenFileForm", "Click to open the older Work File", None, QtGui.QApplication.UnicodeUTF8))
        self.work_file_title_label.setText(QtGui.QApplication.translate("OpenFileForm", "<big>Would you prefer to open the older Work File instead?</big>", None, QtGui.QApplication.UnicodeUTF8))
        self.work_file_details.setText(QtGui.QApplication.translate("OpenFileForm", "<html><head/><body><p>Version v000<br/>Updated on...<br/>Updated by...</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.or_label_b.setText(QtGui.QApplication.translate("OpenFileForm", "<big><b>OR</b></big>", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_ro_frame.setToolTip(QtGui.QApplication.translate("OpenFileForm", "<html><head/><body><p>Click to open the older Published File read-only</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_ro_title_label.setText(QtGui.QApplication.translate("OpenFileForm", "<html><head/><body><p><span style=\" font-size:large;\">You can open the older Publish read-only?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("OpenFileForm", "<html><head/><body><p><span style=\" font-style:italic;\">Note: If you open the Publish read-only, you will have to save the file into your Work Area before you can continue working with it.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("OpenFileForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
