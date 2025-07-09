from tkinter import *
from datetime import datetime
import calendar
import csv
from tkinter import messagebox


def main():
    display_calendar()
    display_events()


root = Tk()
root.title("Calendar App")
root.geometry("2000x1200")
frame_1 = Frame(root, bg="#B4D4FF")
current_month = datetime.now().month
current_year = datetime.now().year


def get_week(day):
    week = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return week[day]


def month(m):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months[m]


def update_month():
    button_month.config(text=month(current_month))


def update_year():
    button_year.config(text=current_year)


def next_button():
    global current_month, current_year
    if current_month + 1 > 12:
        current_month = 1
        current_year += 1
        update_year()
    else:
        current_month += 1
    update_month()
    display_calendar()
    display_events()


def previous_button():
    global current_month, current_year
    if (current_month - 1) < 1:
        current_month = 12
        current_year -= 1
        update_year()
    else:
        current_month -= 1
    update_month()
    display_calendar()
    display_events()


calendar_frame = Frame(frame_1)
calendar_frame.place(relx=0.25, rely=0.3)

for i in range(1):
    for j in range(7):
        week = Button(calendar_frame, text= get_week(j+1), bg="#87B1EB",
                      fg="white", relief=RAISED, height=1, width=10, font=("Comic Sans MS", 8, "bold"))
        week.grid(row=i, column=j, ipadx=30, ipady=1)

calendar_frame_2 = Frame(frame_1, bg="#B4D4FF")
calendar_frame_2.place(relx=0.25, rely=0.39)


def display_calendar():
    global current_month, current_year
    first_day, total_days = calendar.monthrange(current_year, current_month)
    first_day = (first_day + 1) % 7
    day = 1

    for widgets in calendar_frame_2.winfo_children():
        widgets.destroy()

    for i in range(5):
        for j in range(7):
            day_cell = i*7 + j
            if i % 2 == 0 and j % 2 == 0:
                bg_widget = "#BFCDFB"
            elif i % 2 != 0 and j % 2 != 0:
                bg_widget = "#FFFFFF"
            else:
                bg_widget = "#DCE6FB"

            if day_cell < first_day:
                btn = Button(calendar_frame_2, text="", bg=bg_widget,
                             relief=FLAT, height=3, width=10)
            elif day <= total_days:
                btn = Button(calendar_frame_2, text=str(day), bg=bg_widget, relief=FLAT, height=3,
                             width=10, command=lambda current_day=day: create_pop_up(current_day))
                day += 1
            else:
                btn = Button(calendar_frame_2, text="", bg=bg_widget,
                             relief=FLAT, height=3, width=10)

            btn.grid(row=i, column=j, ipadx=30, ipady=2, sticky="nsew")


plus_month_button = Button(frame_1, text=">", fg="#87B1EB",
                           command=next_button, font=("Helvetica", 10, "bold"), relief=FLAT)
plus_month_button.place(relx=0.94, rely=0.2)

button_month = Button(frame_1, text=month(current_month), bg="#87B1EB", fg="white",
                      width=10, font=("Comic Sans MS", 8, "bold"), command=update_month)
button_month.place(relx=0.51, rely=0.2)

button_year = Button(frame_1, text=current_year, bg="#87B1EB",
                     fg="white", font=("Comic Sans MS", 8, "bold"))
button_year.place(relx=0.65, rely=0.2)

minus_month_button = Button(frame_1, text="<", fg="#87B1EB",
                            command=previous_button, font=("Helvetica", 10, "bold"), relief=FLAT)
minus_month_button.place(relx=0.23, rely=0.2)

pop_up = Frame(frame_1, bg="#87B1EB", height=800, width=250)
pop_up.place(relheight=0, relwidth=0)

pop_up_state = False


def collapsible_button():
    global pop_up_state, pop_up
    if pop_up_state == False:
        pop_up.place(relheight=1, relwidth=0.2)
        pop_up_state = True
    else:
        pop_up.place(relheight=0, relwidth=0)
        pop_up_state = False


hamburger_button = Button(frame_1, text="☰", fg="#FFFFFF", bg="#87B1EB",
                          relief=FLAT, command=lambda: collapsible_button(), font=(10))
hamburger_button.place(relx=0.001, rely=0.001)

events_label = Label(pop_up, text="Events", fg="#FFFFFF",
                     bg="#87B1EB", font=("Helvetica", 10, "bold"))
