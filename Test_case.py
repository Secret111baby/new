import pytest

def test_one():
    print("这是测试方法一")

def test_two():
    x = 'hello'
    assert 'h' in x
    print("Bingo")

def test_three():
    a = 1
    b = 5
    c =a + b
    assert c == 6
