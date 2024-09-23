import unittest
import cap


class myTest(unittest.TestCase):
    def test_one(self):
        text = 'sample'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Sample')

    def test_two(self):
        text = 'just do it'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Just Do It')


if __name__ == '__main__':
    unittest.main()
