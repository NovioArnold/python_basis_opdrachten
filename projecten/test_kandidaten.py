import unittest
from unittest.mock import patch, mock_open
from typing import List
from kandidaten import laad_kandidaten, maak_kandidaten, add_stem, sorteer_kandidaten, sorteer_kandidaten_op_naam, save_kandidaten, Kandidaat

class TestKandidaten(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="1,Jan Janssen,0\n2,Piet Pietersen,0\n")
    def test_laad_kandidaten(self, mock_file):
        kandidaten = laad_kandidaten()
        self.assertEqual(len(kandidaten), 2)
        self.assertEqual(kandidaten[0]["naam"], "Jan Janssen")
        self.assertEqual(kandidaten[1]["stemmen"], 0)

    def test_maak_kandidaten(self):
        kandidaten = maak_kandidaten()
        self.assertEqual(len(kandidaten), 5)
        self.assertEqual(kandidaten[0]["naam"], "Jan Janssen")
        self.assertEqual(kandidaten[4]["naam"], "Gert Gertsen")

    def test_add_stem(self):
        kandidaten = maak_kandidaten()
        kandidaten = add_stem(kandidaten, 1)
        self.assertEqual(kandidaten[0]["stemmen"], 1)
        self.assertEqual(kandidaten[1]["stemmen"], 0)

    def test_sorteer_kandidaten(self):
        kandidaten = maak_kandidaten()
        kandidaten[0]["stemmen"] = 5
        kandidaten[1]["stemmen"] = 3
        kandidaten = sorteer_kandidaten(kandidaten)
        self.assertEqual(kandidaten[0]["stemmen"], 5)
        self.assertEqual(kandidaten[1]["stemmen"], 3)

    def test_sorteer_kandidaten_op_naam(self):
        kandidaten = maak_kandidaten()
        kandidaten = sorteer_kandidaten_op_naam(kandidaten)
        self.assertEqual(kandidaten[0]["naam"], "Gert Gertsen")
        self.assertEqual(kandidaten[4]["naam"], "Piet Pietersen")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_kandidaten(self, mock_file):
        kandidaten = maak_kandidaten()
        save_kandidaten(kandidaten)
        mock_file().write.assert_any_call("1,Jan Janssen,0\n")
        mock_file().write.assert_any_call("5,Gert Gertsen,0\n")

if __name__ == "__main__":
    unittest.main()