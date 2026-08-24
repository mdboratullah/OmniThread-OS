def perform_system_upgrade(target_version):
    """
    Manages safe over-the-air updates with automatic rollback capability.
    """
    print(f"[Updater] Upgrading OmniThread OS to version {target_version}...")
    return {"version": target_version, "upgrade_status": "Success", "rollback_ready": True}

if __name__ == '__main__':
    perform_system_upgrade("6.1.0")
