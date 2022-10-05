import nox


@nox.session()
@nox.parametrize("tapas_version", [
    "1.0.2"
])
def tests(session, tapas_version):
    session.install("pytest")
    session.install(f"tapas=={tapas_version}")

    session.run("pytest", "tests")
