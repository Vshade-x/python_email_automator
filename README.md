# PYTHON EMAIL AUTOMATOR | ERROR-PROOF BULK SENDER

### 🎯 Project Overview

A robust, secure Python tool designed to automate personalized email campaigns. This script eliminates costly monthly subscription fees and ensures high deliverability with advanced error handling.

### ✨ Key Features & Robustness

* **Core Function:** Reads contact data (Name, Email) from a CSV, creates unique messages for each recipient, and sends them via a secure SMTP connection.
* **Error-Proof Sending:** Includes advanced **Try/Except logic** to handle individual email recipient failures (e.g., fake or rejected addresses). **The script will not crash** if one address is bad; it skips the faulty email and continues the campaign.
* **Full Personalization:** Custom fields are integrated into the subject and body to make every email unique.
* **Security:** Requires an **App Password** and uses **TLS/SSL** protocols for safe login, avoiding exposure of your main password.
* **Delivery:** Includes a **1-Click Execution File (.bat)** for easy use on Windows.

### 🚀 Execution and Usage

**1. Requirements:** Python (3.x) and required libraries: `pip install pandas`
**2. Setup:** Ensure your email account has **Two-Factor Authentication (2FA)** enabled and an **App Password** generated.
**3. Data Input:** Place your contact list file, **`list_contacts.csv`**, in the project root folder. (Headers must be: `Name, Email`).
**4. Execution:** Simply **double-click the `ejecutar_emails.bat` file** to run the campaign.
**5. Output:** The terminal provides a log of all successful and skipped emails.
