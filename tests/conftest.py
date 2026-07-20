from copy import deepcopy

import pytest

from src.app import activities


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset the shared in-memory activity database before each test."""
    original_activities = deepcopy(activities)

    activities.clear()
    activities.update(deepcopy(original_activities))

    yield

    activities.clear()
    activities.update(deepcopy(original_activities))
