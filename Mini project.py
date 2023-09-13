from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
def Database():
    global conn,cursor
    conn=  mysql.connector.connect(host="localhost",user="root",password="Kam@15")
    cursor= conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS DBMSPRO")
    cursor.execute("USE DBMSPRO")
    cursor.execute("CREATE TABLE IF NOT EXISTS userinfo (first_name varchar(40), last_name varchar(30),age varchar(3),address varchar(30),city varchar(50),user_name varchar(30) PRIMARY KEY NOT NULL, password varchar(30))")
       
#---------------------------------------------------------------Login Function --------------------------------------
def clear():
    userentry.delete(0,END)
    passentry.delete(0,END)

def close():
    win.destroy()   


def login():
    Database()
    a=w.get()
    
    if user_name.get()=="" or password.get()=="": 
        messagebox.showerror("Error","Enter Username and Password",parent=win)

    else:
        try:
            con = mysql.connector.connect(host="localhost",user="root",password="Kam@15",database="DBMSPRO")
            cur = con.cursor()

            cur.execute("select * from userinfo where user_name= %s and password = %s",(user_name.get(),password.get()))
            row = cur.fetchone()

            if row==None:
                messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

            else:
                if a=="Patient":
                    messagebox.showinfo("Success" , "Successfully Login as Patient" , parent = win)
                    close()
                    userWindow = tk.Tk()
                    userWindow.title("Patient Management System")
                    userWindow.geometry("500x500")
                    userWindow.configure(bg = '#D1FFBD')
                    # Create a label for the heading
                    heading = tk.Label(userWindow, text="Patient View", font=("Arial", 25, 'bold'), bg = '#D1FFBD')
                    heading.pack(pady=20)
                    def fun():
                        window = tk.Tk()
                        window.title("Patient Information")
                        window.geometry("400x400")

                        # Create labels and input fields for patient information
                        patient_id_label = tk.Label(window, text="Patient ID:")
                        patient_id_label.pack()
                        patient_id_entry = tk.Entry(window)
                        patient_id_entry.pack()

                        symptoms_label = tk.Label(window, text="Symptoms:")
                        symptoms_label.pack()
                        symptoms_entry = tk.Entry(window)
                        symptoms_entry.pack()

                        tests_label = tk.Label(window, text="Tests:")
                        tests_label.pack()
                        tests_entry = tk.Entry(window)
                        tests_entry.pack()

                        family_history_label = tk.Label(window, text="Family History:")
                        family_history_label.pack()
                        family_history_entry = tk.Entry(window)
                        family_history_entry.pack()

                        diagnosis_date_label = tk.Label(window, text="diagnosis_date:")
                        diagnosis_date_label.pack()
                        diagnosis_date_entry = tk.Entry(window)
                        diagnosis_date_entry.pack()

                        tscore_label = tk.Label(window, text="T-Score(0-4):")
                        tscore_label.pack()
                        tscore_entry = tk.Entry(window)
                        tscore_entry.pack()

                        nscore_label = tk.Label(window, text="N-Score(0-3):")
                        nscore_label.pack()
                        nscore_entry = tk.Entry(window)
                        nscore_entry.pack()

                        mscore_label = tk.Label(window, text="M-Score(0-1):")
                        mscore_label.pack()
                        mscore_entry = tk.Entry(window)
                        mscore_entry.pack()

                        # Create a function to store the input values in the MySQL database
                        def save_data():
                            # Get the input values
                            patient_id = patient_id_entry.get()
                            symptoms = symptoms_entry.get()
                            tests = tests_entry.get()
                            family_history = family_history_entry.get()
                            tscore = tscore_entry.get()
                            nscore = nscore_entry.get()
                            mscore = mscore_entry.get()
                            diagnosis_date=diagnosis_date_entry.get()
                            
                            if (patient_id == "") or (symptoms == "") or (tests == "")  or (tscore == "") or (nscore =="") or (mscore =="") :
                                    message_label.config(text="Please fill all the data")
                            else:  

                                    # Connect to the MySQL database
                                    mydb = mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="Kam@15",
                                            database="DBMSPRO"
                                    )
                                
                                    # Create a cursor object to execute SQL queries
                                    mycursor = mydb.cursor()
                                
                                    # Insert the input values into the database
                                    sql = "INSERT INTO patients (patient_id, symptoms, tests, family_history, tscore, nscore, mscore) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                                    val = (patient_id, symptoms, tests, family_history, tscore, nscore, mscore)
                                    sql1 = "INSERT diagnosis3 (patient_id,diagnosis_date) VALUES (%s,%s)"
                                    val1 = (patient_id, diagnosis_date,)
                                    #sql1 = "Insert into diagnosis3(patient_id,diagnosis_date) values (%s,%s,)"
                                    #val1 = (patient_id,diagnosis_date)
                                    mycursor.execute(sql, val)
                                    mycursor.execute(sql1,val1)
                                
                                    # Commit the changes to the database
                                    mydb.commit()
                                    mycursor.execute("select patient_id, symptoms, tests, family_history, tscore, nscore, mscore from patients where patient_id='%s'"%(patient_id))
                                    e=mycursor.fetchone()
                                
                                    # Close the database connection
                                    mydb.close()
                                    patient_id_entry.delete(0, tk.END)
                                    symptoms_entry.delete(0, tk.END)
                                    tests_entry.delete(0, tk.END)
                                    family_history_entry.delete(0, tk.END)
                                    tscore_entry.delete(0, tk.END)
                                    nscore_entry.delete(0, tk.END)
                                    mscore_entry.delete(0, tk.END)
                                    messagebox.showinfo("Data Saved Succesfully",e)
                                            

                        # Create a button to save the input values to the database
                        save_button = tk.Button(window, text="Save", command=save_data)
                        save_button.pack()

                        # Create a label to display messages
                        message_label = tk.Label(window, text="")
                        message_label.pack()
                        window.mainloop()
                    def fun2():
                            def retrieve_scores():
                                # Connect to the MySQL database
                                db = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Kam@15",
                                    database="DBMSPRO"
                                )
                                
                                # Create a cursor object to execute SQL queries
                                cursor = db.cursor()
                                
                                # Retrieve the scores for the given patient ID
                                patient_id = patient_id_entry.get()
                                hor=w1.get()
                                
                                query = "SELECT tscore, nscore, mscore FROM patients WHERE patient_id = %s"
                                cursor.execute(query, (patient_id,))
                                scores = cursor.fetchone()

                                # Check if the scores were found
                                if scores is None:
                                    result_label.config(text="Invalid ID")
                                # Check if the T-score is 1
                                elif (scores[0] == "is") and (scores[1] == "0") and (scores[2] == "0"):
                                    stage=0
                                    result_label.config(text="Stage 0\nThe tumor has not started growing into healthy breast tissue.\nNearby lymph nodes don't contain cancer.\nNo distant metastasis. ")
                                elif (scores[0] == "1") and (scores[1] == "0") and (scores[2] == "0"):
                                    stage=1
                                    
                                    result_label.config(text="Stage 1\nThe tumor has shown minimal growth.\nNearby lymph nodes don't contain cancer.\nNo distant metastasis. ")
                                elif (scores[0] == "0") and (scores[1] == "1 mi") and (scores[2] == "0"):
                                    stage=1
                                    result_label.config(text="Stage 1\nThe tumor has not started growing into healthy breast tissue.\nMore than 200 cancer cells fornd in lymph nodes.\nNo distant metastasis. ")

                                elif (scores[0] == "0") and (scores[1] == "1") and (scores[2] == "0"):
                                    stage=2
                                    result_label.config(text="Stage 2\nThe tumor has not started growing into healthy breast tissue.\nCancer found in 1-3 axillary lymph nodes.\nNo distant metastasis. ")	

                                elif (scores[0] == "1") and (scores[1] == "1") and (scores[2] == "0"):
                                    stage=2
                                    result_label.config(text="Stage 2\nThe tumor has shown minimal growth.\nCancer found in 1-3 axillary lymph nodes.\nNo distant metastasis. ")	
                                elif (scores[0] == "2") and (scores[1] == "0") and (scores[2] == "0"):
                                    stage=2
                                    result_label.config(text="Stage 2\nThe tumor is graeter than 2cm but less than 5cm.\nNearby lymph nodes don't contain cancer.\nNo distant metastasis. ")
                                elif (scores[0] == "2") and (scores[1] == "1") and (scores[2] == "0"):
                                    stage="2A"
                                    result_label.config(text="Stage 2\nThe tumor is graeter than 2cm but less than 5cm.\nCancer found in 1-3 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[0] == "3") and (scores[1] == "0") and (scores[2] == "0"):
                                    stage=2
                                    result_label.config(text="Stage 2\nThe tumor is graeter than 5cm.\nNearby lymph nodes don't contain cancer.\nNo distant metastasis. ")

                                elif (scores[0] == "0") and (scores[1] == "2") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nThe tumor has not started growing into healthy breast tissue.\nCancer found in 4-9 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[0] == "1") and (scores[1] == "2") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nThe tumor has shown minimal growth.\nCancer found in 4-9 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[0] == "2") and (scores[1] == "2") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nThe tumor is graeter than 2cm but less than 5cm.\nCancer found in 4-9 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[0] == "3") and (scores[1] == "1") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nThe tumor is graeter than 5cm.\nCancer found in 1-3 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[0] == "3") and (scores[1] == "2") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nThe tumor is graeter than 5cm.\nCancer found in 4-9 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[0] == "4") and (scores[1] == "0") and (scores[2] == "0"):
                                    result_label.config(text="Stage 3B\nInvasive tumor with direct extension to the chest wall and/or to the skin\nNearby lymph nodes don't contain cancer.\nNo distant metastasis. ")
                                elif (scores[0] == "4") and (scores[1] == "1") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nInvasive tumor with direct extension to the chest wall and/or to the skin\nCancer found in 1-3 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[0] == "4") and (scores[1] == "2") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nInvasive tumor with direct extension to the chest wall and/or to the skin\nCancer found in 4-9 axillary lymph nodes.\nNo distant metastasis. ")
                                elif (scores[1] == "3") and (scores[2] == "0"):
                                    stage=3
                                    result_label.config(text="Stage 3\nCancer found in 10+ axillary lymph nodes.\nNo distant metastasis. ")

                                elif (scores[2] == "1"):
                                    stage=4
                                    result_label.config(text="Stage 4\nThe cancer has traveled to other parts of the body.")

                                else:
                                    result_label.config(text="Could not analyze results")
                                
                                update_query = "UPDATE patients SET stage = %s WHERE patient_id = %s"
                                cursor.execute(update_query, (stage, patient_id,))
                                update_query1 = "UPDATE diagnosis3  SET stage = %s WHERE patient_id = %s"
                                cursor.execute(update_query1, (stage, patient_id,))
                                db.commit()
                                a="SELECT cancer_type, hormone_receptor_status, her2_status FROM diagnosis1 where stage=%s and hormone_receptor_status=%s"
                                cursor.execute(a, (stage,hor,))
                                te= cursor.fetchone()
                                if te is not None:
                                      value=te[0]
                                      value2=te[1]
                                      value3=te[2]
                                      #r="insert into diagnosis3 (patient_id,cancer_type,hormone_receptor_status, her2_status) values (%s,%s,%s,%s)"
                                      r="update diagnosis3 set cancer_type=%s,hormone_receptor_status=%s, her2_status=%s where patient_id=%s"
                                      cursor.execute(r,(value,value2,value3,patient_id,))
                                      #cursor.execute("select patient_id1,cancer_type,hormone_receptor_status, her2_status from diagnosis where patient_id='%s'"%(patient_id))
                                      db.commit()
                                # Close the database connection
                                db.close()
                                """messagebox.showinfo("Data Saved Succesfully",e)"""

                            # Create the tkinter window
                            roottp1 = tk.Tk()
                            roottp1.title("Score Retrieval")
                            roottp1.geometry("500x500")

                            # Create a label and entry for the patient ID
                            patient_id_label = tk.Label(roottp1, text="Patient ID:",font='Verdana 10 bold')
                            patient_id_label.pack()
                            patient_id_entry = tk.Entry(roottp1)
                            patient_id_entry.pack()
                            a=Label(roottp1,text="Hormone Receptor Status: ",font = 'Verdana 10 bold')
                            #a.place(x=80,y=190)
                            a.pack()
                            w1=ttk.Combobox(roottp1,values=["ER/PR-positive","ER-negative/PR-negative","ER/PR-negative"])
                            #w1.place(x=180, y=190, width=100)
                            w1.pack()    

                            
                            ## Create a button to retrieve the scores
                            retrieve_button = tk.Button(roottp1, text="Calculate Results", command=retrieve_scores)
                            retrieve_button.pack(pady = 15)
                            Label(roottp1,text="Yesterday I dared to struggle Today I dare to win!",font="verdana 10 italic", fg = 'green').pack(pady = 15)
                            Label(roottp1,text="Book Your Appointment with us!",font="verdana 10", fg = 'green').pack()

                         

                            # Create a label to display the result
                            result_label = tk.Label(roottp1, text="")
                            result_label.pack()
                            # Create a frame to hold the buttons
                            button_frame = tk.Frame(roottp1)
                            button_frame.pack()

                            """# Create a button to go back to the home page
                            home_button = tk.Button(button_frame, text="Home")
                            home_button.pack(side="left")"""
                            def fun3():
                                def submit_appointment():
                                        # Retrieve the entered values
                                        patient_id = id_entry.get()
                                        appointment_date = date_entry.get()
                                        appointment_reason = reason_entry.get("1.0", tk.END).strip()
                                        mydb = mysql.connector.connect(
                                            host="localhost",
                                            user="root",
                                            password="Kam@15",
                                            database="DBMSPRO"
                                        )
                                
                                    # Create a cursor object to execute SQL queries
                                        mycursor1 = mydb.cursor()
                                
                                    # Insert the input values into the database
                                        sql1 = "INSERT INTO appointments (patient_id3, appointment_date, appointment_reason) VALUES (%s, %s, %s)"
                                        val1 = (patient_id,appointment_date,appointment_reason)
                                        mycursor1.execute(sql1, val1)
                                
                                    # Commit the changes to the database
                                        mydb.commit()
                                        mydb.close()
                                        id_entry.delete(0, tk.END)
                                        date_entry.delete(0, tk.END)
                                        reason_entry.delete("1.0", tk.END)

                                root1 =tk.Tk()
                                root1.title("Appointment Window")

                                # Create labels and entry fields
                                id_label = tk.Label(root1, text="Patient ID:")
                                id_label.pack()
                                id_entry = tk.Entry(root1)
                                id_entry.pack()

                                date_label = tk.Label(root1, text="Appointment Date:")
                                date_label.pack()
                                date_entry = tk.Entry(root1)
                                date_entry.pack()

                                reason_label = tk.Label(root1, text="Appointment Reason:")
                                reason_label.pack()
                                reason_entry = tk.Text(root1, height=5)
                                reason_entry.pack()

                                # Create the submit button
                                submit_button = tk.Button(root1, text="Submit", command=submit_appointment)
                                submit_button.pack(pady=10)

                                # Start the main tkinter event loop
                                root1.mainloop()

        


                            # Create a button to go to appointments

                            appointments_button = tk.Button(button_frame, text="Book Appointment",command=fun3)
                            appointments_button.pack(pady=10)

                            # Run the tkinter event loop
                            roottp1.mainloop()
                    def fun5():
                        def showed():
                                # Get the patient ID entered by the user
                                patient_id = entry.get()

                                # Connect to the MySQL database
                                connection = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Kam@15",
                                    database="DBMSPRO"
                                )

                                # Create a cursor object to execute SQL queries
                                cursor = connection.cursor()

                                # Execute the SQL query to fetch the patient report
                                cursor.execute("SELECT * FROM diagnosis3 d JOIN treatments t ON d.stage=t.stage WHERE d.stage = (SELECT stage FROM patients WHERE patient_id = %s) and patient_id=%s", (patient_id,patient_id,))

                                # Fetch the row from the result
                                row = cursor.fetchone()

                                # Close the cursor and connection
                                cursor.close()
                                connection.close()

                                # Display the fetched data in a new window
                                display_window = tk.Toplevel(root5)
                                display_window.title("Patient Report")

                                # Create a text widget to display the data
                                text_widget = tk.Text(display_window, height=20, width=80)
                                text_widget.pack(padx=13, pady=15)

                                #text_widget.pack()

                                # Check if a report is found for the given patient ID
                                if row is not None:
                                    text_widget.insert(tk.END, f"Patient ID:  ", "tag_patient_id")
                                    text_widget.insert(tk.END, f"{row[1]}\n")
                                    text_widget.insert(tk.END, f"Stage:  ", "tag_stage")
                                    text_widget.insert(tk.END, f"{row[2]}\n")
                                    text_widget.insert(tk.END, f"Cancer Type:  ", "tag_Cancer_Type")
                                    text_widget.insert(tk.END, f"{row[3]}\n")
                                    text_widget.insert(tk.END, f"Hormone Receptor:  ", "tag_Hormone_Receptor")
                                    text_widget.insert(tk.END, f"{row[4]}\n")
                                    text_widget.insert(tk.END, f"Her2 Status:  ", "tag_Her2_Status")
                                    text_widget.insert(tk.END, f"{row[5]}\n")
                                    text_widget.insert(tk.END, f"Diagnosis Date:  ", "tag_Diagnosis_Date")
                                    text_widget.insert(tk.END, f"{row[6]}\n")
                                    text_widget.insert(tk.END, f"Surgery Type:  ", "tag_Surgery_Type")
                                    text_widget.insert(tk.END, f"{row[8]}\n")
                                    text_widget.insert(tk.END, f"Chemotherapy Type:  ", "tag_Chemotherapy_Type")
                                    text_widget.insert(tk.END, f"{row[9]}\n")
                                    text_widget.insert(tk.END, f"Radiation Therapy Type:  ", "tag_Radiation_Therapy_Type")
                                    text_widget.insert(tk.END, f"{row[10]}\n")
                                    text_widget.insert(tk.END, f"Hormone Therapy Type:  ", "tag_Hormone_Therapy_Type")
                                    text_widget.insert(tk.END, f"{row[11]}\n")
                                    text_widget.insert(tk.END, f"Targated Therapy Type:  ", "tag_Targated_Therapy_Type")
                                    text_widget.insert(tk.END, f"{row[12]}\n")
                                    #text_widget.insert(tk.END, f"Treatment Start Date:  ", "tag_Treatment_Start_Date")
                                    #text_widget.insert(tk.END, f"{row[14]}\n")
                                    #text_widget.insert(tk.END, f"Treatment End Date:  ", "tag_Treatment_End_Date")
                                    #text_widget.insert(tk.END, f"{row[15]}\n")

                                else:
                                    text_widget.insert(tk.END, "No report found for the given patient ID.")
                                
                                    # Make the text widget read-only
                                    text_widget.configure(state="disabled")

                                    # Apply tag configurations for highlighting
                                    text_widget.tag_config("tag_patient_id", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_stage", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Cancer_Type", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Hormone_Receptor", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Her2_Status", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Diagnosis_Date", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Surgery_Type", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Chemotherapy_Type", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Radiation_Therapy_Type", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Hormone_Therapy_Type", font=("Arial",9,"bold"))
                                    text_widget.tag_config("tag_Targated_Therapy_Type", font=("Arial",9,"bold"))
                                    #text_widget.tag_config("tag_Treatment_Start_Date", font=("Arial",9,"bold"))
                                    #text_widget.tag_config("tag_Treatment_End_Date", font=("Arial",9,"bold"))
                        root5 = tk.Tk()
                        root5.title("Patient Report Viewer")
                        root5.geometry("500x300")

                                # Create a label and entry for the patient ID
                        label = tk.Label(root5, text="Patient ID:",font=("Arial",10))
                        label.pack()
                        entry = tk.Entry(root5)
                        entry.pack()

                            # Create a button to fetch and display data
                        fetch_button = tk.Button(root5, text="Fetch Report",font=("Arial",10) ,command=showed)
                        fetch_button.pack()

                            # Start the Tkinter event loop
                        root5.mainloop()



                    #Create the two buttons
                    details_button = tk.Button(userWindow, text="Patient Details", font=("Arial", 14),command=fun, bg='#D1FFBD')
                    details_button.pack(pady=10)

                    consultation_button = tk.Button(userWindow, text="Consultation", font=("Arial", 14),command=fun2,  bg='#D1FFBD')
                    consultation_button.pack(pady=10)

                    report_button=tk.Button(userWindow, text="Medical Report", font=("Arial", 14),command=fun5, bg='#D1FFBD')
                    report_button.pack(pady=10)
                    userWindow.mainloop()

                      
                else:
                     messagebox.showinfo("Success" , "Successfully Login as Doctor" , parent = win)
                     close()
                     def fun9():
                         def search_action():
                            print("Search button clicked")
                            db = mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password="Kam@15",
                                    database="DBMSPRO"
                                )
                            cursor = db.cursor()
                            patient_id = entry.get()
                            cursor.execute("SELECT * FROM diagnosis3 d JOIN treatments t ON d.stage=t.stage WHERE d.stage = (SELECT stage FROM patients WHERE patient_id = %s) and patient_id=%s", (patient_id,patient_id,))

                                # Fetch the row from the result
                            row = cursor.fetchone()

                                # Close the cursor and connection
                            cursor.close()
                            db.close()

                                # Display the fetched data in a new window
                            display_window = tk.Toplevel(root6)
                            display_window.title("Patient Report searched")

                                # Create a text widget to display the data
                            text_widget = tk.Text(display_window, height=20, width=80)
                            text_widget.pack(padx=13, pady=15)

                                #text_widget.pack()

                                # Check if a report is found for the given patient ID
                            if row is not None:
                                text_widget.insert(tk.END, f"Patient ID:  ", "tag_patient_id")
                                text_widget.insert(tk.END, f"{row[1]}\n")
                                text_widget.insert(tk.END, f"Stage:  ", "tag_stage")
                                text_widget.insert(tk.END, f"{row[2]}\n")
                                text_widget.insert(tk.END, f"Cancer Type:  ", "tag_Cancer_Type")
                                text_widget.insert(tk.END, f"{row[3]}\n")
                                text_widget.insert(tk.END, f"Hormone Receptor:  ", "tag_Hormone_Receptor")
                                text_widget.insert(tk.END, f"{row[4]}\n")
                                text_widget.insert(tk.END, f"Her2 Status:  ", "tag_Her2_Status")
                                text_widget.insert(tk.END, f"{row[5]}\n")
                                text_widget.insert(tk.END, f"Diagnosis Date:  ", "tag_Diagnosis_Date")
                                text_widget.insert(tk.END, f"{row[6]}\n")
                                text_widget.insert(tk.END, f"Surgery Type:  ", "tag_Surgery_Type")
                                text_widget.insert(tk.END, f"{row[8]}\n")
                                text_widget.insert(tk.END, f"Chemotherapy Type:  ", "tag_Chemotherapy_Type")
                                text_widget.insert(tk.END, f"{row[9]}\n")
                                text_widget.insert(tk.END, f"Radiation Therapy Type:  ", "tag_Radiation_Therapy_Type")
                                text_widget.insert(tk.END, f"{row[10]}\n")
                                text_widget.insert(tk.END, f"Hormone Therapy Type:  ", "tag_Hormone_Therapy_Type")
                                text_widget.insert(tk.END, f"{row[11]}\n")
                                text_widget.insert(tk.END, f"Targated Therapy Type:  ", "tag_Targated_Therapy_Type")
                                text_widget.insert(tk.END, f"{row[12]}\n")
                                    #text_widget.insert(tk.END, f"Treatment Start Date:  ", "tag_Treatment_Start_Date")
                                    #text_widget.insert(tk.END, f"{row[14]}\n")
                                    #text_widget.insert(tk.END, f"Treatment End Date:  ", "tag_Treatment_End_Date")
                                    #text_widget.insert(tk.END, f"{row[15]}\n")

                            else:
                                text_widget.insert(tk.END, "No report found for the given patient ID.")
                                
                                    # Make the text widget read-only
                                text_widget.configure(state="disabled")

                                    # Apply tag configurations for highlighting
                                text_widget.tag_config("tag_patient_id", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_stage", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Cancer_Type", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Hormone_Receptor", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Her2_Status", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Diagnosis_Date", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Surgery_Type", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Chemotherapy_Type", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Radiation_Therapy_Type", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Hormone_Therapy_Type", font=("Arial",9,"bold"))
                                text_widget.tag_config("tag_Targated_Therapy_Type", font=("Arial",9,"bold"))
                                    #text_widget.tag_config("tag_Treatment_Start_Date", font=("Arial",9,"bold"))
                                    #text_widget.tag_config("tag_Treatment_End_Date", font=("Arial",9,"bold"))
                         root6 = tk.Tk()
                         root6.title("Patient Record Search")
                         root6.geometry("500x300")

                                # Create a label and entry for the patient ID
                         label = tk.Label(root6, text="Patient ID:",font=("Arial",10))
                         label.pack()
                         entry = tk.Entry(root6)
                         entry.pack()
                         search_button = tk.Button(root6, text="Fetch Report",font=("Arial",10) ,command=search_action)
                         search_button.pack()

                            # Start the Tkinter event loop
                         root6.mainloop()
                            
                     def fun4():
                         def tu_update():
                            db= mysql.connector.connect(
                                 host="localhost",
                                 user="root",
                                 password="Kam@15",
                                 database="DBMSPRO"
                                    )
                            cursor1 = db.cursor()
                            appointment_id = appointment_id_entry.get()
                            new_date = date_entry.get()
                            new_notes = notes_entry.get()
                            update_query = "UPDATE appointments SET appointment_date = %s, appointment_notes = %s WHERE patient_id3 = %s"
                            #values = (new_date, new_notes, appointment_id,)
                            cursor1.execute(update_query,(new_date, new_notes, appointment_id,))
                            db.commit()
                            db.close()
                            message_label.config(text="Appointment updated successfully!", fg="green")
                           
                         rootp1 = tk.Tk()
                         rootp1.title("Update window")
                         rootp1.geometry("400x400")

                        # Create labels and entry fields for appointment details
                         appointment_id_label = tk.Label(rootp1, text="Appointment ID:")
                         appointment_id_label.pack()
                         appointment_id_entry = tk.Entry(rootp1)
                         appointment_id_entry.pack()

                         date_label = tk.Label(rootp1, text="New Date:")
                         date_label.pack()
                         date_entry = tk.Entry(rootp1)
                         date_entry.pack()

                         notes_label = tk.Label(rootp1, text="New Notes:")
                         notes_label.pack()
                         notes_entry = tk.Entry(rootp1)
                         notes_entry.pack()

                        # Create the update button
                         update_button1 = tk.Button(rootp1, text="Update Appointment", command= tu_update)
                         update_button1.pack()

                        # Create a label to display update status
                         message_label = tk.Label(rootp1, text="")
                         message_label.pack()

                            # Start the tkinter event loop
                         rootp1.mainloop()
                     def fun7():
                        window1 = tk.Tk()
                        window1.title("Appointments")

                        # Create a treeview to display the data
                        tree = ttk.Treeview(window1)
                        tree["columns"] = ("appointment_id", "patient_id3","appointment_date","appointment_reason","appointment_notes")
                        tree.column("#0", width=0, stretch=tk.NO)
                        tree.column("appointment_id", anchor=tk.CENTER, width=100)
                        tree.column("patient_id3", anchor=tk.CENTER, width=100)
                        tree.column("appointment_date", anchor=tk.W, width=200)
                        tree.column("appointment_reason", anchor=tk.W, width=200)
                        tree.column("appointment_notes", anchor=tk.W, width=200)

                        tree.heading("#0", text="")
                        tree.heading("appointment_id", text="Appointment ID")
                        tree.heading("patient_id3", text="Patient ID")
                        tree.heading("appointment_date", text="Appointment Date")
                        tree.heading("appointment_reason", text="Appointment Reason")
                        tree.heading("appointment_notes", text="Appointment Notes")

                        # Connect to the MySQL database
                        connection = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="Kam@15",
                            database="dbmspro"
                        )

                        # Create a cursor to execute SQL queries
                        cursor = connection.cursor()

                        # Execute the SQL query to retrieve data from the appointments table
                        cursor.execute("SELECT appointment_id, patient_id3, appointment_date, appointment_reason, appointment_notes FROM appointments")

                        # Fetch all the rows returned by the query
                        rows = cursor.fetchall()

                        # Insert the data into the treeview
                        for row in rows:
                            tree.insert("", tk.END, values=row)

                        # Close the cursor and connection
                        cursor.close()
                        connection.close()

                        # Pack the treeview into the window
                        tree.pack(fill=tk.BOTH, expand=True)

                        # Start the Tkinter event loop
                        window1.mainloop()




                            # Create the main window
                                     # Create the main window
                     root = tk.Tk()
                     root.title("Doctor Dashboard")
                     root.geometry("400x400")
                     root.configure(bg='#D1FFBD')
                     heading = tk.Label(root, text = 'Doctor View', font =('Affair',25,'bold'), bg = '#D1FFBD')
                     heading.pack(pady = 10)

                                # Create a frame
                     frame = tk.Frame(root, bg = '#D1FFBD')
                     frame.pack(padx=40, pady=40)

                                # Create a search button
                     search_button = tk.Button(frame, text="Search",font=("Arial", 14), command=fun9, bg = '#D1FFBD')
                     search_button.pack(pady=10)

                                # Create an update button
                     update_button = tk.Button(frame, text="Update",font=("Arial", 14),command=fun4, bg = '#D1FFBD')
                     update_button.pack(pady=10)

                     show_button = tk.Button(frame, text="Show appointment",font=("Arial", 14),command=fun7, bg = '#D1FFBD')
                     show_button.pack(pady=10)

                                # Start the main tkinter event loop
                     root.mainloop()
            con.close()
        except Exception as es:
            messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = win)

