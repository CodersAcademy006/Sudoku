def update_achievements(errors, elapsed_time, achievements):
    """Update and display achievements."""
    if errors == 0 and elapsed_time < 300 and "Perfect Puzzle" not in achievements:
        achievements.append("Perfect Puzzle")
        return "Achievement Unlocked: Perfect Puzzle!"
    return None
