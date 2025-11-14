import atexit
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ...settings import DB_CONFIG, POOL_SIZE, POOL_MAX_SIZE

DATABASE_URL = (
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
)

# Инициализация синхронного движка
engine = create_engine(
    DATABASE_URL,
    pool_size=POOL_SIZE,
    max_overflow=POOL_MAX_SIZE,
    echo=False,
    future=True
)

# Фабрика синхронных сессий
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def close_engine():
    engine.dispose()

def shutdown():
    try:
        close_engine()
    except Exception:
        pass

atexit.register(shutdown)
