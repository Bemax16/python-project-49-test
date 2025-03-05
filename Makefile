install:
	uv venv create
	uv pip install --editable .

build:
	uv pip wheel --wheel-dir=dist .

publish:
	uv pip publish --dry-run

package-install:
	uv pip install dist/*.whl

lint:
	uv pip run ruff check brain_games

brain-games:
	uv venv exec python -m brain_games.scripts.brain_games

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
