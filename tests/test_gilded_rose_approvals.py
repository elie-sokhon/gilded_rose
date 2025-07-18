import io
import os
import sys

from approvaltests import verify
from approvaltests.reporters import PythonNativeReporter

from texttest_fixture import main

# insérer le dossier parent dans sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

reporter = PythonNativeReporter()


def test_gilded_rose_approvals():
    orig_sysout = sys.stdout
    try:
        fake_stdout = io.StringIO()
        sys.stdout = fake_stdout
        sys.argv = ["texttest_fixture.py", 30]
        main()
        answer = fake_stdout.getvalue()
    finally:
        sys.stdout = orig_sysout

    verify(answer, reporter=reporter)


if __name__ == "__main__":
    test_gilded_rose_approvals()
