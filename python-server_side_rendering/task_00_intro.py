#!/var/bin/python3
import logging  # for reporting errors
import os

def generate_invitations(template, attendees):
    """
    Python function that generates personalized invitation
    files from a template with placeholders and a list of objects.
    
    Keyword arguments:
    argument : 
        template: template with placeholder
        attendees : list of attendees object
    Return: 1 if unsuccessful else write to file
    """
    if not isinstance(template, str):
        logging.error("Template is not string")
        return
    if not isinstance(attendees, list):
        logging.error("Attendees list is not list ")
        return
    # if not isinstance( attendee in attendees, dict):
    if not all(isinstance(a, dict) for a in attendees):
        logging.error("Attendees list is not a list of dictionaries")

    # if template is None:
    # if template.strip() is None:
    if not template.strip():
        logging.error("template is empty")
        return
    
    if not attendees:
        logging.error("Attendees list is empty")
        return
    
    count= 1
    for attendee in attendees:
        # name = attendee.get("name", "N/A")
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"      

        print(f"{name}  {event_title}  {event_date}  {event_location}\n")        
        # print(template) for debugging

        invite = template.replace("{name}", name) .replace("{event_title}", event_title)\
        .replace("{event_date}", event_date) . replace("{event_location}", event_location)
        # invite = invite.replace("{event_date}", event_date) for debugging 
        # print(invite) for debugging

        filename= f"output_{count}.txt"       
    
    
        if os.path.exists(filename):
            with open(filename, "a") as f:
                f.write(invite)
        else:       
            with open(filename, 'w') as f:
                f.write(invite)
        count+= 1 
    
if __name__ == "__main__":

    template = """
    
    Hello {name},

    You are invited to the {event_title} on {event_date} at {event_location}.

    We look forward to your presence.

    Best regards,
    Event Team
    """
    attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}]

    generate_invitations(template, attendees)