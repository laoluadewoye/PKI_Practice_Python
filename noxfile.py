import nox


@nox.session(python=[f'3.{i}' for i in range(8, 15)])
def test_3_8_14(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "PKIPractice/tests")
