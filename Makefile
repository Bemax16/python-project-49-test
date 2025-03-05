install:
	uv sync

build:
	uv build

publish:
	uv pip publish --dry-run

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

brain-games:
	uv run brain-games

brain-even:
	uv venv exec python -m brain_games.scripts.brain_even

brain-calc:
	uv venv exec python -m brain_games.scripts.brain_calc

brain-gcd:
	uv venv exec python -m brain_games.scripts.brain_gcd

brain-progression:
	uv venv exec python -m brain_games.scripts.brain_progression

brain-prime:
	uv venv exec python -m brain_games.scripts.brain_prime
