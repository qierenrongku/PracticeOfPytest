def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


# (.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest .\test_two.py
# ============================================================= test session starts =============================================================
# platform win32 -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0
# rootdir: D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1
# collected 1 item                                                                                                                                

# test_two.py F                                                                                                                            [100%]

# ================================================================== FAILURES =================================================================== 
# ________________________________________________________________ test_failing _________________________________________________________________ 

#     def test_failing():
# >       assert (1, 2, 3) == (3, 2, 1)
# E       assert (1, 2, 3) == (3, 2, 1)
# E
# E         At index 0 diff: 1 != 3
# E         Use -v to get more diff

# test_two.py:2: AssertionError
# =========================================================== short test summary info =========================================================== 
# FAILED test_two.py::test_failing - assert (1, 2, 3) == (3, 2, 1)
# ============================================================== 1 failed in 0.06s ============================================================== 



# (.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest .\test_two.py -v
# ====================================================================== test session starts ======================================================================
# platform win32 -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0 -- d:\project\mypythonproject\python_howto\PracticeOfPytest\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1
# collected 1 item

# test_two.py::test_failing FAILED                                                                                                                           [100%]

# =========================================================================== FAILURES ============================================================================ 
# _________________________________________________________________________ test_failing __________________________________________________________________________ 

#     def test_failing():
# >       assert (1, 2, 3) == (3, 2, 1)
# E       AssertionError: assert (1, 2, 3) == (3, 2, 1)
# E
# E         At index 0 diff: 1 != 3
# E
# E         Full diff:
# E           (
# E         +     1,
# E         +     2,...
# E
# E         ...Full output truncated (4 lines hidden), use '-vv' to show

# test_two.py:2: AssertionError
# ==================================================================== short test summary info ==================================================================== 
# FAILED test_two.py::test_failing - AssertionError: assert (1, 2, 3) == (3, 2, 1)
# ======================================================================= 1 failed in 0.07s ======================================================================= 