from zigzag_convertor import zigzag_convertor


def test_singleletter():
    assert zigzag_convertor("s") == "s"


def test_singleRow():
    assert zigzag_convertor("simin") == "simin"

def test_twoRows():
    assert zigzag_convertor("simin") == "smnii"

def test_threeRows():
    assert zigzag_convertor("simin") == "sniim"
