# Pilgrim Assignment - Sales Data Filter and Email Automation

## Live Demo

Try the application here: [Sales Data Filter App](https://pilgrim-assignment-kv7shvbemcgkrykpjvfxtf.streamlit.app/)

## Description

This Streamlit application allows users to filter sales data based on a threshold value and send the filtered results via email. It's designed to demonstrate data processing, filtering, and email automation capabilities.

## Features

- **Data Source Options**: Upload your own Excel file or use sample data
- **Interactive Filtering**: Set a sales threshold using a dynamic slider
- **Data Validation**: Ensures uploaded files contain required 'Sales' column
- **Data Export**: Download filtered results as Excel file
- **Email Automation**: Send filtered data directly via email

## Screenshots

![image](https://github.com/user-attachments/assets/38d7fd3e-1837-4525-ae74-17ab29d248c2)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pilgrim-assignment.git
   cd pilgrim-assignment
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

For the email functionality to work, you need to set up an environment variable for your email password:

1. Create a .env file in the project root with the following content:
   ```
   EMAIL_PASSWORD=your_app_password_here
   ```

   **Note**: For Gmail, you'll need to use an "App Password" rather than your regular account password. You can generate one in your Google Account settings under Security > App Passwords.

2. Install the python-dotenv package if needed:
   ```bash
   pip install python-dotenv
   ```

## Running the Application

1. Start the Streamlit server:
   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

## Usage Guide

1. **Select Data Source**:
   - Choose to upload your own Excel file or use the provided sample data
   - If uploading, ensure your file has a 'Sales' column

2. **Filter Data**:
   - Use the slider to set a minimum sales threshold
   - The app will display records with sales values above this threshold

3. **Save and Download**:
   - Filtered data is automatically saved as an Excel file
   - Click the "Download Filtered Data" button to save to your computer

4. **Email Results**:
   - Enter recipient email address
   - Customize subject and body text
   - Click "Send Email" to deliver the filtered data

## Requirements

- Python 3.7+
- pandas
- streamlit
- openpyxl
- smtplib (standard library)
- email (standard library)

A complete list of dependencies is available in the `requirements.txt` file.

## Project Structure

```
pilgrim-assignment/
├── main.py                # Main application file
├── README.md              # This documentation
├── requirements.txt       # Package dependencies
└── .env                   # Environment variables (create this file)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Similar code found with 1 license type
