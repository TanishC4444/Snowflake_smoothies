import unittest
from unittest.mock import Mock
from streamlit_app import save_order

class OrderTests(unittest.TestCase):
    def test_user_input_is_bound_not_interpolated(self):
        session = Mock()
        name = "O'Brien'); DROP TABLE orders; --"
        save_order(session, 'Apple Mango', name)
        query = session.sql.call_args.args[0]
        self.assertNotIn(name, query)
        self.assertEqual(session.sql.call_args.kwargs['params'], ['Apple Mango', name])
        session.sql.return_value.collect.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
