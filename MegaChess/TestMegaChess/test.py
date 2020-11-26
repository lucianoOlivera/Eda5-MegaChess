import unittest
class testEjemplo(unittest.TestCase):

    def test_calidarVerdadero(self):
        a = 2
        self.assertTrue(a == 2, "Espera un true")

    def test_calidarfalse (self):
        a = 1
        self.assertFalse( 2 == a, "Espera un false")

    def test_Equal(self):
        a = 5
        b = 4+1
        self.assertEqual(a,b,"son iguales")

    def verificar_NotEcual(self):
        a = 5
        b = 10
        self.assertNotEqual(a.b,"son distintos")
    def test_nulo(self):
        a = None
        self.assertIsNone(a,"es noe")
    def test_NoNulo(self):
        a = 5
        self.assertIsNotNone(a,"no es None")
    def test_AssertIS(self): #Mira el typo de dato
        a = 5
        b = 5
        self.assertIs(a,b,"no osn iguales")

    def test_AssertISnot (self):  # Mira el typo de dato
            a = 5
            b = 5.00
            self.assertIsNot(a, b, "no osn iguales")
    def test_Assertin(self):
        a = "Hola"
        b = "Hola mundo"

        self.assertIn(a,b,"El texto no esta incluido")

    def test_assertInnot(self):
        a = "hola"
        b = "HOLA"
        self.assertNotIn(a,b)

    def test_asserGreatr(self):
        a = 7
        b = 1
        self.assertGreater(a,b,"a es mayor que b")
    def test_assertgreaterequal(self):
        a = 5
        b = 1
        self.assertGreaterEqual(a,b)