import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾")

# ── Initialize session state ──────────────────────────────────────────────────
if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Sarah", "305-555-0101", "sarah@email.com")
    st.session_state.scheduler.add_owner(st.session_state.owner)

owner     = st.session_state.owner
scheduler = st.session_state.scheduler

# ── Title ─────────────────────────────────────────────────────────────────────
st.title("🐾 PawPal+")
st.caption("Your personal pet care scheduler.")

# ── Sidebar: Add a Pet ────────────────────────────────────────────────────────
st.sidebar.header("➕ Add a Pet")

pet_name  = st.sidebar.text_input("Pet Name")
pet_breed = st.sidebar.text_input("Breed")
pet_age   = st.sidebar.number_input("Age", min_value=0, max_value=30, step=1)
pet_notes = st.sidebar.text_input("Medical Notes (optional)")

if st.sidebar.button("Add Pet"):
    if pet_name.strip() == "":
        st.sidebar.error("Please enter a pet name.")
    elif any(p.name.lower() == pet_name.lower() for p in owner.pets):
        st.sidebar.error(f"{pet_name} already exists.")
    else:
        new_pet = Pet(pet_name, pet_breed, pet_age, pet_notes or "None")
        owner.add_pet(new_pet)
        st.sidebar.success(f"✅ {pet_name} added!")
        st.rerun()

# ── Sidebar: Add a Task ───────────────────────────────────────────────────────
st.sidebar.header("📋 Schedule a Task")

if owner.pets:
    selected_pet  = st.sidebar.selectbox("Select Pet", [p.name for p in owner.pets])
    task_desc     = st.sidebar.text_input("Task Description")
    task_time     = st.sidebar.time_input("Time")
    task_freq     = st.sidebar.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])

    if st.sidebar.button("Add Task"):
        if task_desc.strip() == "":
            st.sidebar.error("Please enter a task description.")
        else:
            pet = owner.get_pet(selected_pet)
            task_time_str = task_time.strftime("%I:%M %p")
            pet.add_task(Task(task_desc, task_time_str, task_freq))
            st.sidebar.success(f"✅ Task added for {selected_pet}!")
            st.rerun()
else:
    st.sidebar.info("Add a pet first to schedule tasks.")

# ── Main: Today's Schedule ────────────────────────────────────────────────────
st.subheader("📅 Today's Schedule")

all_tasks = scheduler.get_all_tasks()

if not all_tasks:
    st.info("No tasks yet. Add a pet and schedule some tasks!")
else:
    sorted_tasks = sorted(all_tasks, key=lambda x: x[2].time)
    current_pet  = None

    for owner_name, pet_name, task in sorted_tasks:
        if pet_name != current_pet:
            st.markdown(f"### 🐶 {pet_name}")
            current_pet = pet_name

        col1, col2 = st.columns([4, 1])
        with col1:
            status = "✅" if task.completed else "⬜"
            st.write(f"{status} **{task.time}** — {task.description} `{task.frequency}`")
        with col2:
            if not task.completed:
                if st.button("Done", key=f"{pet_name}_{task.description}"):
                    scheduler.mark_task_complete(pet_name, task.description)
                    st.rerun()

# ── Main: Summary ─────────────────────────────────────────────────────────────
st.divider()
total = len(scheduler.get_all_tasks())
done  = len(scheduler.get_completed_tasks())
left  = len(scheduler.get_pending_tasks())

col1, col2, col3 = st.columns(3)
col1.metric("Total Tasks",     total)
col2.metric("Completed",       done)
col3.metric("Pending",         left)

# ── Main: Pets Overview ───────────────────────────────────────────────────────
st.divider()
st.subheader("🐾 Your Pets")

if not owner.pets:
    st.info("No pets added yet.")
else:
    for pet in owner.pets:
        with st.expander(f"{pet.name} — {pet.breed}, {pet.age} yrs"):
            st.write(f"**Medical Notes:** {pet.medical_notes}")
            st.write(f"**Total Tasks:** {len(pet.tasks)}")
            st.write(f"**Pending:** {len(pet.get_pending_tasks())}")
            st.write(f"**Completed:** {len(pet.get_completed_tasks())}")
            if st.button(f"Remove {pet.name}", key=f"remove_{pet.name}"):
                owner.remove_pet(pet.name)
                st.rerun()