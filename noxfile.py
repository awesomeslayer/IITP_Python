import tempfile

import nox
from nox_poetry import session


nox.options.sessions = "lint", "safety", "tests"

locations = "src", "tests", "noxfile.py"
PYTHON_VERSIONS = ["3.11", "3.10", "3.9", "3.8"]


@session(python=PYTHON_VERSIONS)
def tests(session):
    args = session.posargs or ["--cov"]
    session.run_always("poetry", "install", external=True)
    session.run("pytest", *args)


@session(python=PYTHON_VERSIONS)
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@session(python="3.11")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with",
            "dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.11")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
