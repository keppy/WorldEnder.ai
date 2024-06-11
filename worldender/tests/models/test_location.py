from worldender.models.location import Location

def test_location_destroy():
    # Create a parent location
    parent_location = Location(latitude=37.7749, longitude=-122.4194)

    # Create child locations
    child_location1 = Location(latitude=37.7749, longitude=-122.4194, parent=parent_location)
    child_location2 = Location(latitude=37.7749, longitude=-122.4194, parent=parent_location)

    # Add the child locations to the parent location
    parent_location.children.append(child_location1)
    parent_location.children.append(child_location2)

    # Destroy the parent location
    parent_location.destroy()

    # Check if the parent location and its children are marked as destroyed
    assert parent_location.destroyed is True
    assert child_location1.destroyed is True
    assert child_location2.destroyed is True