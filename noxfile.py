import nox


@nox.session(python=[f'3.{i}' for i in range(6, 8)])
def test_3_6_7(session):
    # Pip 23+ doesn't support Python 3.7 and earlier
    session.install("pip<23.0")

    session.install("-r", "requirements.txt")
    session.run("pytest", "PKIPractice/tests")


@nox.session(python=[f'3.{i}' for i in range(8, 15)])
def test_3_8_14(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "PKIPractice/tests")
