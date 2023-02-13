from compare_versions import compare

assert compare("0.1", "1.1") == -1
assert compare("1.1", "1.2") == -1
assert compare("1.2", "1.2.9.9.9.9") == -1
assert compare("1.1", "1.10") == -1
assert compare("1.2", "1.1") == 1
assert compare("1.3.4", "1.3") == 1
assert compare("1.10", "1.2.9.9.9.9") == 1
assert compare("1.10", "1.10") == 0
assert compare("13.10.0", "13.10") == 0
assert compare("13.10.0.1", "13.10") == 1

print("tests passed")
