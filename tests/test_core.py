import unittest
from promptcli import render
class Tests(unittest.TestCase):
 def test_render(self): self.assertEqual(render("Hello {name}",{"name":"Medu"}),"Hello Medu")
if __name__=="__main__":unittest.main()
