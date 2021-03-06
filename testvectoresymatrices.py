import unittest
import vectoresmatricescomplejos as lva

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(lva.sumvectores([(1,2),(3,2)],[(0,0),(0,0)]),[(1,2),(3,2)])

    def test_upper(self):
        self.assertEqual(lva.inverso([(1,2),(3,5),(-8,9)]),[(-1,-2),(-3,-5),(8,-9)])

    def test_upper(self):
        self.assertEqual(lva.multiplicacionescalar([(1,2),(3,4),(5,2)],(1,-2)),[(5, 0), (11, -2), (9, -8)])

    def test_upper(self):
        self.assertEqual(lva.sumamtrices([[(1, 0), (2, 0)], [(3, 4),(4, 5)]], [[(4, 5), (1, 3)], [(6, 7), (8, 9)]]),[[(5, 5), (3, 3)], [(9, 11), (12, 14)]])

    def test_upper(self):
        self.assertEqual(lva.inversaaditiva([[(1, 0), (2, 0)], [(3, 4),(4, 5)]]),[[(-1, 0), (-2, 0)], [(-3, -4), (-4, -5)]])

    def test_upper(self):
        self.assertEqual(lva.multescalarm([[(1, 0), (2, 0)], [(3, 4),(4, 5)]],(3/2,1)),[[(1.5, 1.0), (3.0, 2.0)], [(0.5, 9.0), (1.0, 11.5)]])

    def test_upper(self):
        self.assertEqual(lva.transpuesta([[(1, 2), (2, -1/5)], [(3, 4),(4, 5)]]),[[(1, 2),(3, 4)],[(2, -1/5),(4, 5)]])

    def test_upper(self):
        self.assertEqual(lva.conjugadamatriz([[(1, 2), (2, -1/5)], [(3, 4),(4, 5)]]),[[(1, -2), (2, 0.2)], [(3, -4), (4, -5)]])

    def test_upper(self):
        self.assertEqual(lva.dagamatriz([[(1, 2), (2, -1/5)], [(3, 4),(4, 5)]]),[[(1, -2), (3, -4)], [(2, 0.2), (4, -5)]])

    def test_upper(self):
        self.assertEqual(lva.multiplimatr([[(1, 0), (2, 0)], [(3, 4),(4, 5)]], [[(4, 5), (1, 3)], [(6, 7), (8, 9)]]),[[(16, 19), (17, 21)], [(-19, 89), (-22, 89)]])

    def test_upper(self):
        self.assertEqual(lva.accion([[(3, -3), (0, -5)], [(2, -9), (9, -6)]], [[(1, 1/2)],[(3, 5)]]),[[(29.5, -16.5)], [(63.5, 19.0)]])

    def test_upper(self):
        self.assertEqual(lva.innerpro([(1,2),(3,2)],[(0,0),(0,0)]),(0,0))

    def test_upper(self):
        self.assertEqual(lva.norma([[4, 5], [1, 3], [29, 54], [31, -13/3]]),69.19)

    def test_upper(self):
        self.assertEqual(lva.distancia([(3, 1), (2, -6), (7, 5), (3, -6)], [(5, 1), (4, 2/3), (6, -3), (1, 7/8)]),18.65)

    def test_upper(self):
        self.assertEqual(lva.unitaria([[[1, 0], [0, 0], [0, 0]], [[0, 0], [1, 0], [0, 0]], [[0, 0], [0, 0], [1, 0]]]),True)

    def test_upper(self):
        self.assertEqual(lva.hermitiana([[(7,0),(6,5)],[(6,-5),(-3,0)]]),True)

    def test_upper(self):
        self.assertEqual(lva.tensor([[[3, 2], [5/2, -1], [18/7, 2]], [[1, 5], [12, 0], [6, -3]], [[2, 6], [4, 3], [9, 3]]],[[[1, 0], [3, 4], [5, -7]], [[10, -2], [2, 9], [-9/8, 5]], [[0, 8], [1/3, 0], [1, -9]]]),[[(3, 2), (1, 18), (29, -11), (2.5, -1.0), (11.5, 7.0), (5.5, -22.5), (2.5714285714285716, 2.0), (-0.2857142857142847, 16.285714285714285), (26.857142857142858, -8.0)], [(34, 14), (-12, 31), (-13.375, 12.75), (23.0, -15.0), (14.0, 20.5), (2.1875, 13.625), (29.714285714285715, 14.857142857142858), (-12.857142857142858, 27.142857142857146), (-12.892857142857142, 10.607142857142858)], [(-16, 24), (1.0, 0.6666666666666666), (21, -25), (8.0, 20.0), (0.8333333333333333, -0.3333333333333333), (-6.5, -23.5), (-16.0, 20.571428571428573), (0.8571428571428572, 0.6666666666666666), (20.571428571428573, -21.142857142857146)], [(1, 5), (-17, 19), (40, 18), (12, 0), (36, 48), (60, -84), (6, -3), (30, 15), (9, -57)], [(20, 48), (-43, 19), (-26.125, -0.625), (120, -24), (24, 108), (-13.5, 60.0), (54, -42), (39, 48), (8.25, 33.375)], [(-40, 8), (0.3333333333333333, 1.6666666666666665), (46, -4), (0, 96), (4.0, 0.0), (12, -108), (24, 48), (2.0, -1.0), (-21, -57)], [(2, 6), (-18, 26), (52, 16), (4, 3), (0, 25), (41, -13), (9, 3), (15, 45), (66, -48)], [(32, 56), (-50, 30), (-32.25, 3.25), (46, 22), (-19, 42), (-19.5, 16.625), (96, 12), (-9, 87), (-25.125, 41.625)], [(-48, 16), (0.6666666666666666, 2.0), (56, -12), (-24, 32), (1.3333333333333333, 1.0), (31, -33), (-24, 72), (3.0, 1.0), (36, -78)]])


if __name__ == '__main__':
    unittest.main()


