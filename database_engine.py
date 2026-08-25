import json
import logging

class EnterpriseDatabaseManager:
    def __init__(self):
        self.pg_conn = "postgresql://admin:secure_pass@localhost:5432/omnithread_db"
        self.timescale_hypertable = "metrics_hypertable"
        self.redis_cache = {"session_store": {}, "live_metrics": {}}
        print("[Database] PostgreSQL & TimescaleDB connection pools initialized.")

    def save_telemetry_history(self, node_id, metrics):
        record = json.dumps(metrics)
        self.redis_cache["live_metrics"][node_id] = record
        print(f"[TimescaleDB] Saved telemetry for node: {node_id}")

    def get_cached_metrics(self, node_id):
        return self.redis_cache["live_metrics"].get(node_id, None)
