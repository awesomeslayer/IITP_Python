"""Tests for CLI."""

from _pytest.fixtures import FixtureFunction  # type: ignore
from click.testing import CliRunner  # type: ignore
import pytest

from fast_hough_transform import console


@pytest.fixture
def runner() -> CliRunner:
    """Runner fixtue for CLI."""
    return CliRunner()


def test_main_succeeds(runner: FixtureFunction) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
