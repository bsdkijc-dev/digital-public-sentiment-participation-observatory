import sqlite3
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
SYNTH = BASE / "synthetic-data"

try:
    import duckdb
    HAS_DUCKDB = True
except ImportError:
    HAS_DUCKDB = False


def build_warehouse():
    csv_files = sorted(SYNTH.glob("*.csv"))
    if HAS_DUCKDB:
        db_path = BASE / "dsppo_pilot1.duckdb"
        con = duckdb.connect(str(db_path))
        for f in csv_files:
            tbl = f.stem
            con.execute(f"CREATE OR REPLACE TABLE {tbl} AS SELECT * FROM read_csv_auto('{f.as_posix()}')")
        count = con.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='main'").fetchone()[0]
        con.close()
        print(f"DuckDB warehouse built at {db_path.name} with {count} tables.")
    else:
        db_path = BASE / "dsppo_pilot1_fallback.sqlite"
        con = sqlite3.connect(str(db_path))
        for f in csv_files:
            df = pd.read_csv(f)
            df.to_sql(f.stem, con, if_exists="replace", index=False)
        con.close()
        print(f"DuckDB not installed in current env; SQLite fallback built at {db_path.name} with {len(csv_files)} tables.")


if __name__ == "__main__":
    build_warehouse()
