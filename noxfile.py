import nox


@nox.session(python=["3.10", "3.11", "3.12", "3.13"])
def test(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "PKIPractice/tests")
