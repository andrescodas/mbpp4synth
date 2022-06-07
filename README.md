# A very brief description of this repo

This repo is obtained by exporting the [MBPP](https://github.com/google-research/google-research/blob/51b50d6d6d9290b20f6c042f78f847ccb9127720/mbpp/mbpp.jsonl) dataset to independent code and test files.

Some tests are renamed/moved due to an `ERROR` with standard pytest configurations.  See the pytest results:

```bash
pytest code_test/
```

outputs:
```bash
================================================================================= short test summary info =================================================================================
ERROR code_test/test_19_0.py::test_duplicate
ERROR code_test/test_19_1.py::test_duplicate
ERROR code_test/test_19_2.py::test_duplicate
ERROR code_test/test_46_0.py::test_distinct
ERROR code_test/test_46_1.py::test_distinct
ERROR code_test/test_46_2.py::test_distinct
ERROR code_test/test_801_0.py::test_three_equal
ERROR code_test/test_801_1.py::test_three_equal
ERROR code_test/test_801_2.py::test_three_equal
====================================================================== 2938 passed, 18 warnings, 9 errors in 16.97s =======================================================================
```

This is the renaming command:

```bash
mv code_test/test_19_0.py code_test/ERROR_test_19_0.py
mv code_test/test_19_1.py code_test/ERROR_test_19_1.py
mv code_test/test_19_2.py code_test/ERROR_test_19_2.py
mv code_test/test_46_0.py code_test/ERROR_test_46_0.py
mv code_test/test_46_1.py code_test/ERROR_test_46_1.py
mv code_test/test_46_2.py code_test/ERROR_test_46_2.py
mv code_test/test_801_0.py code_test/ERROR_test_801_0.py
mv code_test/test_801_1.py code_test/ERROR_test_801_1.py
mv code_test/test_801_2.py code_test/ERROR_test_801_2.py
```