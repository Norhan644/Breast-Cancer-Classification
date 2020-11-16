from PyQt5 import QtWidgets
from views import field_view

class InputField(QtWidgets.QWidget, field_view.Ui_Form):
    def __init__(self, title:str, min_val:float, max_val: float, default_val:float = None, unit:str=''):
        super(InputField, self).__init__()
        self.setupUi(self)
        self.min_val = min_val
        self.max_val = max_val
        self.field_lbl.setText(f'{title}({min_val}-{max_val})')
        if default_val == None:
            self._current_val = min_val
        else:
            self._current_val = default_val

        self.val_edit.setText(f'{round(self._current_val, 2)}')
        self.unit_lbl.setText(f'{unit}')

    def get_value(self) ->float:
        return self._current_val

    def is_valid(self) ->bool:
        try:
            self._current_val = float(self.val_edit.text())
        except:
            return False
        return True if self.current_val >= min_val and self.current_val =< max_val else False

