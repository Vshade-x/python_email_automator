import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==========================================================
# 1. CONFIGURATION AND CREDENTIALS
# ==========================================================

# NOTE: Use your actual Gmail and the App Password here
RECIPIENTS_FILE = "list_contacts.csv"  # File must have 'Name' and 'Email' columns
SENDER_EMAIL = "your_sending_email@gmail.com"
SENDER_PASSWORD = "YOUR_APP_PASSWORD_HERE"  # IMPORTANT: Use Google App Password (16 chars)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587 # Standard port for TLS encryption

# ==========================================================
# 2. MAIN FUNCTION (With Nested Error Handling)
# ==========================================================
def send_emails():
    print(f"Starting email automation from: {RECIPIENTS_FILE}")

    # Outer TRY block handles file loading and initial connection errors
    try: 
        df = pd.read_csv(RECIPIENTS_FILE)
        print(f"File loaded. {len(df)} recipients found.")

        # Establish secure connection and log in
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=15) as server:
            server.starttls() # Secure the connection with TLS
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Safe connection and login successful.")

            # BUCLE: Iterate through each recipient and send the email
            for index, row in df.iterrows():
                
                # Inner TRY block isolates errors for a single recipient
                try: 
                    recipient_name = row['Name']
                    recipient_email = row['Email']

                    # 1. Build the Message
                    message = MIMEMultipart()
                    message['From'] = SENDER_EMAIL
                    message['To'] = recipient_email
                    message['Subject'] = f"Hello {recipient_name}, This is your automated report Email"
                    
                    # 2. Build the Body (Plain Text)
                    body = f"""
                    Hello {recipient_name},

                    This is a message from the Vshade Automation Team. 
                    Your personalized email for {recipient_email} has been successfully processed.

                    Best regards,
                    Automation Team
                    """
                    message.attach(MIMEText(body, 'plain'))

                    # 3. Send the message
                    server.send_message(message)

                    print(f"✅ Email sent successfully to: {recipient_email}")

                except smtplib.SMTPRecipientsRefused:
                    # Error handling for invalid/fake email addresses
                    print(f"❌ WARNING: Skipping invalid recipient {recipient_email}. Email address rejected by server.")
                    continue  # Continues the loop to the next valid email
                
                except Exception as e:
                    # General error handling for unexpected issues during a single send
                    print(f"❌ WARNING: An error occurred sending to {recipient_email}. Error: {e}")
                    continue  # Continues the loop
                
    except FileNotFoundError:
        print(f"❌ ERROR: The file '{RECIPIENTS_FILE}' was not found.")
        print("Please ensure the CSV file is in the same folder.")
        return
    except smtplib.SMTPAuthenticationError:
        print("❌ AUTHENTICATION ERROR: Login failed.")
        print("Ensure you are using the correct Google App Password (16 characters).")
        return
    except KeyError as ke:
        print(f"❌ COLUMN ERROR: The required column {ke} was not found in the CSV file.")
        print("Please check that your CSV headers are exactly 'Name' and 'Email'.")
    except Exception as e:
        print(f"❌ An unexpected critical error occurred: {e}")
        return

if __name__ == "__main__":
    send_emails()