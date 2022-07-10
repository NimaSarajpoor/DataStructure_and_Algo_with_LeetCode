from zigzag_convertor import zigzag_convertor


def test_singleletter():
    assert zigzag_convertor("s") == "s"


def test_singleRow():
    assert zigzag_convertor("simin") == "simin"

def test_twoRows():
    assert zigzag_convertor("simin", numRows=2) == "smnii"

def test_threeRows():
    assert zigzag_convertor("simin", numRows=3) == "sniim"


def test_sameLengthRows():
    s = "simin"
    assert zigzag_convertor(s, numRows=len(s)) == "simin"