#---------------------------------------------------------------End Login Function ---------------------------------


#-----------------------------------------------------------Signup FUNCTION --------------------------------------------------
def signup():
    special_ch = ["$","@","_"]
    # signup database connect 
    def action():
        if first_name.get()=="" or last_name.get()=="" or age.get()=="" or add.get()=="" or city.get()=="" or user_name.get()=="" or password.get()=="" or con_pass.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
        elif password.get() != con_pass.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        elif not any(ch.isupper() for ch in password.get()):
            messagebox.showerror("Error","Atleast 1 uppercase character required!")
        elif not any(ch.islower() for ch in password.get()):
            messagebox.showerror ("Error","Atleast 1 lowercase character required!")
        elif not any(ch in special_ch for ch in password.get()):
            messagebox.showerror("Error","Atleast 1 special character required!")
        elif not any(ch.isdigit() for ch in password.get()):
            messagebox.showerror("Error","Atleast 1 number is required!")
        elif len(password.get()) < 8:
            messagebox.showerror("Error","Password must be minimum of 8 characters")
            
        else:
                    try:
                            con = mysql.connector.connect(host="localhost",user="root",password="Kam@15",database="DBMSPRO")
                            cur = con.cursor()
                            a=first_name.get()
                            b=last_name.get()
                            c=age.get()
                            d=add.get()
                            e=city.get()
                            g=user_name.get()
                            h=password.get()
                            data=(a,b,c,d,e,g,h)
                            Database()
                            cur.execute("select * from userinfo where user_name= %s",(g,))
                            row = cur.fetchone()
                            
                            if row!=None:
                                messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                                
                            else:
                                    cur.execute("insert into userinfo(first_name,last_name,age,address,city,user_name,password) values('%s','%s','%s','%s','%s','%s','%s')" % data)
                                    con.commit()
                                    messagebox.showinfo("Success" , "Registration Successfull" , parent = winsignup)
                                    cur.execute("select user_name,password from userinfo where user_name = '%s'"%(g,))
                                    messagebox.showinfo("YOUR username and password is ",cur.fetchone())
                                    cur.execute("select Patientid from userinfo where user_name = '%s'"%(g,))
                                    messagebox.showinfo("YOUR Patient ID  is ",cur.fetchone())
                                    con.close()
                                    clear()
                                    switch()
                    except Exception as es:
                        messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = winsignup)
                                       

    def switch():
        winsignup.destroy()
    
    def clear():
        first_name.delete(0,END)
        last_name.delete(0,END)
        age.delete(0,END)
        add.delete(0,END)
        city.delete(0,END)
        user_name.delete(0,END)
        password.delete(0,END)
        con_pass.delete(0,END)

