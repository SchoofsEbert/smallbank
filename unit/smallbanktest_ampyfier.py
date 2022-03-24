from smallbank import SmallBank
import unittest


class SmallBankTest(unittest.TestCase):

    def setUp(self):
        self.b = SmallBank('Iwena Kroka')

    def testInit(self):
        b = SmallBank('Iwena Kroka')
        self.assertEqual(b.get_balance(), 0)

    def testDeposit(self):
        self.b.deposit(10)
        self.assertEqual(self.b.get_balance(), 10)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        self.b.deposit(100)
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 210)

    def testWithdraw(self):
        self.b.deposit(100)
        self.b.withdraw(30)
        self.assertEqual(self.b.get_balance(), 70)

    def testGetTransaction(self):
        self.b.deposit(100)
        self.assertEqual(self.b.get_transaction(0), 100)

    def testInit_amp(self):
        b = SmallBank('Iwena Kroka')
        self.assertEqual(b.get_self(), b)
        self.assertEqual(b.get_transactions(), [])
        self.assertTrue(b.is_empty())
        self.assertEqual(b.owner, 'Iwena Kroka')
        self.assertEqual(b.get_balance(), 0)

    def testDeposit_amp(self):
        self.b.deposit(10)
        self.assertEqual(self.b.get_transactions(), [10])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 10)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 110)
        self.assertEqual(self.b.get_self(), self.b)
        self.assertEqual(self.b.get_transactions(), [10, 100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.b.deposit(100)
        self.assertEqual(self.b.get_self(), self.b)
        self.assertEqual(self.b.get_transactions(), [10, 100, 100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 210)

    def testDeposit_amp_call_rem_0_none_0_numb_zero_0(self):
        self.assertEqual(self.b.get_balance(), 0)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(0)
        self.assertEqual(excep_info.exception.args, (
            'Can only deposit an amount > 0',))
        self.assertEqual(self.b.get_balance(), 0)

    def testDeposit_amp_call_add_1_none_1_call_rem_3(self):
        self.b.deposit(10)
        self.assertEqual(self.b.get_transactions(), [10])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 10)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(-61637)
        self.assertEqual(excep_info.exception.args, (
            'Can only deposit an amount > 0',))
        self.assertEqual(self.b.get_balance(), 10)

    def testWithdraw_amp_numb_zero_1_none_0(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(0)
        self.assertEqual(excep_info.exception.args, (
            'Can only withdraw an amount > 0',))
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_amp_none_1_call_add_1(self):
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 100)
        self.assertEqual(self.b.get_self(), self.b)
        self.assertEqual(self.b.get_transactions(), [100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(-26277)
        self.assertEqual(excep_info.exception.args, (
            'Can only withdraw an amount > 0',))
        self.assertEqual(self.b.get_balance(), 100)

    def testWithdraw_amp_call_rem_0(self):
        self.b.withdraw(30)
        self.assertEqual(self.b.get_self(), self.b)
        self.assertEqual(self.b.get_transactions(), [])
        self.assertTrue(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 0)

    def testDeposit_numb_zero_2_none_1_none_0(self):
        self.assertEqual(self.b.get_balance(), 0)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(0)
        self.assertEqual(excep_info.exception.args, (
            'Can only deposit an amount > 0',))
        self.assertEqual(self.b.get_balance(), 0)

    def testDeposit_call_rem_1_call_add_1(self):
        self.b.deposit(10)
        self.assertEqual(self.b.get_transactions(), [10])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 10)
        self.assertIsInstance(self.b.get_self(), SmallBank)
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 110)
        self.assertEqual(self.b.get_transactions(), [10, 100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        with self.assertRaises(Exception) as excep_info:
            self.b.deposit(-52705)
        self.assertEqual(excep_info.exception.args, (
            'Can only deposit an amount > 0',))
        self.assertEqual(self.b.get_balance(), 110)

    def testWithdraw_call_rem_0_numb_zero_0(self):
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(0)
        self.assertEqual(excep_info.exception.args, (
            'Can only withdraw an amount > 0',))
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_call_rem_0(self):
        self.b.withdraw(30)
        self.assertEqual(self.b.get_transactions(), [])
        self.assertTrue(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        self.assertEqual(self.b.get_balance(), 0)

    def testWithdraw_call_add_0_call_rem_2(self):
        self.b.deposit(100)
        self.assertEqual(self.b.get_balance(), 100)
        self.assertEqual(self.b.get_transactions(), [100])
        self.assertFalse(self.b.is_empty())
        self.assertEqual(self.b.owner, 'Iwena Kroka')
        with self.assertRaises(Exception) as excep_info:
            self.b.withdraw(-44661)
        self.assertEqual(excep_info.exception.args, (
            'Can only withdraw an amount > 0',))
        self.assertEqual(self.b.get_balance(), 100)


if __name__ == '__main__':
    unittest.main()
