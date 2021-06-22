'''task1
    1 please create your own git repository on github.
    2 (optional) setup pre-commit hook with black and isort formatting for the repo
    3 initialize .gitignore in the repository root (you can use this sample)
    4 create a homework1 directory in the repo
    5 then copy the sample_project into the directory.
    6 fix all bugs in the sample_project code
    7 write an extra test for each found bug

'''
def check_power_of_2(a: int) -> bool:
    return not (bool(a & (a - 1))) and a != 0