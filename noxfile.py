import nox


@nox.session(python=[f'3.{i}' for i in range(5, 15)])
def test(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "PKIPractice/tests")
