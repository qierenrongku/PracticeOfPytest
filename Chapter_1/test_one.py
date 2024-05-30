def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

##################
# (.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest .\test_one.py
# ============================================================= test session starts =============================================================
# platform win32 -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0
# rootdir: D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1
# collected 1 item                                                                                                                                

# test_one.py .                                                                                                                            [100%] 

# ============================================================== 1 passed in 0.02s ============================================================== 


# (.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest .\test_one.py -v
# ============================================================= test session starts =============================================================
# platform win32 -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0 -- d:\project\mypythonproject\python_howto\PracticeOfPytest\.venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1
# collected 1 item

# test_one.py::test_passing PASSED                                                                                                         [100%] 

# ============================================================== 1 passed in 0.03s ==============================================================

