import unittest

class BrainfuckInterpreter:
    def __init__ (self):
        self._cells = [0] * 30000
        self._output = ""

    def output(self):
        return "\0"

    def cells(self):
        return self._cells

    def eval(self, commands) :
        nextCommand = self.__commands[commands[0]]
        nextCommand( self )

    def commandPlus(self):
        self._cells[0] += 1

    def commandMinus(self):
        self._cells[0] -= 1
        self._cells[0] %= 256

    def commandOutput(self):
        pass

    __commands = {
        "+": commandPlus,
        "-": commandMinus,
        ".": commandOutput,
        }
        
class BrainfuckInterpreterTest(unittest.TestCase):

    def test_the_truth(self):
        self.assertEquals(True, True)

    def test_plus_as_a_program_increase_the_first_cell_by_one(self):
        myInterpreter = BrainfuckInterpreter()
        before = myInterpreter.cells()[0]
        myInterpreter.eval('+')
        after = myInterpreter.cells()[0]
        expected = before+1
        self.assertEquals(expected, after)

    def test_minus_as_a_program_decrease_the_first_cell_by_one(self):
        myInterpreter = BrainfuckInterpreter()
        before = myInterpreter.cells()[0]
        myInterpreter.eval("-")
        after = myInterpreter.cells()[0]
        expected = (before - 1) % 256
        self.assertEquals(expected, after)
    
    def test_dot_as_a_program_output_null(self):
        myInterpreter = BrainfuckInterpreter()
        myInterpreter.eval(".")
        self.assertEquals("\0",myInterpreter.output())

    def test_plus_dot_as_program_output_backslash_1(self):
        myInterpreter = BrainfuckInterpreter()
        myInterpreter.eval("+.")
        self.assertEquals("\1", myInterpreter.output())       


if __name__ == "__main__":
	unittest.main()
