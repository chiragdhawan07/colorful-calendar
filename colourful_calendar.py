import calendar
from rich.console import Console
from rich.table import Table

def show_colorful_calendar(year, month):
    console = Console()
    cal = calendar.Calendar()

    table = Table(title=f"[bold cyan]{calendar.month_name[month]} {year}[/bold cyan]", show_lines=True)

    # Add headers
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days):
        color = "red" if day in ["Sat", "Sun"] else "green"
        table.add_column(day, justify="center", style=color)

    # Get days
    month_days = cal.monthdayscalendar(year, month)
    for week in month_days:
        table.add_row(*[str(day) if day != 0 else "" for day in week])

    console.print(table)

if __name__ == "__main__":
    import datetime

    # Get current month and year
    now = datetime.datetime.now()
    default_year = now.year
    default_month = now.month

    print("📅 Colorful Calendar Viewer (Terminal Only)\n")
    try:
        year = int(input(f"Enter year [{default_year}]: ") or default_year)
        month = int(input(f"Enter month (1-12): "))
        if 1 <= month <= 12:
            show_colorful_calendar(year, month)
        else:
            print("Invalid month. Please enter between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
