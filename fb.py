import streamlit as st
import pandas as pd
import datetime
from datetime import datetime, timedelta
import csv
from io import StringIO
import base64
import os

# ڈیٹا فائل کا نام
DATA_FILE = "admission_data.csv"

def load_data():
    """ڈیٹا فائل سے لوڈ کریں"""
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        # ڈیٹا ٹائپس کو درست کریں
        if not df.empty:
            df['age'] = df['age'].astype(int)
            df['course_fee'] = df['course_fee'].astype(int)
            df['discount'] = df['discount'].astype(int)
            df['total_fee'] = df['total_fee'].astype(int)
        return df.to_dict('records')
    return []

def save_data(data):
    """ڈیٹا فائل میں سیو کریں"""
    if data:  # صرف تبھی سیو کریں جب ڈیٹا موجود ہو
        df = pd.DataFrame(data)
        df.to_csv(DATA_FILE, index=False)

# Configure the page
st.set_page_config(
    page_title="Art & Craft Institute Admission & Certificate",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4B0082;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .section-header {
        font-size: 1.5rem;
        color: #8A2BE2;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #8A2BE2;
        padding-bottom: 5px;
    }
    .fee-box {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #4B0082;
        margin: 1rem 0;
    }
    .receipt {
        background-color: #fffaf0;
        padding: 2rem;
        border-radius: 10px;
        border: 2px solid #8A2BE2;
        margin: 1rem 0;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .course-outline {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .schedule-box {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #228B22;
        margin: 1rem 0;
    }
    .certificate-border {
        border: 15px solid #FFD700;
        padding: 30px;
        background-color: #fcfcfc;
        text-align: center;
        margin: 20px 0;
        background: linear-gradient(135deg, #fff 0%, #f9f9f9 100%);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .certificate-title {
        font-family: 'Times New Roman', serif;
        font-size: 3.5rem;
        color: #4B0082;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .certificate-subtitle {
        font-size: 1.5rem;
        color: #8A2BE2;
        margin-bottom: 1rem;
        font-style: italic;
    }
    .certificate-name {
        font-family: 'Cursive', 'Brush Script MT', sans-serif;
        font-size: 3.5rem;
        color: #008080;
        margin: 2rem 0;
        border-bottom: 3px double #008080;
        display: inline-block;
        padding: 0 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .certificate-course {
        font-size: 2rem;
        color: #333;
        margin-top: 1rem;
        font-style: italic;
        font-weight: bold;
    }
    .stDownloadButton button {
        background-color: #8A2BE2;
        color: white;
        font-weight: bold;
    }
    .eligible-student {
        background-color: #e8f5e8;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        border-left: 4px solid #28a745;
    }
    .not-eligible-student {
        background-color: #fff3cd;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
        border-left: 4px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

class AdmissionSystem:
    def __init__(self):
        self.courses = {
            'Crochet - Basic': {'fee': 5000, 'duration': '3 months', 'level': 'Basic', 'days': 'Monday, Wednesday, Friday', 'time': '2:00 PM - 4:00 PM', 'days_per_week': '3 days'},
            'Crochet - Advanced': {'fee': 7000, 'duration': '3 months', 'level': 'Advanced', 'days': 'Tuesday, Thursday', 'time': '5:00 PM - 7:00 PM', 'days_per_week': '2 days'},
            'Baking - Basic': {'fee': 6000, 'duration': '3 months', 'level': 'Basic', 'days': 'Monday, Wednesday', 'time': '5:00 PM - 7:00 PM', 'days_per_week': '2 days'},
            'Baking - Advanced': {'fee': 8000, 'duration': '3 months', 'level': 'Advanced', 'days': 'Tuesday, Thursday, Friday', 'time': '2:00 PM - 4:00 PM', 'days_per_week': '3 days'},
            'Cooking - Basic': {'fee': 5500, 'duration': '3 months', 'level': 'Basic', 'days': 'Tuesday, Thursday', 'time': '2:00 PM - 4:00 PM', 'days_per_week': '2 days'},
            'Cooking - Advanced': {'fee': 7500, 'duration': '3 months', 'level': 'Advanced', 'days': 'Monday, Wednesday, Friday', 'time': '5:00 PM - 7:00 PM', 'days_per_week': '3 days'},
            'Stitching - Basic': {'fee': 5000, 'duration': '3 months', 'level': 'Basic', 'days': 'Monday, Wednesday, Friday', 'time': '5:00 PM - 7:00 PM', 'days_per_week': '3 days'},
            'Stitching - Advanced': {'fee': 7000, 'duration': '3 months', 'level': 'Advanced', 'days': 'Tuesday, Thursday', 'time': '2:00 PM - 4:00 PM', 'days_per_week': '2 days'},
            'Hand Embroidery - Basic': {'fee': 4500, 'duration': '3 months', 'level': 'Basic', 'days': 'Tuesday, Thursday', 'time': '5:00 PM - 7:00 PM', 'days_per_week': '2 days'},
            'Hand Embroidery - Advanced': {'fee': 6500, 'duration': '3 months', 'level': 'Advanced', 'days': 'Monday, Wednesday, Friday', 'time': '2:00 PM - 4:00 PM', 'days_per_week': '3 days'},
            'Hand Knitting - Basic': {'fee': 4000, 'duration': '3 months', 'level': 'Basic', 'days': 'Monday, Wednesday', 'time': '2:00 PM - 4:00 PM', 'days_per_week': '2 days'},
            'Hand Knitting - Advanced': {'fee': 6000, 'duration': '3 months', 'level': 'Advanced', 'days': 'Tuesday, Thursday, Friday', 'time': '5:00 PM - 7:00 PM', 'days_per_week': '3 days'}
        }
        
        self.course_outlines = self._initialize_course_outlines()
        
    def _initialize_course_outlines(self):
        outlines = {
            'Crochet - Basic': [
                "Introduction to Crochet Tools & Materials", "Basic Crochet Stitches: Chain, Slip, Single", "Double Crochet & Treble Crochet",
                "Working in Rounds - Circles & Squares", "Reading Basic Crochet Patterns", "Simple Projects: Coasters, Scarves",
                "Color Changing Techniques", "Finishing & Blocking Techniques", "Troubleshooting Common Mistakes",
                "Project: Basic Granny Square", "Project: Simple Beanie", "**Final Assessment & Certificate**"
            ],
            'Crochet - Advanced': [
                "Advanced Stitch Patterns", "Complex Color Work", "Lace Crochet Techniques",
                "Amigurumi & 3D Crochet", "Garment Construction", "Professional Finishing Techniques",
                "Custom Pattern Design", "Market Ready Product Development", "Advanced Project: Crochet Garment",
                "Advanced Project: Home Decor Item", "Portfolio Development", "**Final Assessment & Certificate**"
            ],
            'Baking - Basic': [
                "Introduction to Baking Tools & Equipment", "Basic Baking Principles & Measurements", "Cookie & Biscuit Making",
                "Basic Cake Baking & Decorating", "Bread Making Fundamentals", "Pastry Basics: Puffs & Tarts",
                "Frosting & Icing Techniques", "Oven Temperature Control", "Food Safety & Hygiene",
                "Project: Assorted Cookies", "Project: Basic Birthday Cake", "**Final Assessment & Certificate**"
            ],
            'Baking - Advanced': [
                "Advanced Cake Decorating", "French Pastries & Desserts", "Artisan Bread Making",
                "Chocolate Work & Tempering", "Sugar Art & Pulled Sugar", "Wedding Cake Design",
                "Advanced Baking Science", "Recipe Development", "Commercial Baking Techniques",
                "Project: Tiered Wedding Cake", "Project: French Pastry Platter", "**Final Assessment & Certificate**"
            ],
            'Cooking - Basic': [
                "Kitchen Safety & Hygiene", "Basic Cutting Techniques", "Fundamental Cooking Methods",
                "Sauce Making Basics", "Rice & Grain Preparation", "Vegetable Cooking Techniques",
                "Basic Meat & Poultry Preparation", "Menu Planning Basics", "Food Presentation",
                "Project: Complete 3-Course Meal", "Project: Traditional Dishes", "**Final Assessment & Certificate**"
            ],
            'Cooking - Advanced': [
                "Advanced Cooking Techniques", "International Cuisine", "Molecular Gastronomy Basics",
                "Advanced Sauce Making", "Meat & Seafood Specialist", "Restaurant Style Cooking",
                "Menu Engineering", "Food Cost Control", "Advanced Presentation Techniques",
                "Project: International Dinner", "Project: Fine Dining Experience", "**Final Assessment & Certificate**"
            ],
            'Stitching - Basic': [
                "Introduction to Sewing Machine", "Basic Stitches & Seams", "Fabric Types & Selection",
                "Pattern Reading Basics", "Simple Garment Construction", "Zipper & Button Installation",
                "Hemming Techniques", "Basic Alterations", "Care & Maintenance of Equipment",
                "Project: Simple Top/Dress", "Project: Basic Home Decor Item", "**Final Assessment & Certificate**"
            ],
            'Stitching - Advanced': [
                "Advanced Garment Construction", "Complex Pattern Making", "Tailoring Techniques",
                "Evening Wear Construction", "Advanced Finishing Methods", "Professional Alterations",
                "Fabric Manipulation", "Portfolio Development", "Business of Stitching",
                "Project: Formal Suit/Dress", "Project: Designer Outfit", "**Final Assessment & Certificate**"
            ],
            'Hand Embroidery - Basic': [
                "Introduction to Embroidery Tools", "Basic Embroidery Stitches", "Fabric Selection & Preparation",
                "Color Theory in Embroidery", "Pattern Transfer Methods", "Simple Floral Motifs",
                "Border Designs & Patterns", "Finishing & Framing", "Care of Embroidered Items",
                "Project: Embroidered Handkerchief", "Project: Decorative Wall Piece", "**Final Assessment & Certificate**"
            ],
            'Hand Embroidery - Advanced': [
                "Advanced Embroidery Techniques", "Thread Painting & Shading", "Gold Work Embroidery",
                "Beadwork & Sequins", "Traditional Regional Styles", "Portrait Embroidery",
                "Mixed Media Embroidery", "Exhibition Quality Work", "Teaching Methodology",
                "Project: Heirloom Piece", "Project: Advanced Art Piece", "**Final Assessment & Certificate**"
            ],
            'Hand Knitting - Basic': [
                "Introduction to Knitting Needles & Yarn", "Basic Knitting Stitches", "Casting On & Binding Off",
                "Reading Simple Patterns", "Increasing & Decreasing", "Color Work Basics",
                "Simple Project Construction", "Blocking & Finishing", "Troubleshooting Common Errors",
                "Project: Scarf or Shawl", "Project: Basic Hat", "**Final Assessment & Certificate**"
            ],
            'Hand Knitting - Advanced': [
                "Advanced Stitch Patterns", "Cable Knitting Techniques", "Lace Knitting",
                "Garment Construction", "Professional Finishing", "Custom Pattern Design",
                "Yarn Substitution & Calculation", "Advanced Color Work", "Knitting for Business",
                "Project: Complex Garment", "Project: Designer Accessory", "**Final Assessment & Certificate**"
            ]
        }
        return outlines
        
    def calculate_total_fee(self, course, discount=0):
        base_fee = self.courses[course]['fee']
        return base_fee - discount
    
    def get_course_outline(self, course_name):
        return self.course_outlines.get(course_name, ["Course outline not available."])

def get_base64_image(image_path):
    """تصویر کو base64 میں تبدیل کریں"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.warning(f"لوگو فائل نہیں مل سکی: {image_path}")
        return None
    except Exception as e:
        st.warning(f"لوگو لوڈ کرنے میں مسئلہ: {e}")
        return None

def get_certificate_html(student_data):
    """لوگو کے ساتھ سرٹیفکیٹ کی HTML جنریٹ کریں"""
    
    # لوگو کی تصویر (اگر موجود ہو)
    logo_html = ""
    logo_base64 = get_base64_image("123.jpg")
    if logo_base64:
        logo_html = f'<img src="data:image/jpeg;base64,{logo_base64}" style="height: 100px; margin-bottom: 20px;" alt="Institute Logo">'
    else:
        # اگر لوگو نہیں ہے تو انسٹی ٹیوٹ کا نام دکھائیں
        logo_html = '<h2 style="color: #4B0082; margin-bottom: 20px;">Art & Craft Institute</h2>'
    
    # درست تاریخوں کا حساب
    try:
        # Completion date = admission date + 90 days
        admission_date = datetime.strptime(student_data['admission_date'], '%Y-%m-%d')
        completion_date = (admission_date + timedelta(days=90)).strftime('%B %d, %Y')
        
        # Issue date = آج کی تاریخ
        issue_date = datetime.now().strftime('%B %d, %Y')
        
        # Certificate ID = admission_id + "-CERT"
        certificate_id = f"{student_data['admission_id']}-CERT"
        
    except Exception as e:
        # اگر تاریخ میں کوئی مسئلہ ہو تو ڈیفالٹ ویلیوز استعمال کریں
        st.error(f"تاریخ کا حساب لگانے میں مسئلہ: {e}")
        completion_date = "Not Available"
        issue_date = datetime.now().strftime('%B %d, %Y')
        certificate_id = f"{student_data['admission_id']}-CERT"
    
    html_content = f"""
    <div class="certificate-border">
        {logo_html}
        <h1 class="certificate-title">CERTIFICATE OF COMPLETION</h1>
        <p class="certificate-subtitle">This is to Certify That</p>
        <div class="certificate-name">{student_data['student_name'].upper()}</div>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            Has successfully completed the <strong>{student_data['course']}</strong> course
        </p>
        <p style="font-size: 1.1rem; margin-bottom: 2rem;">
            with dedication and excellence from <strong>Art & Craft Institute</strong>
        </p>
        
        <div style="display: flex; justify-content: space-around; margin-top: 3rem;">
            <div style="text-align: center;">
                <p>___________________________</p>
                <p style="font-weight: bold; margin-top: 5px;">Institute Director</p>
                <p style="font-size: 0.9rem;">Art & Craft Institute</p>
            </div>
            <div style="text-align: center;">
                <p>Completion Date: {completion_date}</p>
                <p style="font-weight: bold; margin-top: 5px;">Course Duration</p>
                <p style="font-size: 0.9rem;">{student_data['duration']}</p>
            </div>
            <div style="text-align: center;">
                <p>___________________________</p>
                <p style="font-weight: bold; margin-top: 5px;">Course Instructor</p>
                <p style="font-size: 0.9rem;">{student_data['course']}</p>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <p><strong>Issued On:</strong> {issue_date}</p>
        </div>
        
        <p style="font-size: 0.9rem; margin-top: 2rem; color: #777;">
            Certificate ID: {certificate_id} | Course: {student_data['course']} | Level: {student_data['course_level']}
        </p>
    </div>
    """
    return html_content

def get_eligible_students(admission_data):
    """صرف ان طلبہ کو واپس کریں جن کی completion date ہو چکی ہے"""
    eligible_students = []
    today = datetime.now().date()
    
    for student in admission_data:
        try:
            admission_date = datetime.strptime(student['admission_date'], '%Y-%m-%d').date()
            completion_date = admission_date + timedelta(days=90)
            
            # اگر آج کی تاریخ completion date کے برابر یا اس سے زیادہ ہے
            if today >= completion_date:
                student['completion_date'] = completion_date.strftime('%Y-%m-%d')
                eligible_students.append(student)
        except Exception as e:
            continue
    
    return eligible_students

def generate_certificate_page():
    st.markdown('<div class="section-header">📜 Course Completion Certificate</div>', unsafe_allow_html=True)
    
    if not st.session_state.admission_data:
        st.info("No admission records found. Please add admissions first.")
        return
    
    # صرف eligible طلبہ کو فلٹر کریں
    eligible_students = get_eligible_students(st.session_state.admission_data)
    all_students = st.session_state.admission_data
    
    st.info(f"""
    **Certificate Eligibility Criteria:**
    - ✅ **Eligible for Certificate**: {len(eligible_students)} students (completed 90 days course)
    - ⏳ **In Progress**: {len(all_students) - len(eligible_students)} students (still in course)
    - 📊 **Total Students**: {len(all_students)} students
    """)
    
    # اگر کوئی eligible طالب علم نہیں ہے
    if not eligible_students:
        st.warning("""
        **No students are eligible for certificate yet.**
        
        **Requirements for certificate:**
        - Student must have completed 90 days (3 months) of course
        - Certificate will be available automatically after course completion
        """)
        
        # تمام طلبہ کی لسٹ دکھائیں (صرف معلومات کے لیے)
        if st.checkbox("Show All Students (In Progress)"):
            for student in all_students:
                admission_date = datetime.strptime(student['admission_date'], '%Y-%m-%d').date()
                completion_date = admission_date + timedelta(days=90)
                days_remaining = (completion_date - datetime.now().date()).days
                
                st.markdown(f"""
                <div class="not-eligible-student">
                    <strong>{student['student_name']}</strong> - {student['course']}<br>
                    <small>Admission: {student['admission_date']} | Completion: {completion_date} | Days Remaining: {max(0, days_remaining)}</small>
                </div>
                """, unsafe_allow_html=True)
        return

    # Eligible طلبہ کی لسٹ
    st.success(f"🎉 {len(eligible_students)} students are eligible for certificate!")
    
    select_options = [f"{student['student_name']} - {student['course']} (ID: {student['admission_id']})" for student in eligible_students]
    
    selected_option = st.selectbox("Select Student for Certificate Generation", ["Select a Student"] + select_options)
    
    if selected_option != "Select a Student":
        selected_id = selected_option.split('(ID: ')[1].replace(')', '')
        student_data = next((student for student in eligible_students 
                             if student['admission_id'] == selected_id), None)
        
        if student_data:
            # ڈیٹا کی تصدیق
            admission_date = datetime.strptime(student_data['admission_date'], '%Y-%m-%d').date()
            actual_completion_date = admission_date + timedelta(days=90)
            
            st.success(f"✅ Generating certificate for: {student_data['student_name']}")
            
            # طالب علم کی تفصیلات
            st.info(f"""
            **Student Details:**
            - **Name:** {student_data['student_name']}
            - **Course:** {student_data['course']} ({student_data['course_level']})
            - **Admission Date:** {student_data['admission_date']}
            - **Course Duration:** {student_data['duration']}
            - **Actual Completion Date:** {actual_completion_date}
            - **Certificate ID:** {student_data['admission_id']}-CERT
            """)
            
            st.subheader(f"Certificate Preview for {student_data['student_name']}")
            
            certificate_html = get_certificate_html(student_data)
            st.markdown(certificate_html, unsafe_allow_html=True)
            
            # ڈاؤنلوڈ کے لیے مکمل HTML فائل
            certificate_download_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Certificate - {student_data['student_name']}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    .certificate-border {{
                        border: 15px solid #FFD700;
                        padding: 30px;
                        background-color: #fcfcfc;
                        text-align: center;
                        margin: 20px 0;
                        background: linear-gradient(135deg, #fff 0%, #f9f9f9 100%);
                        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                    }}
                    .certificate-title {{
                        font-family: 'Times New Roman', serif;
                        font-size: 3.5rem;
                        color: #4B0082;
                        font-weight: bold;
                        margin-bottom: 0.5rem;
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                    }}
                    .certificate-subtitle {{
                        font-size: 1.5rem;
                        color: #8A2BE2;
                        margin-bottom: 1rem;
                        font-style: italic;
                    }}
                    .certificate-name {{
                        font-family: 'Cursive', 'Brush Script MT', sans-serif;
                        font-size: 3.5rem;
                        color: #008080;
                        margin: 2rem 0;
                        border-bottom: 3px double #008080;
                        display: inline-block;
                        padding: 0 20px;
                        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
                    }}
                </style>
            </head>
            <body>
                {certificate_html}
            </body>
            </html>
            """
            
            st.download_button(
                label=f"🌟 Download Certificate for {student_data['course']} (HTML)",
                data=certificate_download_content,
                file_name=f"Certificate_{student_data['student_name'].replace(' ', '_')}_{student_data['course'].replace(' ', '_')}.html",
                mime="text/html",
                key="download_certificate"
            )

def main():
    st.markdown('<div class="main-header">🎨 Art & Craft Institute - Admission & Records System</div>', unsafe_allow_html=True)
    
    # ڈیٹا لوڈ کریں
    if 'admission_data' not in st.session_state:
        st.session_state.admission_data = load_data()
    
    if 'current_student' not in st.session_state:
        st.session_state.current_student = {}
    if 'show_receipt' not in st.session_state:
        st.session_state.show_receipt = False
    
    system = AdmissionSystem()
    
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["New Admission", "View Records", "Generate Receipt", "Fee Structure", "Course Outlines", "Class Schedule", "Generate Certificate"])
    
    if page == "New Admission":
        new_admission(system)
    elif page == "View Records":
        view_records()
    elif page == "Generate Receipt":
        generate_receipt()
    elif page == "Fee Structure":
        fee_structure(system)
    elif page == "Course Outlines":
        course_outlines(system)
    elif page == "Class Schedule":
        class_schedule(system)
    elif page == "Generate Certificate":
        generate_certificate_page()

def new_admission(system):
    st.markdown('<div class="section-header">📝 New Student Admission</div>', unsafe_allow_html=True)
    
    if st.session_state.show_receipt and st.session_state.current_student:
        display_receipt(st.session_state.current_student)
        if st.button("🔄 Create New Admission"):
            st.session_state.show_receipt = False
            st.session_state.current_student = {}
            st.rerun()
        return
    
    with st.form("admission_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Student Information")
            student_name = st.text_input("Full Name*")
            father_name = st.text_input("Father/Husband Name")
            age = st.number_input("Age", min_value=5, max_value=80, value=18)
            contact = st.text_input("Contact Number*")
            email = st.text_input("Email Address")
            address = st.text_area("Residential Address")
            
        with col2:
            st.subheader("Course Details")
            course = st.selectbox("Select Course*", list(system.courses.keys()))
            
            course_info = system.courses[course]
            st.markdown(f'<div class="schedule-box">', unsafe_allow_html=True)
            st.markdown(f"**Fixed Schedule for {course}:**")
            st.markdown(f"**Days:** {course_info['days']}")
            st.markdown(f"**Time:** {course_info['time']}")
            st.markdown(f"**Duration:** {course_info['duration']} ({course_info['days_per_week']})")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.subheader("Fee Details")
            admission_date = st.date_input("Admission Date*", datetime.now().date())
            discount = st.number_input("Discount (if any)", min_value=0, value=0)
            
            total_fee = system.calculate_total_fee(course, discount)
            
            st.markdown(f'<div class="fee-box">'
                        f'<h4>Fee Breakdown</h4>'
                        f'<p>Course Fee: Rs. {system.courses[course]["fee"]:,}</p>'
                        f'<p>Discount: Rs. {discount}</p>'
                        f'<p><strong>Total Fee: Rs. {total_fee:,}</strong></p>'
                        f'</div>', unsafe_allow_html=True)
        
        submitted = st.form_submit_button("Submit Admission")
        
        if submitted:
            if not student_name or not contact or not course:
                st.error("Please fill all required fields (*) correctly!")
            else:
                admission_id = f"ART{datetime.now().strftime('%Y%m%d%H%M%S')}"
                
                student_data = {
                    'admission_id': admission_id,
                    'admission_date': admission_date.strftime('%Y-%m-%d'),
                    'student_name': student_name,
                    'father_name': father_name,
                    'age': age,
                    'contact': contact,
                    'email': email,
                    'address': address,
                    'course': course,
                    'course_level': system.courses[course]['level'],
                    'days': system.courses[course]['days'],
                    'time_slot': system.courses[course]['time'],
                    'days_per_week': system.courses[course]['days_per_week'],
                    'course_fee': system.courses[course]['fee'],
                    'discount': discount,
                    'total_fee': total_fee,
                    'duration': system.courses[course]['duration'],
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
                st.session_state.current_student = student_data
                st.session_state.admission_data.append(student_data)
                save_data(st.session_state.admission_data)  # ڈیٹا سیو کریں
                st.session_state.show_receipt = True
                
                st.success(f"Admission Successful! Admission ID: {admission_id}")
                st.balloons()
                st.rerun()

def display_receipt(student_data):
    st.markdown('<div class="section-header">🎫 Admission Receipt</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="receipt">', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([2,1,1])
        with col1:
            st.markdown("**Art & Craft Institute**")
            st.markdown("*Where Creativity Meets Excellence*")
        with col3:
            st.markdown(f"**Admission ID:** {student_data['admission_id']}")
            st.markdown(f"**Date:** {student_data['admission_date']}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Student Information:**")
            st.markdown(f"Name: {student_data['student_name']}")
            st.markdown(f"Father/Husband Name: {student_data['father_name']}")
            st.markdown(f"Age: {student_data['age']}")
            st.markdown(f"Contact: {student_data['contact']}")
        
        with col2:
            st.markdown("**Course Details:**")
            st.markdown(f"Course: {student_data['course']}")
            st.markdown(f"Level: {student_data['course_level']}")
            st.markdown(f"Duration: {student_data['duration']}")
            st.markdown(f"Days: {student_data['days']}")
            st.markdown(f"Time: {student_data['time_slot']}")
        
        st.markdown("---")
        
        st.markdown("**Fee Breakdown:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"Course Fee: Rs. {student_data['course_fee']:,}")
        with col2:
            if student_data['discount'] > 0:
                st.markdown(f"Discount: Rs. {student_data['discount']:,}")
        with col3:
            st.markdown(f"**Total Fee: Rs. {student_data['total_fee']:,}**")
        
        st.markdown("---")
        st.markdown("*Thank you for choosing Art & Craft Institute*")
        st.markdown("*Classes: Monday to Friday | Timing: 2:00-4:00 PM & 5:00-7:00 PM*")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        csv_data = generate_csv_data(student_data)
        st.download_button(
            label="📥 Download Receipt as CSV",
            data=csv_data,
            file_name=f"admission_receipt_{student_data['admission_id']}.csv",
            mime="text/csv"
        )

def generate_csv_data(student_data):
    output = StringIO()
    writer = csv.writer(output)
    
    writer.writerow(["Art & Craft Institute - Admission Receipt"])
    writer.writerow([])
    writer.writerow(["Admission ID:", student_data['admission_id']])
    writer.writerow(["Admission Date:", student_data['admission_date']])
    writer.writerow([])
    
    writer.writerow(["STUDENT INFORMATION"])
    writer.writerow(["Full Name:", student_data['student_name']])
    writer.writerow(["Father/Husband Name:", student_data['father_name']])
    writer.writerow(["Age:", student_data['age']])
    writer.writerow(["Contact:", student_data['contact']])
    writer.writerow(["Email:", student_data['email']])
    writer.writerow(["Address:", student_data['address']])
    writer.writerow([])
    
    writer.writerow(["COURSE DETAILS"])
    writer.writerow(["Course:", student_data['course']])
    writer.writerow(["Level:", student_data['course_level']])
    writer.writerow(["Duration:", student_data['duration']])
    writer.writerow(["Days:", student_data['days']])
    writer.writerow(["Time Slot:", student_data['time_slot']])
    writer.writerow([])
    
    writer.writerow(["FEE BREAKDOWN"])
    writer.writerow(["Course Fee:", f"Rs. {student_data['course_fee']:,}"])
    if student_data['discount'] > 0:
        writer.writerow(["Discount:", f"Rs. {student_data['discount']:,}"])
    writer.writerow(["TOTAL FEE:", f"Rs. {student_data['total_fee']:,}"])
    writer.writerow([])
    writer.writerow(["Thank you for choosing Art & Craft Institute!"])
    
    return output.getvalue()

def view_records():
    st.markdown('<div class="section-header">📊 Admission Records</div>', unsafe_allow_html=True)
    
    if not st.session_state.admission_data:
        st.info("No admission records found.")
        return
    
    df = pd.DataFrame(st.session_state.admission_data)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Admissions", len(df))
    with col2:
        st.metric("Total Revenue", f"Rs. {df['total_fee'].sum():,}")
    with col3:
        popular_course = df['course'].mode()[0] if not df.empty else "N/A"
        st.metric("Most Popular Course", popular_course)
    with col4:
        avg_fee = df['total_fee'].mean() if not df.empty else 0
        st.metric("Average Fee", f"Rs. {avg_fee:,.0f}")
    
    st.subheader("Filter Records")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        course_filter = st.selectbox("Filter by Course", ["All"] + list(df['course'].unique()))
    with col2:
        level_filter = st.selectbox("Filter by Level", ["All"] + list(df['course_level'].unique()))
    with col3:
        search_name = st.text_input("Search by Name")
    
    filtered_df = df.copy()
    if course_filter != "All":
        filtered_df = filtered_df[filtered_df['course'] == course_filter]
    if level_filter != "All":
        filtered_df = filtered_df[filtered_df['course_level'] == level_filter]
    if search_name:
        filtered_df = filtered_df[filtered_df['student_name'].str.contains(search_name, case=False)]
    
    st.dataframe(filtered_df[['admission_id', 'admission_date', 'student_name', 'course', 'course_level', 'days', 'time_slot', 'total_fee']], 
                 use_container_width=True)
    
    csv_data_all = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download All Records as CSV",
        data=csv_data_all,
        file_name=f"admission_records_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

def generate_receipt():
    st.markdown('<div class="section-header">🧾 Generate Receipt</div>', unsafe_allow_html=True)
    
    if not st.session_state.admission_data:
        st.info("No admission records found. Please add admissions first.")
        return
    
    admission_ids = [student['admission_id'] for student in st.session_state.admission_data]
    selected_id = st.selectbox("Select Admission ID", admission_ids)
    
    if selected_id:
        student_data = next((student for student in st.session_state.admission_data 
                             if student['admission_id'] == selected_id), None)
        
        if student_data:
            display_receipt(student_data)

def fee_structure(system):
    st.markdown('<div class="section-header">💰 Fee Structure</div>', unsafe_allow_html=True)
    
    st.info("Below is the detailed fee structure for all courses offered at our institute.")
    
    fee_data = []
    for course, details in system.courses.items():
        fee_data.append({
            'Course': course,
            'Level': details['level'],
            'Duration': details['duration'],
            'Days': details['days'],
            'Time': details['time'],
            'Fee': f'Rs. {details["fee"]:,}'
        })
    
    df = pd.DataFrame(fee_data)
    st.table(df)
    
    st.markdown("""
    ### 📋 Additional Information:
    - **All courses are 3 months duration** (Basic + Advanced = 6 months complete course)
    - **Fixed schedules** for each course for better management
    - Classes are conducted from **Monday to Friday** only
    - Two time slots available: **2:00-4:00 PM** and **5:00-7:00 PM**
    - All course materials are included in the fee
    - **Certificate provided upon course completion**
    - Flexible payment options available
    """)

def course_outlines(system):
    st.markdown('<div class="section-header">📚 Course Outlines</div>', unsafe_allow_html=True)
    
    st.info("Select a course to view its detailed curriculum and learning objectives.")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        selected_course = st.selectbox("Select Course", list(system.courses.keys()))
        
        if selected_course:
            course_info = system.courses[selected_course]
            st.markdown(f"""
            **Course:** {selected_course}
            **Level:** {course_info['level']}
            **Duration:** {course_info['duration']}
            **Days:** {course_info['days']}
            **Time:** {course_info['time']}
            **Fee:** Rs. {course_info['fee']:,}
            """)
    
    with col2:
        if selected_course:
            outline = system.get_course_outline(selected_course)
            
            st.markdown(f'<div class="course-outline">', unsafe_allow_html=True)
            st.markdown(f"### {selected_course} - Course Outline")
            st.markdown("---")
            
            st.markdown("##### Topics Covered:")
            for topic in outline:
                st.markdown(f"- {topic}")
                
            st.markdown('</div>', unsafe_allow_html=True)
            
            outline_text = f"{selected_course} - Course Outline\n"
            outline_text += "=" * 50 + "\n\n"
            outline_text += f"Duration: {system.courses[selected_course]['duration']}\n"
            outline_text += f"Days: {system.courses[selected_course]['days']}\n"
            outline_text += f"Time: {system.courses[selected_course]['time']}\n\n"
            for i, topic in enumerate(outline, 1):
                outline_text += f"{i}. {topic}\n"
            
            st.download_button(
                label="📥 Download Course Outline (TXT)",
                data=outline_text,
                file_name=f"{selected_course.replace(' ', '_')}_Outline.txt",
                mime="text/plain"
            )

def class_schedule(system):
    st.markdown('<div class="section-header">📅 Complete Class Schedule</div>', unsafe_allow_html=True)
    
    st.info("Complete timetable for all courses offered at the institute.")
    
    schedule_data = []
    for course, details in system.courses.items():
        schedule_data.append({
            'Course': course,
            'Level': details['level'],
            'Days': details['days'],
            'Time': details['time'],
            'Duration': details['duration'],
            'Fee': f'Rs. {details["fee"]:,}'
        })
    
    df = pd.DataFrame(schedule_data)
    
    st.subheader("Morning Batch (2:00 PM - 4:00 PM) ☀️")
    morning_courses = df[df['Time'] == '2:00 PM - 4:00 PM'].reset_index(drop=True)
    st.table(morning_courses)
    
    st.subheader("Evening Batch (5:00 PM - 7:00 PM) 🌙")
    evening_courses = df[df['Time'] == '5:00 PM - 7:00 PM'].reset_index(drop=True)
    st.table(evening_courses)
    
    st.subheader("📋 Weekly Timetable Overview")
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = ['2:00 PM - 4:00 PM', '5:00 PM - 7:00 PM']
    
    timetable_data = []
    for day in days:
        for time_slot in time_slots:
            courses_on_day_time = []
            for course, details in system.courses.items():
                if day in details['days'] and details['time'] == time_slot:
                    courses_on_day_time.append(course)
            
            timetable_data.append({
                'Day': day,
                'Time Slot': time_slot,
                'Courses': ', '.join(courses_on_day_time) if courses_on_day_time else 'No classes'
            })
    
    timetable_df = pd.DataFrame(timetable_data)
    pivot_df = timetable_df.pivot(index='Time Slot', columns='Day', values='Courses').reindex(columns=days)
    st.dataframe(pivot_df, use_container_width=True)

if __name__ == "__main__":
    main()