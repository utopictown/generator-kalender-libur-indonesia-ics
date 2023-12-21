from icalendar import Calendar, Event
from datetime import datetime
import pytz

# Translated month names from Indonesian to English
month_translations = {
    'Januari': 'January',
    'Februari': 'February',
    'Maret': 'March',
    'April': 'April',
    'Mei': 'May',
    'Juni': 'June',
    'Juli': 'July',
    'Agustus': 'August',
    'September': 'September',
    'Oktober': 'October',
    'November': 'November',
    'Desember': 'December'
}

def translate_date(date_str):
    day, month, year = date_str.split()
    month_eng = month_translations[month]
    return f"{day} {month_eng} {year}"

# Data for holidays and joint leave in 2024
holidays = {
    "1 Januari 2024": "Tahun Baru 2024 Masehi",
    "8 Februari 2024": "Isra Mikraj Nabi Muhammad SAW",
    "10 Februari 2024": "Tahun Baru Imlek 2575 Kongzili",
    "11 Maret 2024": "Hari Suci Nyepi Tahun Baru Saka 1946",
    "29 Maret 2024": "Wafat Isa Almasih",
    "31 Maret 2024": "Hari Paskah",
    "10 April 2024": "Hari Raya Idul Fitri 1445H",
    "11 April 2024": "Hari Raya Idul Fitri 1445H",
    "1 Mei 2024": "Hari Buruh Internasional",
    "9 Mei 2024": "Kenaikan Isa Almasih",
    "23 Mei 2024": "Hari Raya Waisak 2568 BE",
    "1 Juni 2024": "Hari Lahir Pancasila",
    "17 Juni 2024": "Hari Raya Idul Adha 1445H",
    "7 Juli 2024": "Tahun Baru Islam 1446H",
    "17 Agustus 2024": "Hari Kemerdekaan RI",
    "16 September 2024": "Maulid Nabi Muhammad SAW",
    "25 Desember 2024": "Hari Raya Natal"
}

joint_leaves = {
    "9 Februari 2024": "Cuti Bersama Tahun Baru Imlek",
    "12 Maret 2024": "Cuti Bersama Hari Suci Nyepi Tahun Baru Saka 1946",
    "8 April 2024": "Cuti Bersama Idul Fitri 1445H",
    "9 April 2024": "Cuti Bersama Idul Fitri 1445H",
    "12 April 2024": "Cuti Bersama Idul Fitri 1445H",
    "15 April 2024": "Cuti Bersama Idul Fitri 1445H",
    "10 Mei 2024": "Cuti Bersama Kenaikan Isa Al Masih",
    "24 Mei 2024": "Cuti Bersama Hari Raya Waisak",
    "18 Juni 2024": "Cuti Bersama Idul Adha 1445H",
    "26 Desember 2024": "Cuti Bersama Hari Raya Natal"
}

# Combine all dates into one dictionary
all_dates = {**holidays, **joint_leaves}

# Create a calendar
cal = Calendar()
cal.add('prodid', '-//Indonesia Holiday Calendar 2024//mxm.dk//')
cal.add('version', '2.0')

# Timezone for Indonesia (Jakarta)
tz = pytz.timezone('Asia/Jakarta')

# Function to convert date string to datetime object
def convert_to_datetime(date_str):
    translated_date_str = translate_date(date_str)
    return tz.localize(datetime.strptime(translated_date_str, "%d %B %Y"))

# Add events to the calendar
for date_str, description in all_dates.items():
    event = Event()
    event.add('summary', description)
    event_date = convert_to_datetime(date_str)
    event.add('dtstart', event_date)
    event.add('dtend', event_date)  # Single day event
    cal.add_component(event)

# Write the calendar to an .ics file
file_path = 'Indonesia_Holidays_2024.ics'
with open(file_path, 'wb') as f:
    f.write(cal.to_ical())