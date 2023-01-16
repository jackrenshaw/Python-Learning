import gi 
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import calculatorEval

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MathUI:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("Calculator.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window1")
        self.textarea = self.builder.get_object("textvalue")
        self.window.show_all()

    def one(self,widget):
        self.textarea.Text = "testing"
        print(self.Buffer)
        return True

    def two(self):
        return True

    def three(self):
        return True

    def four(self):
        return True

    def five(self):
        return True

    def six(self):
        return True
        
    def seven(self):
        return True

    def eight(self):
        return True

    def nine(self):
        return True

    def plus(self):
        return True

    def minus(self):
        return True
        
    def multiply(self):
        return True

    def divide(self):
        return True

    def lparen(self):
        return True

    def rparen(self):
        return True

    def equal(self):
        return True

if __name__ == "__main__":
    MathUI()
    Gtk.main()