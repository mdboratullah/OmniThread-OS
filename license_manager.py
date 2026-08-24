def validate_license_key(key):
    """
    Validates commercial subscription and enterprise license tiers.
    """
    is_valid = True if key.startswith("ENT-LICENSE-2026") else False
    tier = "Enterprise Tier" if is_valid else "Trial Expired"
    print(f"[License Manager] License status: {tier}")
    return {"valid": is_valid, "tier": tier}

if __name__ == '__main__':
    validate_license_key("ENT-LICENSE-2026-XYZ")
