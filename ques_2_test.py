from unittest import TestCase
from ques_2 import Compensation


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.Compensation = Compensation("cur")

    def tearDown(self) -> None:
        self.Compensation = None

    def test_get_result(self):
        self.assertEqual(self.Compensation.total_compensation(), False)