#-------------------------------------------------------END Signup FUNCTION --------------------------------------------------

#------------------------------------------------------- Signup Window --------------------------------------------------


    # start Signup Window   

    winsignup = Tk()
    winsignup.title("Signup")
    
    #winsignup.maxsize(width=500 ,  height=600)
    #winsignup.minsize(width=500 ,  height=600)
    #winsignup.configure(bg='lightblue')

    winsignup.geometry('500x600')
    winsignup.configure(bg='lightblue')

    #heading label
    heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold',bg='lightblue')
    heading.place(x=80 , y=60)

    # form data label
    first_name = Label(winsignup, text= "First Name: " , font='Verdana 10 bold',bg='lightblue')
    first_name.place(x=62,y=130)

    last_name = Label(winsignup, text= "Last Name: " , font='Verdana 10 bold',bg='lightblue')
    last_name.place(x=62,y=160)

    age = Label(winsignup, text= "Age: " , font='Verdana 10 bold',bg='lightblue')
    age.place(x=62,y=190)
    
    add = Label(winsignup, text= "Address: " , font='Verdana 10 bold',bg='lightblue')
    add.place(x=62,y=240)
    
    city = Label(winsignup, text= "City: " , font='Verdana 10 bold',bg='lightblue')
    city.place(x=62,y=270)

    user_name = Label(winsignup, text= "Username: " , font='Verdana 10 bold',bg='lightblue')
    user_name.place(x=62,y=320)

    password = Label(winsignup, text= "Password: " , font='Verdana 10 bold',bg='lightblue')
    password.place(x=62,y=350)

    con_pass = Label(winsignup, text= "Confirm Password: " , font='Verdana 10 bold',bg='lightblue')
    con_pass.place(x=62,y=380)

    # Entry Box ------------------------------------------------------------------
    first_name = StringVar()
    last_name = StringVar()
    age = IntVar(winsignup, value='0')
    add = StringVar()
    city= StringVar()
    user_name = StringVar()
    password = StringVar()
    con_pass = StringVar()

    first_name = Entry(winsignup, width=40 , textvariable = first_name)
    first_name.place(x=200 , y=133)


    
    last_name = Entry(winsignup, width=40 , textvariable = last_name)
    last_name.place(x=200 , y=163)

    
    age = Entry(winsignup, width=40, textvariable = age)
    age.place(x=200 , y=193)
    
    add = Entry(winsignup, width=40 , textvariable = add)
    add.place(x=200 , y=243)

    city = Entry(winsignup, width=40,textvariable = city)
    city.place(x=200 , y=273)
    
    user_name = Entry(winsignup, width=40,textvariable = user_name)
    user_name.place(x=200 , y=323)

    
    password = Entry(winsignup, width=40, textvariable = password)
    password.place(x=200 , y=353)

    
    con_pass= Entry(winsignup, width=40 ,show="*" , textvariable = con_pass)
    con_pass.place(x=200 , y=383)


    # button login and clear

    btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action, bg='lightblue')
    btn_signup.place(x=200, y=420)

    btn_login1 = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear,bg='lightblue')
    btn_login1.place(x=280, y=420)

    sign_up_btn = Button(winsignup , text="Switch To Login" ,font='Verdana 10 bold' ,command = switch,bg='lightblue' )
    sign_up_btn.place(x=350 , y =20)


    winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------    


    

