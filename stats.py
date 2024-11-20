def update_statistics(time_spent, errors, difficulty):
    """Track game statistics."""
    stats = {
        "time": time_spent,
        "errors": errors,
        "difficulty": difficulty
    }
    # Save stats to file or database
    return stats