import unittest
from main import main
import unittest.mock as mock

class TestIntegration(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['\n', '\n', '\n', '\n', '\n', '\n', 'T', 'L', '3', '3', '\n',])
    def test_integration_3_ai(self, input):
        with self.assertRaises(SystemExit):
            main()

    @mock.patch('builtins.input', side_effect=['\n', '\n', '\n', '\n', '\n', '\n', 'T', 'L', '4', '4', '\n',])
    def test_integration_4_ai(self, input):
        with self.assertRaises(SystemExit):
            main()

    @mock.patch('builtins.input', side_effect=['\n', '\n', '\n', '\n', '\n', '\n', 'T', 'L', '5', '5', '\n',])
    def test_integration_5_ai(self, input):
        with self.assertRaises(SystemExit):
            main()

    @mock.patch('builtins.input', side_effect=['\n', '\n', '\n', '\n', '\n', '\n', 'T', 'L', '6', '6', '\n',])
    def test_integration_6_ai(self, input):
        with self.assertRaises(SystemExit):
            main()

    @mock.patch('builtins.input', side_effect=['\n', '\n', '\n', '\n', '\n', '\n', 'T', 'L', '7', '7', '\n',])
    def test_integration_7_ai(self, input):
        with self.assertRaises(SystemExit):
            main()

    @mock.patch('builtins.input', side_effect=['\n', '\n', '\n', '\n', '\n', '\n', 'T', 'L', '8', '8', '\n',])
    def test_integration_8_ai(self, input):
        with self.assertRaises(SystemExit):
            main()

if __name__ == "__main__":
    unittest.main()