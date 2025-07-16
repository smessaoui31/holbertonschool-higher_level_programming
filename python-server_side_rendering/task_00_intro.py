import os

def generate_invitations(template, attendees):
    # Vérification des types
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    # Vérification template vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Vérification liste vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Traitement de chaque invité
    for index, attendee in enumerate(attendees, start=1):
        # Copie du template
        personalized = template

        # Remplacement des placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) or "N/A"
            personalized = personalized.replace(f"{{{key}}}", value)

        filename = f"output_{index}.txt"

        # Vérification si le fichier existe déjà
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists and will be overwritten.")

        # Écriture du fichier avec gestion des erreurs
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(personalized)
            print(f"Generated: {filename}")
        except Exception as e:
            print(f"Error writing {filename}: {e}")
