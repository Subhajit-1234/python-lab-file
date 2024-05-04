# Mr_Dr is a appoinment booking program

from datetime import datetime, timedelta
import datetime
import random
def privious_menu():
    pass
def secdule():
    current_date = datetime.datetime.now().date()
    next_date = current_date + datetime.timedelta(days=1)
    random_hour = random.randint(10, 16)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    random_time = datetime.time(random_hour, random_minute, random_second)

    print("Your Slot:", next_date)
    print("Your time:", random_time)
def sign_in():
    Name = input("Enter Your Name:")
    ph_no = int(input("Enter Your Phone Number:"))
    age = int(input("Enter Your Age:"))
    if(age >= 18):
        pass
    else:
        print("You are not elegeble for login!!!!!")
        exit()
    
    password = input("Create a password:")
    with open('login.txt', 'a') as f:
        f.write(f"{Name},{ph_no},{password}\n")
def log_in(phone,pass_code):
    name = input("Enter Your Name:")
    with open('login.txt', 'r') as f:
        for line in f:
            name, phone_number, password = line.strip().split(',')
            if(phone == phone_number and pass_code == password):
                print("Login Successfull......")
            else:
                print("Login Failed")
def patient_detal():
    print("Enter 1 if patient first time visiting\n\nEnter 2 many time")
    choice_first = int(input("Enter Your Choice:"))
    match choice_first:
        case 1:
            name = input("Enter Patient Name:")
            Age = int(input("Enter Age:"))
            sex = input("Enter Sex:")
            Phone_number = int(input("Enter Phone Number:"))
            with open('patient.txt', 'a') as f:
                f.write(f"Name:{name} age:{Age} sex:{sex} phone_number:{Phone_number}\n")
        case 2:
            name = input("Enter Patient Name:")
            
def payment():
    print("\nEnter 1 for UPI\n\nEnter 2 for netbanking")
    choice_payment = int(input("Enter your choice:"))
    match choice_payment:
        case 1:
            print("UPI ID:1234567890@okicici and misterdoctor1234@ybl")
        case 2:
            print("AC No. 90876543211234 IFSC Code:SYNB0009542 Branch:Noida Health and care pvt. ltd.")
    transection_id = input("Enter your transection no.")
    with open('t.txt', 'a') as f:
        f.write(f"Transection number:{transection_id}")
    print("\nYour Payment Is Completed")
print("Enter 1 for login\n\nEnter 2 for sign_up")
ch = int(input("Enter your choice:"))
if(ch == 1):
    phone = int(input("Enter your phone number:"))
    pass_code = input("Enter your password:")
    log_in(phone,pass_code)
elif(ch == 2):
    sign_in()
    print("Going to login......")
    phone = int(input("Enter your phone number:"))
    pass_code = input("Enter your password:")
    log_in(phone,pass_code)
else:
    print("Worng input!!!!!\nTry again")
    exit()
