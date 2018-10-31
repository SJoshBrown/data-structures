import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.target = LinkedList()

    def test_append(self):
        self.target.append(1)

        self.assertEqual(str(self.target), "1")

    def test_append_many(self):
        self.target.append(1)
        self.target.append(2)
        self.target.append(3)

        self.assertEqual(str(self.target), "1->2->3")

    def test_reverse(self):
        self.target.append(1)
        self.target.append(2)
        self.target.append(3)

        self.target.reverse()

        self.assertEqual(str(self.target), "3->2->1")

    def test_remove_head(self):
        self.target.append(1)
        self.target.append(2)
        self.target.append(3)

        self.target.remove(1)

        self.assertEqual(str(self.target), "2->3")

    def test_remove_inner(self):
        self.target.append(1)
        self.target.append(2)
        self.target.append(3)

        self.target.remove(2)

        self.assertEqual(str(self.target), "1->3")

    def test_remove_tail(self):
        self.target.append(1)
        self.target.append(2)
        self.target.append(3)

        self.target.remove(3)

        self.assertEqual(str(self.target), "1->2")

    def test_remove_not_in_list(self):
        self.target.append(1)
        self.target.append(2)
        self.target.append(3)

        self.target.remove(42)

        self.assertEqual(str(self.target), "1->2->3")

    def test_length(self):
        self.assertEqual(len(self.target), 0)

        self.target.append(1)
        self.target.append(2)
        self.target.append(3)
        self.assertEqual(len(self.target), 3)

        self.target.remove(2)
        self.assertEqual(len(self.target), 2)

    def test_bool(self):
        self.assertFalse(self.target)

        self.target.append(1)

        self.assertTrue(self.target)

    def test_get_index(self):
        self.target.append(1)
        self.target.append(2)
        self.target.append(3)

        self.assertEqual(1, self.target[0])
        self.assertEqual(2, self.target[1])
        self.assertEqual(3, self.target[2])

    def tearDown(self):
        self.target = None


if __name__ == '__main__':
    unittest.main()
