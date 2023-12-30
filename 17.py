from datetime import datetime

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.projects = []

    def log_hours(self, project, hours, date):
        project.log_time(self, hours, date)

    def generate_timesheet(self, start_date, end_date):
        timesheet = f"Timesheet for {self.name} ({start_date} to {end_date}):\n"
        total_hours = 0

        for project in self.projects:
            project_timesheet = project.generate_project_timesheet(self, start_date, end_date)
            if project_timesheet:
                timesheet += project_timesheet
                total_hours += project.get_total_hours(self, start_date, end_date)

        timesheet += f"\nTotal Hours: {total_hours}"
        return timesheet


class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.time_entries = []

    def log_time(self, employee, hours, date):
        time_entry = TimeEntry(employee, hours, date)
        self.time_entries.append(time_entry)
        if employee not in employee.projects:
            employee.projects.append(self)

    def generate_project_timesheet(self, employee, start_date, end_date):
        project_timesheet = f"\nProject: {self.name}\n"

        for entry in self.time_entries:
            if entry.employee == employee and start_date <= entry.date <= end_date:
                project_timesheet += f"{entry.date}: {entry.hours} hours\n"

        return project_timesheet

    def get_total_hours(self, employee, start_date, end_date):
        total_hours = 0
        for entry in self.time_entries:
            if entry.employee == employee and start_date <= entry.date <= end_date:
                total_hours += entry.hours
        return total_hours


class TimeEntry:
    def __init__(self, employee, hours, date):
        self.employee = employee
        self.hours = hours
        self.date = date


employee1 = Employee(employee_id=1, name="u1")
employee2 = Employee(employee_id=2, name="u2")

project1 = Project(project_id=101, name="Project 1")
project2 = Project(project_id=102, name="Project 2")

employee1.log_hours(project1, hours=8, date=datetime(2023, 1, 1))
employee1.log_hours(project2, hours=6, date=datetime(2023, 1, 2))
employee2.log_hours(project1, hours=7, date=datetime(2023, 1, 1))
employee2.log_hours(project2, hours=9, date=datetime(2023, 1, 2))

timesheet1 = employee1.generate_timesheet(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 1, 2))
timesheet2 = employee2.generate_timesheet(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 1, 2))

print(timesheet1)
print(timesheet2)
