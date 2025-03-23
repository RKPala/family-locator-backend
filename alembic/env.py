from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from config import DATABASE_URL  # ✅ Import from config.py
from models import Base  # ✅ Import Base to detect models

# Alembic Config object
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)  # ✅ Use database URL from config.py

# Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Use the metadata from models.py
target_metadata = Base.metadata  # ✅ Use Base.metadata for auto migrations

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    engine = create_engine(DATABASE_URL, poolclass=pool.NullPool)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()