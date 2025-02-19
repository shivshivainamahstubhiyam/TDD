def test_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1"):
        add("1,-1")

def test_multiple_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1,-2"):
        add("-1,-2,3")