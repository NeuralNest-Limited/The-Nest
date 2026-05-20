"""Allow ``python -m nest_cli`` to invoke the CLI entry point."""

from .cli import app


if __name__ == "__main__":  # pragma: no cover
    app()
