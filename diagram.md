

```mermaid
classDiagram
    class Pet {
        +String name
        +String breed
        +int age
        +String medical_notes
        +get_pet_info()
        +update_medical_notes()
    }

    class Owner {
        +String name
        +String phone_number
        +String email
        +String address
        +List pets
        +add_pet()
        +remove_pet()
        +view_scheduled_appointments()
    }

    class Walker {
        +String name
        +String phone_number
        +List availability
        +List assigned_walks
        +accept_walk()
        +complete_walk()
        +view_schedule()
    }

    class Walk {
        +String date
        +String time
        +int duration
        +String location
        +String status
        +schedule_walk()
        +cancel_walk()
        +mark_as_complete()
    }

    class DropOffPickUp {
        +String drop_off_time
        +String pick_up_time
        +String location
        +String status
        +schedule_drop_off()
        +schedule_pick_up()
        +cancel_appointment()
        +mark_as_complete()
    }

    class Scheduler {
        +List walks
        +List appointments
        +String today_date
        +get_todays_tasks()
        +filter_by_pet()
        +filter_by_walker()
        +check_availability()
    }

    class Notification {
        +String recipient
        +String message
        +String timestamp
        +String type
        +send_notification()
        +mark_as_read()
    }

    Owner "1" --> "many" Pet : owns
    Pet "1" --> "many" Walk : scheduled for
    Walker "1" --> "many" Walk : assigned to
    Owner "1" --> "many" DropOffPickUp : books
    Pet "1" --> "many" DropOffPickUp : dropped off
    Scheduler "1" --> "many" Walk : manages
    Scheduler "1" --> "many" DropOffPickUp : manages
    Scheduler "1" --> "1" Notification : sends
