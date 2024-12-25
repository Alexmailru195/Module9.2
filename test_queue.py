import unittest
from LinkedList import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(3)

    def test_is_empty(self):
        """Тест на проверку метода is_empty."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('a')
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        """Тест на проверку метода is_full."""
        self.assertFalse(self.queue.is_full())
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.assertTrue(self.queue.is_full())

if __name__ == "__main__":
    unittest.main()