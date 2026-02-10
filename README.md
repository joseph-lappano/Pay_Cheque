# Pay_Cheque

Check in software with support for barcode scanners, managed through a specified CSV file tailored to the user's needs.

# Features
- Real-time check-in and rescan handling for security
- Timestamped entries
- Event capacity indicators
- Configurable event options
- Cross-platform exectuables (Windows and macOS)
- Search through both student number (barcode) and name (manual)

# Technologies
- Python
- CSV file handling
- Pygame GUI

# Motivation
- Created to assist high school Student Council with large events (400+ attendees), creating streamlined attendance tracking with security implementation

# Requirements
- CSV file including specified information in the following format:
Student Number | OEN | Last_Name | First_Name | Grade Level | Option 1 | Option 2 | Option 3 | Option 4 | Checked-In | Time
- Options 1-4 customizable based on event, displays underneath ticket-holder (ie: Food options, merchandise sales)
- Barcode Scanner (Not mandatory, but needed for efficiency)
