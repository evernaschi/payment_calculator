from main import main
import pytest

def test_main_ok(capsys):
    main()
    captured = capsys.readouterr()
    output = (
        "The amount to pay RENE is: 215.0 USD\n" 
        + "The amount to pay ASTRID is: 85.0 USD\n"
        + "The amount to pay JOHN is: 130.0 USD\n"
        + "The amount to pay MARY is: 100.0 USD\n"
        + "The amount to pay JAMES is: 105.0 USD\n"
        )
    assert captured.out == output

def test_main_err_1():
    with pytest.raises(Exception, match=r".*Format error in input file.*"):
        main("tests/input_err_1.txt")

def test_main_err_2():
    with pytest.raises(Exception, match=r".*Format error in Schedule.*"):
        main("tests/input_err_2.txt")

def test_main_err_3():
    with pytest.raises(Exception, match=r".*Format error in Schedule.*"):
        main("tests/input_err_3.txt")

def test_main_err_4():
    with pytest.raises(Exception, match=r".*Format error in time.*"):
        main("tests/input_err_4.txt")
