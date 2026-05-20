from typer.testing import CliRunner

from neural_notes.cli import app

runner = CliRunner()

def test_health_command() -> None:
    result = runner.invoke(app, ["health"])
    assert result.exit_code == 0
    assert "CLI is healthy!" in result.output