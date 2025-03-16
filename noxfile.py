"""
Nox testing file.
"""

import nox


@nox.session(python=[f'3.{i}' for i in range(9, 15)])
def test_project(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "PKIPractice/tests")