cardio = (["Dr. Gaurav Gupta","Exprence = 12 year","MBBS // MD // SURGEN","FEES:900"],["Dr. Mayank Jain","Exprence = 10+ Year","MBBS // MD ","FEES:850"],["Dr. Praveen Mittal","Exprence = 8 Year","MBBS // MD","FEES:850"],["Dr. Partha P Bishnu","Exprence = 9 year","MBBS // MD // SURGEN","FEES:1000"])
eye = (["Dr. Praveen Gupta","Exprence = 12 year","MBBS // MD // SURGEN","FEES:900"],["Dr. Mayank Routh","Exprence = 10+ Year","MBBS // MD ","FEES:850"],["Dr. Rakesh Mittal","Exprence = 8 Year","MBBS // MD","FEES:850"],["Dr. Parthana Banerjee","Exprence = 9 year","MBBS // MD // SURGEN","FEES:1000"])
dentist = (["Dr. Rakesh Gupta","Exprence = 12 year","MBBS // MD // SURGEN","FEES:900"],["Dr. Subhajit Routh","Exprence = 10+ Year","MBBS // MD ","FEES:850"],["Dr. Rakesh Roy","Exprence = 8 Year","MBBS // MD","FEES:850"],["Dr. Parthana Routh","Exprence = 9 year","MBBS // MD // SURGEN","FEES:1000"])
gp = (["Dr. Minakshi Gupta","Exprence = 12 year","FEES:900"],["Dr. Subhajit Aggarwal","Exprence = 10+ Year","FEES:850"],["Dr. Amit Roy","Exprence = 8 Year","FEES:850"],["Dr. Goutam Routh","Exprence = 9 year","FEES:1000"])
# Consultant
c1 = (["Dr. Gaurav Gupta","Exprence = 12 year","MBBS // MD // SURGEN","FEES:900"],["Dr. Mayank Jain","Exprence = 10+ Year","MBBS // MD ","FEES:850"],["Dr. Praveen Mittal","Exprence = 8 Year","MBBS // MD","FEES:850"],["Dr. Partha P Bishnu","Exprence = 9 year","MBBS // MD // SURGEN","FEES:1000"])
c2 = (["Dr. Praveen Gupta","Exprence = 12 year","MBBS // MD // SURGEN","FEES:900"],["Dr. Mayank Routh","Exprence = 10+ Year","MBBS // MD ","FEES:850"],["Dr. Rakesh Mittal","Exprence = 8 Year","MBBS // MD","FEES:850"],["Dr. Parthana Banerjee","Exprence = 9 year","MBBS // MD // SURGEN","FEES:1000"])
c3 = (["Dr. Rakesh Gupta","Exprence = 12 year","MBBS // MD // SURGEN","FEES:900"],["Dr. Subhajit Routh","Exprence = 10+ Year","MBBS // MD ","FEES:850"],["Dr. Rakesh Roy","Exprence = 8 Year","MBBS // MD","FEES:850"],["Dr. Parthana Routh","Exprence = 9 year","MBBS // MD // SURGEN","FEES:1000"])
c4 = (["Dr. Minakshi Gupta","Exprence = 12 year","FEES:900"],["Dr. Subhajit Aggarwal","Exprence = 10+ Year","FEES:850"],["Dr. Amit Roy","Exprence = 8 Year","FEES:850"],["Dr. Goutam Routh","Exprence = 9 year","FEES:1000"])
while True:
    print("Enter 1 for Appointment Booking\n\n Enter 2 for Consultant")
    choice_1 = int(input("Enter Your Choice:"))
    match choice_1:
        case 1:
            a = "Appointment Booking"
            print(a.center(250))
            print("\n\nEnter 1 for Cardiologist\n\nEnter 2 for Eye Specalist\n\nEnter 3 for Dentist\n\nEnter 4 for General Physician\n\nEnter 5 for exit")
            choice_2 = int(input("Enter your choice:"))
            match choice_2:
                case 1:
                    b = "Appointment Booking/Cardiologist"
                    print(b.center(250))
                    print(f"\n\nEnter 1 for {cardio[0]}\n\nEnter 2 for {cardio[1]}\n\nEnter 3 for {cardio[2]}\n\nEnter 4 for {cardio[3]}\n\nEnter 5 for previous menu")
                    choice_3 = int(input("Enter your choice:"))
                    match choice_3:
                        case 1:
                            c = "Appointment Booking/Cardiologist/Booking Confirm"
                            print(c.center(250))
                            for i in cardio[0]:
                                print(i)
                            patient_detal()
                            print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                            choice_4 = int(input("Enter Your Choice:"))
                            match choice_4:
                                        case 1:
                                            d = "Appointment Booking/Cardiologist/Booking Confirm/Payment"
                                            print(d.center(250))
                                            payment()
                                            e = "Appointment Booking/Cardiologist/Booking Confirm/Payment/Time Slot"
                                            print(e.center(230))
                                            for ele in cardio[0]:
                                                print(ele)
                                            secdule()
                                        case 2:
                                            exit()
                                    
                                    
                        case 2:
                                b = "Appointment Booking/Eye Specialist"
                                print(b.center(250))
                                print(f"\n\nEnter 1 for {eye[0]}\n\nEnter 2 for {eye[1]}\n\nEnter 3 for {eye[2]}\n\nEnter 4 for {eye[3]}\n\nEnter 5 for previous menu")
                                choice_3 = int(input("Enter your choice:"))
                                match choice_3:
                                    case 1:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in eye[0]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in eye[0]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 2:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in eye[1]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in eye[1]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 3:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in eye[2]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in eye[2]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 4:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in eye[3]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in eye[3]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 5:
                                        exit()
                        case 3:
                                b = "Appointment Booking/Dentist"
                                print(b.center(250))
                                print(f"\n\nEnter 1 for {dentist[0]}\n\nEnter 2 for {dentist[1]}\n\nEnter 3 for {dentist[2]}\n\nEnter 4 for {dentist[3]}\n\nEnter 5 for previous menu")
                                choice_3 = int(input("Enter your choice:"))
                                match choice_3:
                                    case 1:
                                        c = "Appointment Booking/Deentist/Booking Confirm"
                                        print(c.center(250))
                                        for i in dentist[0]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Dentist/Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Dentist/Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in dentist[0]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 2:
                                        c = "Appointment Booking/Deentist/Booking Confirm"
                                        print(c.center(250))
                                        for i in dentist[1]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Dentist/Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Dentist/Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in dentist[1]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 2:
                                        c = "Appointment Booking/Deentist/Booking Confirm"
                                        print(c.center(250))
                                        for i in dentist[1]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Dentist/Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Dentist/Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in dentist[1]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 3:
                                        c = "Appointment Booking/Deentist/Booking Confirm"
                                        print(c.center(250))
                                        for i in dentist[2]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Dentist/Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Dentist/Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in dentist[2]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 4:
                                        c = "Appointment Booking/Deentist/Booking Confirm"
                                        print(c.center(250))
                                        for i in dentist[3]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Dentist/Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Dentist/Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in dentist[3]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 5:
                                        exit()
                        case 4:
                                b = "Appointment Booking/General Physician"
                                print(b.center(250))
                                print(f"\n\nEnter 1 for {gp[0]}\n\nEnter 2 for {gp[1]}\n\nEnter 3 for {gp[2]}\n\nEnter 4 for {gp[3]}\n\nEnter 5 for previous menu")
                                choice_3 = int(input("Enter your choice:"))
                                match choice_3:
                                    case 1:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in gp[0]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in gp[0]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 2:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in gp[1]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in gp[1]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 3:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in gp[2]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in gp[2]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 4:
                                        c = "Appointment Booking/Eye spe./Booking Confirm"
                                        print(c.center(250))
                                        for i in gp[3]:
                                                    print(i)
                                                    patient_detal()
                                                    print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                    choice_4 = int(input("Enter Your Choice:"))
                                                    match choice_4:
                                                        case 1:
                                                            d = "Appointment Booking/Eye spe./Booking Confirm/Payment"
                                                            print(d.center(250))
                                                            payment()
                                                            e = "Appointment Booking/Eye spe./Booking Confirm/Payment/Time Slot"
                                                            print(e.center(230))
                                                            for ele in gp[3]:
                                                                print(ele)
                                                            secdule()
                                                        case 2:
                                                            exit()
                                    case 5:
                                        exit()
                case 2:
                    a = "Consultant"
                    print(a.center(250))
                    print("\n\nEnter 1 for Cardiologist\n\nEnter 2 for Eye Specalist\n\nEnter 3 for Dentist\n\nEnter 4 for General Physician\n\nEnter 5 for exit")
                    choice_2 = int(input("Enter your choice:"))
                    match choice_2:
                            case 1:
                                b = "Consultant/Cardiologist"
                                print(b.center(250))
                                print(f"\n\nEnter 1 for {c1[0]}\n\nEnter 2 for {c1[1]}\n\nEnter 3 for {c1[2]}\n\nEnter 4 for {c1[3]}\n\nEnter 5 for previous menu")
                                choice_3 = int(input("Enter your choice:"))
                                match choice_3:
                                    case 1:
                                        c = "Consultant/Cardiologist/Booking Confirm"
                                        print(c.center(250))
                                        for i in c1[0]:
                                            print(i)
                                        patient_detal()
                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                        choice_4 = int(input("Enter Your Choice:"))
                                        match choice_4:
                                            case 1:
                                                d = "Consultant/Cardiologist/Booking Confirm/Payment"
                                                print(d.center(250))
                                                payment()
                                                e = "Consultant/Cardiologist/Booking Confirm/Payment/Time Slot"
                                                print(e.center(230))
                                                for ele in c1[0]:
                                                    print(ele)
                                                secdule()
                                            case 2:
                                                exit()
                                    case 2:
                                        c = "Consultant/Cardiologist/Booking Confirm"
                                        print(c.center(250))
                                        for i in c1[1]:
                                            print(i)
                                        patient_detal()
                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                        choice_4 = int(input("Enter Your Choice:"))
                                        match choice_4:
                                            case 1:
                                                d = "Consultant/Cardiologist/Booking Confirm/Payment"
                                                print(d.center(250))
                                                payment()
                                                e = "Consultant/Cardiologist/Booking Confirm/Payment/Time Slot"
                                                print(e.center(230))
                                                for ele in c1[1]:
                                                    print(ele)
                                                secdule()
                                            case 2:
                                                exit()
                            case 3:
                                c = "Consultant/Cardiologist/Booking Confirm"
                                print(c.center(250))
                                for i in c1[2]:
                                    print(i)
                                patient_detal()
                                print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                choice_4 = int(input("Enter Your Choice:"))
                                match choice_4:
                                    case 1:
                                        d = "Consultant/Cardiologist/Booking Confirm/Payment"
                                        print(d.center(250))
                                        payment()
                                        e = "Consultant/Cardiologist/Booking Confirm/Payment/Time Slot"
                                        print(e.center(230))
                                        for ele in c1[2]:
                                            print(ele)
                                        secdule()
                                    case 2:
                                        exit()
                            case 4:
                                c = "Consultant/Cardiologist/Booking Confirm"
                                print(c.center(250))
                                for i in c1[3]:
                                    print(i)
                                patient_detal()
                                print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                choice_4 = int(input("Enter Your Choice:"))
                                match choice_4:
                                    case 1:
                                        d = "Consultant/Cardiologist/Booking Confirm/Payment"
                                        print(d.center(250))
                                        payment()
                                        e = "Consultant/Cardiologist/Booking Confirm/Payment/Time Slot"
                                        print(e.center(230))
                                        for ele in c1[3]:
                                            print(ele)
                                        secdule()
                                    case 2:
                                        exit()
                            case 5:
                                exit()
                                
                            
                            case 2:
                                    b = "Consultant/Eye Specialist"
                                    print(b.center(250))
                                    print(f"\n\nEnter 1 for {c2[0]}\n\nEnter 2 for {c2[1]}\n\nEnter 3 for {c2[2]}\n\nEnter 4 for {c2[3]}\n\nEnter 5 for previous menu")
                                    choice_3 = int(input("Enter your choice:"))
                                    match choice_3:
                                        case 1:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c2[0]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c2[0]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 2:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c2[1]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c2[1]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 3:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c2[2]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c2[2]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 4:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c2[3]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c2[3]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 5:
                                            exit()
                            case 3:
                                    b = "Consultant/Dentist"
                                    print(b.center(250))
                                    print(f"\n\nEnter 1 for {dentist[0]}\n\nEnter 2 for {dentist[1]}\n\nEnter 3 for {dentist[2]}\n\nEnter 4 for {dentist[3]}\n\nEnter 5 for previous menu")
                                    choice_3 = int(input("Enter your choice:"))
                                    match choice_3:
                                        case 1:
                                            c = "Consultant/Deentist/Booking Confirm"
                                            print(c.center(250))
                                            for i in dentist[0]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Dentist/Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Dentist/Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in dentist[0]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 2:
                                            c = "Consultant/Deentist/Booking Confirm"
                                            print(c.center(250))
                                            for i in dentist[1]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Dentist/Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Dentist/Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in dentist[1]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 3:
                                            c = "Consultant/Deentist/Booking Confirm"
                                            print(c.center(250))
                                            for i in dentist[2]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Dentist/Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Dentist/Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in dentist[2]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 4:
                                            c = "Consultant/Deentist/Booking Confirm"
                                            print(c.center(250))
                                            for i in dentist[3]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Dentist/Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Dentist/Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in dentist[3]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 5:
                                            exit()
                            case 4:
                                    b = "Consultant/General Physician"
                                    print(b.center(250))
                                    print(f"\n\nEnter 1 for {c3[0]}\n\nEnter 2 for {c3[1]}\n\nEnter 3 for {c3[2]}\n\nEnter 4 for {c3[3]}\n\nEnter 5 for exit")
                                    choice_3 = int(input("Enter your choice:"))
                                    match choice_3:
                                        case 1:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c3[0]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c3[0]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 2:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c3[1]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c3[1]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 3:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c3[2]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c3[2]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 4:
                                            c = "Consultant/Eye spe./Booking Confirm"
                                            print(c.center(250))
                                            for i in c3[3]:
                                                        print(i)
                                                        patient_detal()
                                                        print("\n\nEnter 1 Payment\n\nEnter 2 for exit")
                                                        choice_4 = int(input("Enter Your Choice:"))
                                                        match choice_4:
                                                            case 1:
                                                                d = "Consultant/Eye spe./Booking Confirm/Payment"
                                                                print(d.center(250))
                                                                payment()
                                                                e = "Consultant/Eye spe./Booking Confirm/Payment/Time Slot"
                                                                print(e.center(230))
                                                                for ele in c3[3]:
                                                                    print(ele)
                                                                secdule()
                                                            case 2:
                                                                exit()
                                        case 5:
                                                exit()
