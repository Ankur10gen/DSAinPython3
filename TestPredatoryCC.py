import unittest
from PredatoryCreditCard import PredatoryCreditCard

class TestPCC(unittest.TestCase):

    def test_get_customer(self):
        pcc = PredatoryCreditCard('Ankur', 'CITI', '12012023', 95000, 0.03)
        self.assertEqual(pcc.get_customer(), 'Ankur')

    def test_charge(self):
        pcc = PredatoryCreditCard('Ankur', 'CITI', '12012023', 95000, 0.03)
        self.assertEqual(pcc.charge(95002), False)
        self.assertEqual(pcc.get_liability(),5)

    def test_process_month(self):
        pcc = PredatoryCreditCard('Ankur', 'CITI', '12012023', 95000, 0.03)
        pcc.charge(10000)
        pcc.process_month()
        self.assertEqual(pcc.get_liability(), 10000*pow(1+0.03,1/12))

if __name__ == '__main__':
    unittest.main()
