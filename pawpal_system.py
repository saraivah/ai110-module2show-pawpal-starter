class Pet:
    def __init__(self, name, breed, age, medical_notes):
        self.name = name
        self.breed = breed
        self.age = age
        self.medical_notes = medical_notes

    def get_pet_info(self):
        pass

    def update_medical_notes(self):
        pass


class Owner:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.pets = []

    def add_pet(self):
        pass

    def remove_pet(self):
        pass

    def view_scheduled_appointments(self):
        pass


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
        self.walks = []
        self.appointments = []
        self.today_date = None

    def get_todays_tasks(self):
        pass

    def filter_by_pet(self):
        pass

    def filter_by_walker(self):
        pass

    def check_availability(self):
        pass


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