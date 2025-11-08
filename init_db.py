"""
Database initialization script for ACME University Enrollment System
This script creates sample users, courses, and enrollments for testing
"""

from app import app, db, User, Course, Enrollment

def init_database():
    """Initialize database with sample data"""

    with app.app_context():
        #drop all tables and recreate them (fresh start)
        print("Dropping existing tables...")
        db.drop_all()

        print("Creating tables...")
        db.create_all()

        #create users (students, teachers, admin)
        print("Creating users...")

        #students
        student1 = User(username='cnorris', full_name='Chuck Norris', role='student')
        student1.set_password('password123')

        student2 = User(username='msherman', full_name='Mindy Sherman', role='student')
        student2.set_password('password123')

        student3 = User(username='aranganath', full_name='Aditya Ranganath', role='student')
        student3.set_password('password123')

        student4 = User(username='nlittle', full_name='Nancy Little', role='student')
        student4.set_password('password123')

        student5 = User(username='ychen', full_name='Yi Wen Chen', role='student')
        student5.set_password('password123')

        student6 = User(username='jstuart', full_name='John Stuart', role='student')
        student6.set_password('password123')

        #teachers
        teacher1 = User(username='ahepworth', full_name='Dr Hepworth', role='teacher')
        teacher1.set_password('password123')

        teacher2 = User(username='swalker', full_name='Susan Walker', role='teacher')
        teacher2.set_password('password123')

        teacher3 = User(username='rjenkins', full_name='Ralph Jenkins', role='teacher')
        teacher3.set_password('password123')

        #admin
        admin = User(username='admin', full_name='System Administrator', role='admin')
        admin.set_password('admin123')

        #add all users to session
        db.session.add_all([
            student1, student2, student3, student4, student5, student6,
            teacher1, teacher2, teacher3, admin
        ])
        db.session.commit()

        #create courses
        print("Creating courses...")

        course1 = Course(
            course_name='Physics 121',
            teacher_id=teacher2.id,
            time='TR 11:00-11:50 AM',
            capacity=10
        )

        course2 = Course(
            course_name='CS 106',
            teacher_id=teacher1.id,
            time='MWF 2:00-2:50 PM',
            capacity=10
        )

        course3 = Course(
            course_name='Math 101',
            teacher_id=teacher3.id,
            time='MWF 10:00-10:50 AM',
            capacity=8
        )

        course4 = Course(
            course_name='CS 162',
            teacher_id=teacher1.id,
            time='TR 3:00-3:50 PM',
            capacity=4
        )

        db.session.add_all([course1, course2, course3, course4])
        db.session.commit()

        #create enrollments
        print("Creating enrollments...")

        #chuck Norris enrollments
        enrollment1 = Enrollment(student_id=student1.id, course_id=course1.id, grade=0.0)
        enrollment2 = Enrollment(student_id=student1.id, course_id=course2.id, grade=0.0)

        #mindy Sherman enrollments (not enrolled in Physics 121 and CS 106, enrolled in others)
        enrollment3 = Enrollment(student_id=student2.id, course_id=course3.id, grade=0.0)
        enrollment4 = Enrollment(student_id=student2.id, course_id=course4.id, grade=0.0)

        #additional students for Physics 121 (to reach 5/10)
        enrollment5 = Enrollment(student_id=student3.id, course_id=course1.id, grade=0.0)
        enrollment6 = Enrollment(student_id=student4.id, course_id=course1.id, grade=0.0)
        enrollment7 = Enrollment(student_id=student5.id, course_id=course1.id, grade=0.0)

        #additional students for CS 106 (to reach 4/10)
        enrollment8 = Enrollment(student_id=student3.id, course_id=course2.id, grade=0.0)
        enrollment9 = Enrollment(student_id=student4.id, course_id=course2.id, grade=0.0)

        #students for CS 162 (full at 4/4) - with grades for teacher view
        enrollment10 = Enrollment(student_id=student3.id, course_id=course4.id, grade=92.0)
        enrollment11 = Enrollment(student_id=student4.id, course_id=course4.id, grade=78.0)
        enrollment12 = Enrollment(student_id=student5.id, course_id=course4.id, grade=95.0)
        enrollment13 = Enrollment(student_id=student6.id, course_id=course4.id, grade=76.0)

        #math 101 students (to reach 4/8)
        enrollment14 = Enrollment(student_id=student3.id, course_id=course3.id, grade=0.0)
        enrollment15 = Enrollment(student_id=student4.id, course_id=course3.id, grade=0.0)
        enrollment16 = Enrollment(student_id=student5.id, course_id=course3.id, grade=0.0)

        db.session.add_all([
            enrollment1, enrollment2, enrollment3, enrollment4, enrollment5,
            enrollment6, enrollment7, enrollment8, enrollment9, enrollment10,
            enrollment11, enrollment12, enrollment13, enrollment14, enrollment15,
            enrollment16
        ])
        db.session.commit()

        print("\n" + "="*60)
        print("Database initialized successfully!")
        print("="*60)
        print("\nSample login credentials:\n")
        print("STUDENTS:")
        print("  Username: cnorris    | Password: password123 (Chuck Norris)")
        print("  Username: msherman   | Password: password123 (Mindy Sherman)")
        print("  Username: aranganath | Password: password123 (Aditya Ranganath)")
        print("  Username: nlittle    | Password: password123 (Nancy Little)")
        print("  Username: ychen      | Password: password123 (Yi Wen Chen)")
        print("  Username: jstuart    | Password: password123 (John Stuart)")
        print("\nTEACHERS:")
        print("  Username: ahepworth  | Password: password123 (Dr Hepworth)")
        print("  Username: swalker    | Password: password123 (Susan Walker)")
        print("  Username: rjenkins   | Password: password123 (Ralph Jenkins)")
        print("\nADMIN:")
        print("  Username: admin      | Password: admin123")
        print("\nTo access admin panel, login as admin and navigate to /admin")
        print("="*60)

if __name__ == '__main__':
    init_database()
