import unittest
from unittest.mock import MagicMock,patch
from cal import *    

class Mob():
    def __init__(self,xpos,ypos,width,height):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        
class Mytest(unittest.TestCase):
    def test_aabbcollision(self):
        list1 = [Mob(15,10,3,2),Mob(7,10,3,2),Mob(10,9,2,1),Mob(10,12,5,3),Mob(15,7,3,3),Mob(7,8,3,2),Mob(7,12,3,3),Mob(15,12,1,1)]
        list2 = [Mob(16,10,3,2),Mob(7,10,2,2),Mob(10,9,2,0.5),Mob(10,13,5,3)]
        center = Mob(10,10,5,2)

        for i in range(8):
            self.assertEqual(aabbcollision(center,list1[i]),True)
        for i in range(4):
            self.assertEqual(aabbcollision(center,list2[i]),False)

    def test_gameed2(self):
        self.assertEqual(gameend2(MagicMock(life = 0),MagicMock(life = 10)),0)
        self.assertEqual(gameend2(MagicMock(life = 1),MagicMock(life = 10)),-1)
        self.assertEqual(gameend2(MagicMock(life = 2),MagicMock(life = 0)),1)
        self.assertEqual(gameend2(MagicMock(life = 0),MagicMock(life = 0)),0)

    @patch('cal.aabbcollision')
    def test_attack(self,mock_get_aabb):
        a = MagicMock(life = 1)
        b = MagicMock(attack = 1)

        mock_get_aabb.return_value = True
        attack(a,b)
        self.assertEqual(a.life,0)

        mock_get_aabb.return_value = False
        attack(a,b)
        self.assertEqual(a.life, 0)
        
if __name__ == '__main__':
    unittest.main()