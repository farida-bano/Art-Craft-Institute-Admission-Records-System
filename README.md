hi everyone

🎨 Art & Craft Institute - Admission & Certificate System A comprehensive Streamlit web application for managing student admissions, course registrations, fee management, and certificate generation for an Art & Craft Institute.

🌟 Features 📝 Admission Management New Student Admission: Complete student registration with personal and course details

Automatic ID Generation: Unique admission IDs (ARTYYYYMMDDHHMMSS)

Fee Calculation: Automatic fee calculation with discount support

Digital Receipts: Generate and download admission receipts

📊 Records & Analytics View All Records: Complete database of student admissions

Advanced Filtering: Filter by course, level, or student name

Financial Analytics: Total revenue, average fees, popular courses

Data Export: Download records as CSV files

💰 Fee Structure Transparent Pricing: Clear fee breakdown for all courses

Course Details: Duration, schedule, and level information

Discount System: Flexible discount application

📚 Course Information Detailed Outlines: Comprehensive curriculum for each course

Downloadable Content: Export course outlines as text files

Structured Learning: Step-by-step topic progression

🕐 Class Scheduling Weekly Timetable: Complete class schedule overview

Batch Management: Morning (2:00-4:00 PM) and Evening (5:00-7:00 PM) batches

Day-wise Breakdown: Course distribution across weekdays

🎓 Certificate System Auto-Generated Certificates: Professional completion certificates

90-Day Completion Rule: Certificates available after course duration

Logo Integration: Institute branding on certificates

Download Options: HTML format certificates with custom styling

🚀 Installation & Setup Prerequisites Python 3.7 or higher

pip (Python package manager)

Step 1: Clone or Download bash
If using git

git clone cd art-craft-institute
Or download the Python file directly

Step 2: Install Dependencies bash pip install streamlit pandas datetime Step 3: Add Institute Logo Place your institute logo file named 123.jpg in the same directory as the application.

Step 4: Run the Application bash streamlit run app.py 📋 System Requirements Software Requirements Python: Version 3.7+

Streamlit: Latest version

Pandas: For data management

Modern Web Browser: Chrome, Firefox, Safari, or Edge

Hardware Requirements RAM: Minimum 2GB

Storage: 100MB free space

Internet: For initial package installation

🎯 How to Use

    New Admission Navigate to "New Admission" page

Fill student personal information

Select course from available options

View automatic fee calculation

Submit to generate admission ID and receipt

    View Records Go to "View Records" page

Use filters to find specific students

View financial analytics

Export data as needed

    Generate Certificates Access "Generate Certificate" page

System shows eligible students (completed 90 days)

Select student and preview certificate

Download professional certificate

    Course Management Check fee structure and schedules

View detailed course outlines

Download curriculum information

📁 File Structure text art-craft-institute/ │ ├── app.py # Main application file ├── 123.jpg # Institute logo (required) ├── admission_data.csv # Auto-generated data file └── README.md # This file 🎨 Course Catalog Available Courses Crochet (Basic & Advanced)

Baking (Basic & Advanced)

Cooking (Basic & Advanced)

Stitching (Basic & Advanced)

Hand Embroidery (Basic & Advanced)

Hand Knitting (Basic & Advanced)

Course Features 🕐 Duration: 3 months per level

📅 Schedule: Monday to Friday

⏰ Timings: 2:00-4:00 PM & 5:00-7:00 PM

💰 Fees: Rs. 4,000 - Rs. 8,000

🔧 Technical Details Data Management CSV-based Storage: Simple file-based data management

Automatic Backup: Data persists between sessions

Data Validation: Type checking and error handling

Certificate System HTML-based Certificates: Professional formatting

Auto-calculation: Completion dates based on admission

Branding: Institute logo integration

Security: Unique certificate IDs

User Interface Responsive Design: Works on different screen sizes

Urdu & English: Bilingual interface support

Custom Styling: Professional color scheme and layout

💡 Usage Tips For Administrators Regular Backups: Export data periodically

Logo Customization: Replace 123.jpg with your logo

Fee Updates: Modify course fees in the code as needed

Course Management: Add new courses in the courses dictionary

For Students Keep Admission ID: Required for future reference

Certificate Eligibility: Automatic after 90 days

Receipt Download: Save digital receipt for records

🛠️ Customization Modifying Course Details Edit the courses dictionary in the code to:

Add new courses

Update fees

Modify schedules

Change duration

Styling Changes Modify the CSS in the st.markdown section to:

Change colors

Update fonts

Modify layouts

Add new styles

Logo Requirements Format: JPG/JPEG

Name: 123.jpg

Location: Same directory as application

Aspect Ratio: Square recommended

🔒 Data Security Local Storage All data stored locally in CSV format

No external server dependencies

Complete data ownership

Privacy Features No personal data sharing

Local processing only

User-controlled data export

📞 Support Troubleshooting Application won't start: Check Python and dependency installation

Logo not showing: Verify 123.jpg exists in correct directory

Data not saving: Check file permissions in application directory

Common Issues Missing dependencies: Re-run pip install command

Certificate generation: Ensure 90 days have passed since admission

Data persistence: Check if admission_data.csv is writable

🎊 Benefits For Institute ✅ Digital admission management

✅ Automated certificate generation

✅ Financial tracking and reporting

✅ Professional branding

✅ Time-saving automation

For Students ✅ Digital receipts and certificates

✅ Transparent fee structure

✅ Easy course information access

✅ Professional documentation

📄 License This project is open-source and available for educational and institutional use.

Developed with ❤️ for Art & Craft Institutes

Streamline your admission process and certificate management with this comprehensive digital solution! 🎨📚🎓
