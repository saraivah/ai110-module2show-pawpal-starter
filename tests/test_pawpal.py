from pawpal_system import Task, Pet

def test_task_completion():
    task = Task("Morning walk", "7:00 AM", "Daily")
    assert task.completed == False, "Task should start as incomplete"
    task.mark_complete()
    assert task.completed == True, "Task should be complete after mark_complete()"
    print("✅ test_task_completion passed!")

def test_task_addition():
    pet = Pet("Buddy", "Labrador", 3)
    assert len(pet.tasks) == 0, "Pet should start with no tasks"
    pet.add_task(Task("Morning walk",   "7:00 AM", "Daily"))
    pet.add_task(Task("Feed breakfast", "7:30 AM", "Daily"))
    pet.add_task(Task("Evening walk",   "6:00 PM", "Daily"))
    assert len(pet.tasks) == 3, "Pet should have 3 tasks after adding 3"
    print("✅ test_task_addition passed!")

if __name__ == "__main__":
    print("\n🧪 Running PawPal+ Tests...\n")
    test_task_completion()
    test_task_addition()
    print("\n🎉 All tests passed!\n")