events_label.place(relx=0.1, rely=0.1)


def create_pop_up(current_day):
    current_date = f"{current_day}-{current_month}-{current_year}"
    pop_window = Toplevel(root, bg="#87B1EB")
    pop_window.title("ADD EVENTS")
    pop_window.geometry("300x400")
    pop_window.resizable(False, False)

    current_date_label = Label(pop_window, text=current_date, fg="#FFFFFF",
                               bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    current_date_label.place(relx=0.3, rely=0.01)

    event_name_label = Label(pop_window, text="Event Name", fg="#FFFFFF",
                             bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    event_name_label.place(relx=0.3, rely=0.1)

    enter_name = Entry(pop_window, width=30)
    enter_name.place(relx=0.1, rely=0.17)

    time_label = Label(pop_window, text="Time", fg="#FFFFFF",
                       bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    time_label.place(relx=0.3, rely=0.23)

    enter_time = Entry(pop_window, width=30)
    enter_time.place(relx=0.1, rely=0.3)

    venue_label = Label(pop_window, text="Venue", fg="#FFFFFF",
                        bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    venue_label.place(relx=0.4, rely=0.36)

    enter_venue = Entry(pop_window, width=30)
    enter_venue.place(relx=0.1, rely=0.43)

    remarks_label = Label(pop_window, text="Remarks", fg="#FFFFFF",
                          bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    remarks_label.place(relx=0.4, rely=0.5)

    enter_remarks = Entry(pop_window, width=30)
    enter_remarks.place(relx=0.1, rely=0.57)

    submit_btn = Button(pop_window, text="Add Event", fg="#FFFFFF", bg="#87B1EB", font=("Comic Sans MS", 9, "bold"), relief=FLAT, command=lambda: database(
        pop_window, current_date, enter_name.get().strip(), enter_time.get().strip(), enter_venue.get().strip(), enter_remarks.get().strip()))
    submit_btn.place(relx=0.35, rely=0.7)


def database(mini_pop_up, date, event_name, time, venue, remarks):
    with open("database.csv", "a", newline="") as file:
        csv_writer = csv.DictWriter(
            file, fieldnames=["Date", "Event_Name", "Event_Time", "Event_Venue", "Event_Remarks"])
        file.seek(0,2)
        if file.tell() == 0:
            csv_writer.writeheader()
        if time == "":
            time = "All Day"
        if venue == "":
            venue = "No location specified"

        if event_name:
            records = {"Date": date, "Event_Name": event_name, "Event_Time": time,
                       "Event_Venue": venue, "Event_Remarks": remarks}
            csv_writer.writerow(records)
        mini_pop_up.destroy()
        display_events()


def display_events():
    events_listbox.delete(0, END)
    current_events = []
    try:
        with open("database.csv", "r", newline="") as file:
            csv_reader = csv.DictReader(file)
            sorted_data = sorted(csv_reader, key=lambda x: x['Date'])
            for details in sorted_data:
                date = details["Date"].split("-")
                month, year = int(date[1]), int(date[2])
                if month == current_month and year == current_year:
                    current_events.append(
                        f"{details['Date']} ~ {details['Event_Name']} ~ {details['Event_Time']} ~ {details['Event_Venue']} ~ {details['Event_Remarks']}")

            if not current_events:
                events_listbox.insert(END, "No events for this month.")

            else:
                for events in current_events:
                    events_listbox.insert(END, events)
    except FileNotFoundError as e:
        events_listbox.insert(END, "No events for this month.")


def rewrite_data(deleted_event):
    records = []
    try:
        with open("database.csv", "r", newline="") as file:
            csv_reader = csv.DictReader(file)
            sorted_data = sorted(csv_reader, key=lambda x: x['Date'])
            for details in sorted_data:
                event_format = f"{details['Date']} ~ {details['Event_Name']} ~ {details['Event_Time']} ~ {details['Event_Venue']} ~ {details['Event_Remarks']}"
                if event_format != deleted_event:
                    records.append(details)
    except FileNotFoundError:
        pass

    with open("database.csv", "w", newline="") as file:
        csv_writer = csv.DictWriter(
            file, fieldnames=["Date", "Event_Name", "Event_Time", "Event_Venue", "Event_Remarks"])
        csv_writer.writeheader()
        csv_writer.writerows(records)

    display_events()


def mode(mode_title, date, event_name, time, venue, remarks, edit_event=None):
    pop_window = Toplevel(root, bg="#87B1EB")
    pop_window.title(mode_title)
    pop_window.geometry("300x400")
    pop_window.resizable(False, False)

    current_date_label = Label(pop_window, text=date, fg="#FFFFFF",
                               bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    current_date_label.place(relx=0.3, rely=0.01)

    event_name_label = Label(pop_window, text="Event Name", fg="#FFFFFF",
                             bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    event_name_label.place(relx=0.3, rely=0.1)

    enter_name = Entry(pop_window, width=30)
    enter_name.place(relx=0.1, rely=0.17)
    enter_name.insert(0, event_name)

    time_label = Label(pop_window, text="Time", fg="#FFFFFF",
                       bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    time_label.place(relx=0.3, rely=0.23)

    enter_time = Entry(pop_window, width=30)
    enter_time.place(relx=0.1, rely=0.3)
    enter_time.insert(0, time)

    venue_label = Label(pop_window, text="Venue", fg="#FFFFFF",
                        bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    venue_label.place(relx=0.4, rely=0.36)

    enter_venue = Entry(pop_window, width=30)
    enter_venue.place(relx=0.1, rely=0.43)
    enter_venue.insert(0, venue)

    remarks_label = Label(pop_window, text="Remarks", fg="#FFFFFF",
                          bg="#87B1EB", font=("Comic Sans MS", 9, "bold"))
    remarks_label.place(relx=0.4, rely=0.5)

    enter_remarks = Entry(pop_window, width=30)
    enter_remarks.place(relx=0.1, rely=0.57)
    enter_remarks.insert(0, remarks)

    if mode_title == "Edit":
        submit_btn = Button(pop_window, text="Add Event", fg="#FFFFFF", bg="#87B1EB", font=("Comic Sans MS", 9, "bold"), relief=FLAT, command=lambda: edit(
            pop_window, date, enter_name.get().strip(), enter_time.get().strip(), enter_venue.get().strip(), enter_remarks.get().strip(), edit_event))
        submit_btn.place(relx=0.35, rely=0.7)


def view_event():
    event_selected = events_listbox.curselection()
    if event_selected:
        event = events_listbox.get(event_selected)
        date, event_name, event_time, event_venue, event_remarks = event.split("~")
        mode("View", date, event_name, event_time, event_venue, event_remarks)

    else:
        messagebox.showwarning("error", "Select an event to edit")


def edit_func():
    event_selected = events_listbox.curselection()
    if event_selected:
        edit_event = events_listbox.get(event_selected)
        date, event_name, event_time, event_venue, event_remarks = edit_event.split("~")
        mode("Edit", date, event_name, event_time, event_venue, event_remarks, edit_event)

    else:
        messagebox.showwarning("error", "Select an event to edit")


def delete_event():
    event_selected = events_listbox.curselection()
    if event_selected:
        deleted_event = events_listbox.get(event_selected)
        events_listbox.delete(ANCHOR)
        rewrite_data(deleted_event)
    else:
        messagebox.showwarning("error", "Select an event to delete")


def edit(pop_window, date, name, time, venue, remarks, old_event):
    database(pop_window, date, name, time, venue, remarks)
    rewrite_data(old_event)
    display_events()


events_listbox = Listbox(pop_up, fg="#FFFFFF", bg="#87B1EB",
                         width=35, height=35, relief=SUNKEN, bd=0)
events_listbox.place(relx=0.1, rely=0.15)

edit_btn = Button(pop_up, text="Edit", fg="#FFFFFF", bg="#87B1EB",
                  command=edit_func, relief=FLAT, font=("Helvetica", 10, "bold"))
edit_btn.place(relx=0.1, rely=0.85)

delete_btn = Button(pop_up, text="Delete", fg="#FFFFFF", bg="#87B1EB",
                    command=delete_event, relief=FLAT, font=("Helvetica", 10, "bold"))
delete_btn.place(relx=0.4, rely=0.85)

view_btn = Button(pop_up, text="View", fg="#FFFFFF", bg="#87B1EB",
                  command=view_event, relief=FLAT, font=("Helvetica", 10, "bold"))
view_btn.place(relx=0.7, rely=0.85)

if __name__ == "__main__":
    main()
    frame_1.pack(fill="both", expand=True)
    root.mainloop()
