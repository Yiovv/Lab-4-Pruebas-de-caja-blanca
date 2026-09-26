import pytest
import process_grades

@pytest.mark.parametrize(
        'students, expected',
        [
            ([{'name':'Ana','grades': [90,90,90]}],['Ana']),
            
        ]
)

def test_process_grades_passed(students, expected):
    result=process_grades.process_grades(students)
    assert result['passed'] == expected


@pytest.mark.parametrize(
        'students, expected',
        [
            ([{'name':'Ana','grades': [60,60,60]}],'recovery'),
            
        ]
)

def test_process_grades_recovery(students, expected,capsys):
    result=process_grades.process_grades(students)
    captured = capsys.readouterr()
    assert expected in captured.out