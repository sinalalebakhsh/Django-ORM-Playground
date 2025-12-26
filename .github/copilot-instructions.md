## Copilot / AI Agent Instructions — Django ORM Playground

Purpose: Help AI coding agents become productive quickly in this repository (a small Django project used as an ORM lab).

- Big picture:
  - Single Django project at `orm_playground/` with one app `playground`.
  - Models are intentionally split per-file under `playground/models/` (e.g. `product.py`, `user.py`, `order.py`). Import them centrally in `playground/models/__init__.py`.
  - The project demonstrates ORM patterns (bulk `update()` with `F()`, `select_related`, `select_for_update`, `Subquery`/`OuterRef`, and transactions).

- Key files to inspect for intent and examples:
  - `orm_playground/settings.py` — DB and debug configuration (note: default DB block is MySQL-style; a `db.sqlite3` file is present in the repo root for quick local runs).
  - `playground/models/*.py` — model definitions (follow the per-model file pattern).
  - `playground/views.py` — canonical examples of ORM usage (F() updates, `select_related`, `Subquery`, and transaction usage).
  - `playground/migrations/` — existing migrations; add new migrations when models change.

- Project-specific conventions and patterns:
  - Models: create one class per file in `playground/models/` and add an import to `playground/models/__init__.py`.
  - Foreign keys commonly reference app-qualified names (e.g. `'playground.Category'`) — follow that string-style in cross-file references.
  - Prefer ORM set-based updates using `F()` (see `playground/views.py` for examples) instead of Python loops that call `.save()` repeatedly.
  - Avoid N+1 by using `select_related()` for FK and `prefetch_related()` for M2M/related sets; the codebase uses `select_related('category')` in examples.
  - Use `transaction.atomic()` and `select_for_update()` when modeling concurrent updates (example in `playground/views.py`).

- How to run locally (quick):
  1. Install dependencies: project uses `Pipfile`. Recommended: `pip install pipenv && pipenv install` or use a virtualenv and `pip install -r requirements.txt` if you export one.
  2. Activate environment: `pipenv shell` (or activate your venv).
  3. Apply migrations (or use included `db.sqlite3` for read-only exploration):
     - `python manage.py makemigrations`
     - `python manage.py migrate`
  4. Run server: `python manage.py runserver`
  5. Run tests: `python manage.py test playground`

- Migrations & DB notes:
  - There are existing migrations in `playground/migrations/` — keep them in sync when changing models.
  - `settings.py` contains a MySQL example; the repository contains `db.sqlite3` suitable for quick experiments. Confirm DB settings before running destructive actions.

- Pull requests / code edits guidance for agents:
  - When adding models: add the file to `playground/models/`, import it in `playground/models/__init__.py`, then generate & include migrations.
  - When changing query logic, prefer set-based ORM (F, annotate, Subquery) and reference `playground/views.py` for idiomatic patterns.
  - Tests: add or update tests under `playground/tests.py` or create a `tests/` folder in the app.

- Examples to copy from:
  - F() update: `Product.objects.filter(category__name="Electronics").update(price=F("price") * 1.1)` (`playground/views.py`)
  - Annotate with subquery: `Category.objects.annotate(top_product_name=Subquery(...))` (`playground/views.py`)
  - Atomic + select_for_update pattern: see the `transaction.atomic()` + `select_for_update()` snippet in `playground/views.py`.

If anything in this summary is unclear or you want more examples (tests, more code locations), tell me which area to expand and I'll iterate.
