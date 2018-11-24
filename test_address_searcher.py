import unittest

from address_searcher import AdressSearcher


class TestAdressSearcher(unittest.TestCase):
    def test_岩手県八幡平市大更を郵便番号から取得できる(self):
        address_seaecher = AdressSearcher()

        actual = address_seaecher.search(postal_code="0287111")

        self.assertEqual("岩手県八幡平市大更", actual)

    def test_東京都練馬区豊玉南を郵便番号から取得できる(self):
        address_seaecher = AdressSearcher()

        actual = address_seaecher.search(postal_code="1760014")

        self.assertEqual("東京都練馬区豊玉南", actual)

    def test_郵便番号がない場合(self):
        address_searcher = AdressSearcher()

        actual = address_searcher.search

        self.assertEqual("該当する郵便番号は見つかりません", actual)

if __name__ == "__main__":
    unittest.main()
