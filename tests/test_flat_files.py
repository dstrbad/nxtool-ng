import unittest

from nxapi.log_providers import flat_file


class TestParseLog(unittest.TestCase):
    def test_show_stats(self):
        parser = flat_file.FlatFile()
        stats = parser.get_statistics()
        print stats
        assert True

