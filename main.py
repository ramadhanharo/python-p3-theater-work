from lib.crud import create_role, create_audition, get_all_roles, get_auditions_for_role, update_audition_hired_status, delete_audition


def main():
    # Create some roles
    print("Creating roles...")
    create_role("Nurse")
    create_role("Teacher")
    create_role("Pilot")

    # Create some auditions for these roles
    print("\nCreating auditions...")
    create_audition("ramadhan", "theatre 1", 1)  # nurse role ID = 1
    create_audition("abdi", "theatre 2", 1)  # teacher role ID = 1
    create_audition("jacob", "theatre 3", 2)  # pilot role ID = 2


    # Fetch and print all roles
    print("\nFetching all roles...")
    roles = get_all_roles()
    for role in roles:
        print(f"Role: {role.character_name}")

    # Fetch and print all auditions for the "teacher" role (ID = 1)
    print("\nFetching auditions for teacher...")
    auditions = get_auditions_for_role(1)
    for audition in auditions:
        print(f"Audition Actor: {audition.actor}, Location: {audition.location}")

    # Update an audition to hired (ID = 1)
    print("\nUpdating the first audition to 'hired' status...")
    update_audition_hired_status(1, True)

    # Delete an audition (ID = 2)
    print("\nDeleting audition ID 2...")
    delete_audition(2)

    # Final check on auditions
    print("\nFetching auditions after deletion...")
    auditions = get_auditions_for_role(1)
    for audition in auditions:
        print(f"Audition Actor: {audition.actor}, Location: {audition.location}")

if __name__ == '__main__':
    main()
