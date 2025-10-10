import pandas as pd 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Configuration Variables
RECIPIENTS_FILE = "list_contacts.csv" 
SENDER_EMAIL = "vshade.automation@gmail.com"
SENDER_PASSWORD = "App Pasword" # IMPORTANT: Use an App Password for Gmail
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587

# 2. Main Function
def send_emails():
    print(f"Starting email automation from: {RECIPIENTS_FILE}")

    # Bloque TRY que envuelve todo el código que puede fallar (carga y conexión)
    try: 
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(RECIPIENTS_FILE)
        print(f"File loaded. {len(df)} recipients found.")

        # --- MODULE 2: Connection and Sending ---
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=15) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Safe connection and login successful.")

            for index, row in df.iterrows():
                recipient_name = row['Name']
                recipient_email = row['Email']

                message = MIMEMultipart()
                message['From'] = SENDER_EMAIL
                message['To'] = recipient_email

                message['Subject'] = f"Hello {recipient_name}, This is your automated report Email"
                
                body = f"""
                Hello {recipient_name},

                This is a message of test automation. Confirming that your email
                {recipient_email} is ready to receive the report.

                Best regards,
                Automation Team
                """

                message.attach(MIMEText(body, 'plain'))

                server.send_message(message)

                print(f"Email sent successfully to: {recipient_email}")
                
    except FileNotFoundError:
        print(f"❌ ERROR: The file '{RECIPIENTS_FILE}' was not found.")
        print("Please ensure the CSV file is in the same folder.")
        return
    except smtplib.SMTPAuthenticationError:
        # MENSAJE DE ERROR LIMPIO Y UNIVERSAL
        print("❌ ERROR DE AUTENTICACIÓN: Authentication failed.")
        print("Ensure you are using the correct App Password for your service (e.g., Gmail).")
        return
    except KeyError as ke:
        print(f"❌ ERROR DE COLUMNA: The required column ({ke}) was not found in the CSV file.")
        print("Please check that the column headers in your CSV are exactly 'Name' and 'Email'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

if __name__ == "__main__":
    send_emails()