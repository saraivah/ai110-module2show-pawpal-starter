from datetime import date


class Task:
    def __init__(self, description, time, frequency, completed=False):
        self.description = description
        self.time = time
        self.frequency = frequency
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.description} at {self.time} ({self.frequency})"

class Pet:
    def __init__(self, name, breed, age, medical_notes="None"):
        self.name = name
        self.breed = breed
        self.age = age
        self.medical_notes = medical_notes
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_pet_info(self):
        return {
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "medical_notes": self.medical_notes,
            "tasks": self.tasks
        }

    def update_medical_notes(self):
        pass

    def __str__(self):
        """Return a formatted string representation of the pet."""
        return f"{self.name} ({self.breed}, {self.age} years old) — {len(self.tasks)} tasks"


class Owner:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def view_scheduled_appointments(self):
        pass

    def __str__(self):
        """Return a formatted string representation of the pet."""
        return f"{self.name} ({self.breed}, {self.age} years old) — {len(self.tasks)} tasks"


class Walker:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.availability = []
        self.assigned_walks = []

    def accept_walk(self):
        pass

    def complete_walk(self):
        pass

    def view_schedule(self):
        pass

    def __str__(self):
        """Return a formatted string representation of the walker."""
        return f"{self.name} — {len(self.assigned_walks)} assigned walks"


class Walk:
    def __init__(self, date, time, duration, location, status):
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.status = status
        self.pet = None
        self.walker = None

    def schedule_walk(self):
        pass

    def cancel_walk(self):
        pass

    def mark_as_complete(self):
        pass

    def __str__(self):
        """Return a formatted string representation of the walk."""
        return f"Walk on {self.date} at {self.time} for {self.duration} minutes — {self.status}"

class DropOffPickUp:
    def __init__(self, drop_off_time, pick_up_time, location, status):
        self.drop_off_time = drop_off_time
        self.pick_up_time = pick_up_time
        self.location = location
        self.status = status
        self.pet = None
        self.owner = None

    def schedule_drop_off(self):
        pass

    def schedule_pick_up(self):
        pass

    def cancel_appointment(self):
        pass

    def mark_as_complete(self):
        pass


class Scheduler:
    def __init__(self):
        self.owners = []
        self.today = date.today()

    def add_owner(self, owner):
        self.owners.append(owner)

    def get_todays_tasks(self):
        pass

    def filter_by_pet(self):
        pass

    def filter_by_walker(self):
        pass

    def check_availability(self):
        pass

    def get_all_tasks(self):
        tasks = []
        for owner in self.owners:
            for pet in owner.pets:
                for task in pet.tasks:
                    tasks.append((owner.name, pet.name, task))
        return tasks

    def summary(self):
        total = len(self.get_all_tasks())
        done  = len(self.get_completed_tasks())
        left  = len(self.get_pending_tasks())
        print(f"\n📊 Summary: {total} total tasks | {done} complete | {left} pending")

    
    def get_completed_tasks(self):
     return [(owner, pet, task)
            for owner, pet, task in self.get_all_tasks()
            if task.completed]

    def get_pending_tasks(self):
     return [(owner, pet, task)
            for owner, pet, task in self.get_all_tasks()
            if not task.completed]


class Notification:
    def __init__(self, recipient, message, timestamp, type):
        self.recipient = recipient
        self.message = message
        self.timestamp = timestamp
        self.type = type

    def send_notification(self):
        pass

    def mark_as_read(self):
        pass