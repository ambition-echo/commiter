from committer.ui.UI_mainwindow import Ui_MainWindow
from committer.utils.standardpath import StandardPath
from committer.utils.uitools import set_size
from PySide2.QtGui import QIcon, QPixmap
from committer.resource import rc_icons
from PySide2.QtWidgets import QWidget
import os


class MainWindow(QWidget, Ui_MainWindow):

    def __init__(self, username):
        super(MainWindow, self).__init__()
        self.user_name = username
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.set_icons()
        self.set_boxes()
        self.set_other_ui()

    def set_icons(self):
        self.setWindowIcon(QIcon(QPixmap(":/icons/committer.png")))
        self.my_commit_btn.setIcon(QIcon(QPixmap(":/icons/my.svg")))
        self.assigned_me_btn.setIcon(QIcon(QPixmap(":/icons/assigned.svg")))
        self.save_to_draft_btn.setIcon(QIcon(QPixmap(":/icons/save.svg")))
        self.save_to_template_btn.setIcon(
            QIcon(QPixmap(":/icons/template.svg")))
        self.commit_btn.setIcon(QIcon(QPixmap(":/icons/commit.svg")))

        label_icon_list = [
            self.user_name_icon, self.product_icon, self.project_icon,
            self.module_icon, self.branch_icon, self.type_icon,
            self.severity_icon, self.pri_icon, self.version_icon, self.os_icon,
            self.browser_icon, self.draft_icon, self.template_icon,
            self.title_icon, self.keywords_icon, self.mailto_icon
        ]
        for i in label_icon_list:
            set_size(i)
        self.user_name_icon.setPixmap(QPixmap(":/icons/user.svg"))
        self.product_icon.setPixmap(QPixmap(":/icons/product.svg"))
        self.project_icon.setPixmap(QPixmap(":/icons/project.svg"))
        self.module_icon.setPixmap(QPixmap(":/icons/module.svg"))
        self.branch_icon.setPixmap(QPixmap(":/icons/branch.svg"))
        self.type_icon.setPixmap(QPixmap(":/icons/type.svg"))
        self.severity_icon.setPixmap(QPixmap(":/icons/severity.svg"))
        self.pri_icon.setPixmap(QPixmap(":/icons/pri.svg"))
        self.version_icon.setPixmap(QPixmap(":/icons/version.svg"))
        self.os_icon.setPixmap(QPixmap(":/icons/os.svg"))
        self.browser_icon.setPixmap(QPixmap(":/icons/browser.svg"))
        self.draft_icon.setPixmap(QPixmap(":/icons/draft.svg"))
        self.template_icon.setPixmap(QPixmap(":/icons/template.svg"))
        self.title_icon.setPixmap(QPixmap(":/icons/title.svg"))
        self.keywords_icon.setPixmap(QPixmap(":/icons/keywords.svg"))
        self.mailto_icon.setPixmap(QPixmap(":/icons/mailto.svg"))

    def set_other_ui(self):
        self.user_name_label.setText(self.user_name)
        self.setWindowTitle("Committer")

    def set_boxes(self):
        self.set_local_box()
        self.set_remote_box()

    def set_local_box(self):
        type_list = [
            'baselineedition', 'docerror', 'reliable', 'compatible',
            'modifyimport', 'codeerror', 'config', 'install', 'security',
            'performance', 'standard', 'designdefect', 'system', 'app',
            'desktop', 'kernel', 'newfeature', 'page_display', 'experience',
            'function', 'interface', 'operation_prompt', 'not_involve'
        ]
        for item in type_list:
            self.type_box.addItem(item)
        os_list = [
            'ios', 'android', 'deepin', 'uos', 'all', 'windows', 'others'
        ]
        for item in os_list:
            self.os_box.addItem(item)
        browser_list = ['uos', 'all', 'ie', 'chrome', 'firefox', 'other']
        for item in browser_list:
            self.browser_box.addItem(item)
        for i in range(1, 5):
            self.severity_box.addItem(str(i))
        for i in range(5):
            self.pri_box.addItem(str(i))
        self.get_draft_list()
        self.get_template_list()

    def get_draft_list(self):
        draft_dir = StandardPath.draft_dir()
        StandardPath.check(draft_dir)
        self.draft_box.addItem("None")
        for r, dirs, files in os.walk(draft_dir):
            for i in files:
                if i.endswith('json'):
                    self.draft_box.addItem(i.split('.')[0])
        self.draft_box.setCurrentText("None")

    def get_template_list(self):
        template_dir = StandardPath.template_dir()
        StandardPath.check(template_dir)
        self.template_box.addItem("None")
        for r, dirs, files in os.walk(template_dir):
            for i in files:
                if i.endswith('json'):
                    self.template_box.addItem(i.split('.')[0])
        self.template_box.setCurrentText("None")

    def set_remote_box(self):
        pass

    def build_json(self):
        data = {'meta': {}, "auth": {}}
        data['meta']['product'] = self.product_box.currentText()
