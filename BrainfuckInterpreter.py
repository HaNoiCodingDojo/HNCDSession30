import unittest

class BrainfuckInterpreter:
    def __init__ (self):
        self._cells = [0] * 30000
        self._output = ""
        self.dataPointer = 0

    def output(self):
        return self._output

    def cells(self):
        return self._cells

    def eval(self, commands) :
        for nextCommandChar in commands:
            nextCommand = self.__commands[nextCommandChar]
            nextCommand( self )

    def commandPlus(self):
        self._cells[self.dataPointer] += 1

    def commandMinus(self):
        self._cells[self.dataPointer] -= 1
        self._cells[self.dataPointer] %= 256

    def commandDot(self):
        self._output += str(chr(self._cells[self.dataPointer]))

    def commandGreat(self):
        self.dataPointer += 1

    __commands = {
        "+": commandPlus,
        "-": commandMinus,
        ".": commandDot,
        ">": commandGreat,
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

    def test_great_plus_as_program_increase_the_second_cell_by_one(self):
        myInterpreter = BrainfuckInterpreter()
        before = myInterpreter.cells()[1]
        myInterpreter.eval('>+')
        after = myInterpreter.cells()[1]
        expected = before + 1
        self.assertEquals(expected, after)

    def test_great_plus_dot_as_program_output_backslash_one(self):
        myInterpreter = BrainfuckInterpreter()
        myInterpreter.eval('>+.')
        self.assertEquals("\1", myInterpreter.output())
    
    def test_hello_as_a_program_do_nothing_and_output_nothing(self):
        myInterpreter = BrainfuckInterpreter()
        myInterpreter.eval('hello')
        self.assertEquals("", myInterpreter.output())
        self.assertEquals([0] * 30000, myInterpreter.cells())
    

if __name__ == "__main__":
	unittest.main()
