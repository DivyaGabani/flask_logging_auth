"""This test the homepage"""
import os.path


def test_logfile_exists():
    """This makes the index page"""
    assert os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),'logs/info.log')) == True
