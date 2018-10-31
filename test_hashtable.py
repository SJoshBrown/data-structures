import unittest
from hashtable import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.target = HashTable()

    def test_initial_size(self):
        self.assertEqual(0, len(self.target))

    def test_set(self):
        self.target[0] = 'zero'

        self.assertEqual(self.target._data[0].value, 'zero')
        self.assertEqual(self.target._data[0].key, 0)

    def test_set_same_key(self):
        self.target[9] = 'something'
        self.target[9] = 'something else'

        self.assertEqual(self.target._data[1].value, 'something else')
        self.assertEqual(self.target._data[1].key, 9)

    def test_set_same_hash(self):
        self.target[1] = 'something'
        self.target[9] = 'something else'

        self.assertEqual(self.target._data[1].value, 'something')
        self.assertEqual(self.target._data[1].key, 1)
        self.assertEqual(self.target._data[1].next.value, 'something else')
        self.assertEqual(self.target._data[1].next.key, 9)

    def test_get(self):
        self.target[5] = "some data"

        result = self.target[5]

        self.assertEqual("some data", result)

    def test_get_search_linked_list(self):
        self.target[5] = "test data"
        self.target[13] = "42"
        self.target[21] = "1337"

        result = self.target[5]
        result_2 = self.target[13]
        result_3 = self.target[21]

        self.assertEqual("test data", result)
        self.assertEqual("42", result_2)
        self.assertEqual("1337", result_3)

    def test_get_key_error(self):
        result = self.target[5]

        self.assertEqual(None, result)

    def test_contains_false(self):
        result = 5 in self.target

        self.assertEqual(False, result)

    def test_contains_false_while_hashed_index_populated(self):
        self.target[5] = "test data"
        result = 13 in self.target

        self.assertEqual(False, result)

    def test_contains_true(self):
        self.target[5] = "test data"
        result = 5 in self.target

        self.assertEqual(True, result)

    def test_contains_true_inside_linked_list(self):
        self.target[5] = "test data"
        self.target[13] = "42"
        self.target[21] = "1337"

        result = 13 in self.target

        self.assertEqual(True, result)

    def test_delitem(self):
        self.target[5] = "test data"

        del self.target[5]

        self.assertEqual(0, len(self.target))
        self.assertEqual(None, self.target._data[5])

    def test_delitem_inside_linked_list(self):
        self.target[5] = "test data"
        self.target[13] = "42"
        self.target[21] = "1337"

        del self.target[13]

        self.assertEqual(2, len(self.target))
        self.assertEqual(None, self.target[13])
        self.assertEqual("test data", self.target[5])
        self.assertEqual("1337", self.target[21])

    def test_resize_up(self):
        self.target[1] = 'some data'
        self.target[2] = 'some data'
        self.target[3] = 'some data'
        self.target[4] = 'some data'
        self.target[5] = 'some data'
        self.target[6] = 'some data'
        self.target[7] = 'some data'
        self.target[8] = 'some data'
        self.target[9] = 'beyond old range'

        self.assertEqual(16, self.target._capacity)
        self.assertEqual(16, len(self.target._data))
        self.assertEqual('beyond old range', self.target._data[9].value)

    def test_resize_down(self):
        self.target[1] = 'some data'
        self.target[2] = 'some data'
        self.target[3] = 'some data'
        self.target[4] = 'some data'
        self.target[5] = 'some data'
        self.target[6] = 'some data'
        self.target[7] = 'some data'

        self.assertEqual(16, self.target._capacity)
        self.assertEqual(16, len(self.target._data))

        del self.target[7]
        del self.target[6]
        del self.target[5]
        del self.target[4]

        self.assertEqual(8, self.target._capacity)
        self.assertEqual(8, len(self.target._data))