#------------------------------------------------------------ Login Window -----------------------------------------

win =Tk()

# app title
win.title("The Royal Marsden Hospital ")



# window size
#screen_width = win.winfo_screenwidth()
#screen_height = win.winfo_screenheight()


# create a frame with screen size
#frame = tk.Frame(win, width=screen_width, height=screen_height,bg = 'lightblue')
#frame.pack()
#win.maxsize(width=1500 ,  height=900)
#win.minsize(width=1500 ,  height=900)

win.geometry('800x500')

img100 = PhotoImage(file='C:/Users/Kamakshi Sarbhai/Desktop/hi1.png')
#img100 = img100.subsample(1,1)

label = Label(win,image=img100)
label.place(x=0,y=0,relwidth=1,relheight=1)

#heading label
h1=Label(win,text="Welcome To The Royal Marsden Hospital ",font = 'Verdana 25 bold',fg='blue')
h1.place(x=70,y=50)

heading = Label(win , text = "Login Page" , font = 'Verdana 15 bold', fg='blue')
heading.place(x=70 , y=100)

username = Label(win, text= "Username :" , font='Verdana 10 bold', fg='blue')
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold', fg='blue')
userpass.place(x=80,y=260)

a=Label(win,text="Designation :",font = 'Verdana 10 bold', fg='blue')
a.place(x=80,y=290)
w=ttk.Combobox(win,values=["Patient","Doctor"])
w.place(x=200, y=290, width=100)
#Desg=Label(win,text="Designation :",font='Verdana 10 bold')
#Desg.place(x=80,y=280)

# Entry Box
#p=StringVar()
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)

#personentry = Entry(win, width=40 , textvariable = p)
#personentry.focus()
#personentry.place(x=200 , y=270)  


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login, bg='lightblue')
btn_login.place(x=200, y=340)
img11 = PhotoImage(file='C:/Users/Kamakshi Sarbhai/Desktop/img11.png')

img11 = img11.subsample(9,9)

btn_login.image = img11
btn_login.config(image=img11)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear, bg='lightblue')
btn_login.place(x=280, y=340)

img3 = PhotoImage(file='C:/Users/Kamakshi Sarbhai/Desktop/img3.png')

img3 = img3.subsample(9,9)

btn_login.image = img3
btn_login.config(image=img3)


# signup button

sign_up_btn = Button(win , text="Switch To Sign up" ,font='Verdana 10 bold' , command = signup, bg='lightblue' )
sign_up_btn.place(x=700 , y =100)



win.mainloop()

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------------------
