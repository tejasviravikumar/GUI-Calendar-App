# Calendar App
#### Video Demo:  [GUI Calendar](https://youtu.be/Dm8ZdF0ZH-M)
#### Description
This is my cs50p final project , I have created a calendar using GUI with the help of ```tkinter``` module . It enable users to view a monthly calendar and easily manage tasks. The app displays the current month and a grid calendar. Users can press the ```<``` previous button and  ```>``` next button to navigate months. When the user clicks a day it opens a pop up window , and asks for event name , time , venue , and remarks. When the user clicks ```☰``` button , they can view all the events entered by the user. Only they current month details are shown and at the bottom ```edit``` , ```view``` and  ```delete``` buttons are available. The user can select any of the event to perform the operations. The details entered are stored in a csv file.

#### Features
+ __View__: The user can click an event on the list box to view the event details clearly.

+ __Edit__: The user can click any events from the list box to edit an event.

+ __Delete__: The user can remove an event from the list box simply by clicking an event and press the delete button.

+ __CSV Storage__: The event details are stored in a file called ```database.csv``` in this format:
                                      `Title, Description, Venue, Time, Date`
The `Date` is stored in `DD-MM-YYYY` format.

#### Libraries
 `tkinter` – for building the graphical user interface (GUI).

 `datetime` – to get current date, month, and year.

 `calendar` – to get month structure (days, weeks, etc.).

 `csv` – to store and retrieve event data from a CSV file.

#### Installing Libraries
To install all the required libraries for this project, run:

```
pip install -r requirements.txt
```

#### Test Cases

`test_seven_days()`
A nested for loop is used to display all the days in a week , it calls the function ```get_week()``` and passes a number as an argument. The function ```get_week()``` returns the day associated with the number passed to the function. ```test_seven_days()``` it checks whether the intended day in returned when a number is passed.

`test_month()`
To display all the months in a year , it calls the function ```month()``` and a number is passed as an argument. The function ```month()``` returns the month associated with the number passed to the function. ```test_month()``` it checks whether the intended month in returned when a number is passed.

#### CSV File
In a file called ```database.csv``` , all the event details are stored. By using ```csv.DictWriter``` the event details are written to the ```database.csv``` and ```csv.DictReader``` to fetch the details to be displayed on the calendar.  When the user clicks delete the event details is overwritten on the same file except the event to be deleted and if the user clicks edit the event details are written to the file and the old event details is removed from the ```database.csv```

### Author: Tejasvi R

