if __name__ == "__main__":
    raise SystemExit(
        "You're about to run an Attribute Module which is not allowed! Run the src/entrypoint.py instead!"
    )
else:
    from datetime import timedelta as timeConstraint
    from typing import Final

    _ALLOWABLE_TIME_TO_COMMIT: Final = timeConstraint(minutes=30)
