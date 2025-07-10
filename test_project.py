import project
import pytest


def main():
    test_seven_days()
    test_month()
    test_invalid_week()
    test_invalid_month()


def test_seven_days():
    assert project.get_week(1) == "Sunday"
    assert project.get_week(2) == "Monday"
    assert project.get_week(3) == "Tuesday"
    assert project.get_week(4) == "Wednesday"
    assert project.get_week(5) == "Thursday"
    assert project.get_week(6) == "Friday"
    assert project.get_week(7) == "Saturday"


def test_month():
    assert project.month(1) == "January"
    assert project.month(2) == "February"
    assert project.month(3) == "March"
    assert project.month(4) == "April"
    assert project.month(5) == "May"
    assert project.month(6) == "June"
    assert project.month(7) == "July"
    assert project.month(8) == "August"
    assert project.month(9) == "September"
    assert project.month(10) == "October"
    assert project.month(11) == "November"
    assert project.month(12) == "December"


def test_invalid_week():
    with pytest.raises(KeyError):
        project.get_week(0)
    with pytest.raises(KeyError):
        project.get_week(8)


def test_invalid_month():
    with pytest.raises(KeyError):
        project.month(0)
    with pytest.raises(KeyError):
        project.month(13)


if __name__ == "__main__":
    main()
