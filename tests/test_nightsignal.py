import pathlib
import unittest

from vito_algorithms import nightsignal as ns

SAMPLE_HR_DATA_1 = "sample_data/NightSignal/test/Orig_NonFitbit_HR.csv"
SAMPLE_HR_DATA_2 = "sample_data/NightSignal/test/P355472-AppleWatch-hr.csv"
NS_OUTPUT_PATH = "vito_algorithms/tmp/NS-signals.json"


class MyTestCase(unittest.TestCase):
    def test_getScore(self):
        hr_data_path = pathlib.Path(__file__).parent.parent.joinpath(pathlib.Path(SAMPLE_HR_DATA_1)).resolve()
        ns.getScore(hr_data_path)
        ns_output_path = pathlib.Path(__file__).parent.parent.joinpath(pathlib.Path(NS_OUTPUT_PATH))
        self.assertTrue(ns_output_path.is_file())


if __name__ == '__main__':
    unittest.main()