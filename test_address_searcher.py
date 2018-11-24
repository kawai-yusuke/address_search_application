import unittest


class AdressSearcher():
    def search(self, postal_code):
        return "岩手県八幡平市大更"

class TestAdressSearcher(unittest.TestCase):
    def test_岩手県八幡平市大更を郵便番号から取得できる(self):
        address_seaecher = AdressSearcher()

        actual = address_seaecher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)



if __name__ == "__main__":
    unittest.main()
