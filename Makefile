
install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make-lint:
	poetry run flake8 brain_games

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
