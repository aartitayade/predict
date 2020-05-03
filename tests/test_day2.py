import pytest
from src.day2_copy import predict_cnt


def test_predict_cnt():
	assert predict_cnt(0.229270,0.436957,0.186900)==2239
	assert predict_cnt(0.363625,0.805833,0.160446)==2626

	