import unittest

class BrainfuckInterpreter:
    def __init__ (self):
        self._cells = [0] * 30000

    def cells(self):
        return self._cells

    def eval(self, command):
        self._cells[0] += 1
        
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


if __name__ == "__main__":
	unittest.main()
