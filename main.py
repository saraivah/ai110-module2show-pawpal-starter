from pawpal_system import Task, Pet, Owner, Scheduler

# ── Create owners ─────────────────────────────────────────────────────────────
owner1 = Owner("Sarah", "305-555-0101", "sarah@email.com")
owner2 = Owner("James", "305-555-0202", "james@email.com")

# ── Create pets ───────────────────────────────────────────────────────────────
dog  = Pet("Buddy",   "Labrador",       3)
cat  = Pet("Whiskers","Siamese",        5)
bird = Pet("Mango",   "Parrot",         2)

# ── Create tasks ──────────────────────────────────────────────────────────────
dog.add_task(Task("Morning walk",     "7:00 AM",  "Daily"))
dog.add_task(Task("Feed breakfast",   "7:30 AM",  "Daily"))
dog.add_task(Task("Give medication",  "9:00 AM",  "Weekly"))
dog.add_task(Task("Evening walk",     "6:00 PM",  "Daily"))

cat.add_task(Task("Feed breakfast",   "8:00 AM",  "Daily"))
cat.add_task(Task("Clean litter box", "10:00 AM", "Daily"))
cat.add_task(Task("Grooming",         "3:00 PM",  "Weekly"))

bird.add_task(Task("Feed seeds",      "8:30 AM",  "Daily"))
bird.add_task(Task("Clean cage",      "11:00 AM", "Weekly"))
bird.add_task(Task("Playtime",        "4:00 PM",  "Daily"))

# ── Assign pets to owners ─────────────────────────────────────────────────────
owner1.add_pet(dog)
owner1.add_pet(cat)
owner2.add_pet(bird)

# ── Set up scheduler ──────────────────────────────────────────────────────────
scheduler = Scheduler()
scheduler.add_owner(owner1)
scheduler.add_owner(owner2)

# ── Print Today's Schedule ────────────────────────────────────────────────────
from datetime import date

print()
print("=" * 50)
print(f"   🐾 PAWPAL+ — TODAY'S SCHEDULE")
print(f"   📅 {date.today().strftime('%A, %B %d %Y')}")
print("=" * 50)

current_owner = None
current_pet   = None

sorted_tasks = sorted(scheduler.get_all_tasks(), key=lambda x: x[2].time)

for owner_name, pet_name, task in sorted_tasks:
    if owner_name != current_owner:
        print(f"\n👤 Owner: {owner_name}")
        current_owner = owner_name
        current_pet   = None

    if pet_name != current_pet:
        print(f"  🐶 {pet_name}")
        current_pet = pet_name

    status = "✅" if task.completed else "⬜"
    print(f"      {status}  {task.time:<12} {task.description:<25} [{task.frequency}]")

print()
print("=" * 50)
scheduler.summary()
print()