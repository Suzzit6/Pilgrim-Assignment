import pandas as pd
import smtplib
from email.message import EmailMessage
import streamlit as st
import os
import io
import tempfile

st.set_page_config(
    page_title="Sales Data Filter",
    page_icon="📊",
    layout="wide"
)

st.title("Pilgrim Email Automation Assignment")
st.markdown("---")

#  send email
def send_email(receiver_email, subject, body, attachment_path):
    try:
        sender_email = 'ferryellaaa3@gmail.com'
        sender_password = os.getenv('EMAIL_PASSWORD')

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(body)

        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            return True, f"Email sent to {receiver_email} with filtered sales data!"
    except Exception as e:
        return False, f"Error sending email: {str(e)}"

#create sample data
def create_sample_data():
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=20),
        'Product': ['Product A', 'Product B', 'Product C', 'Product D'] * 5,
        'Quantity': [10, 5, 8, 12, 15, 7, 9, 11, 20, 6, 8, 13, 9, 4, 7, 10, 12, 8, 5, 11],
        'Sales': [1500, 800, 2000, 950, 3000, 750, 1200, 1800, 2500, 500, 
                 1100, 1600, 900, 600, 2200, 1700, 1300, 850, 750, 1900]
    }
    return pd.DataFrame(data)

st.sidebar.header("Data Source")

data_option = st.sidebar.radio(
    "Choose data source:",
    ["Upload Excel file", "Use sample data"]
)

df = None
if data_option == "Upload Excel file":
    uploaded_file = st.sidebar.file_uploader("Upload your Excel file", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            if 'Sales' not in df.columns:
                st.sidebar.error("❌ The uploaded file doesn't have a 'Sales' column. Please upload a file with sales data.")
                df = None
        except Exception as e:
            st.sidebar.error(f"Error reading file: {str(e)}")
            df = None
else:
    df = create_sample_data()
    st.sidebar.success("✅ Using sample sales data")

if df is not None:
    st.subheader("Original Data")
    st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Filter Settings")
    
    col1, col2 = st.columns(2)
    with col1:
        min_sales = int(df['Sales'].min())
        max_sales = int(df['Sales'].max())
        default_value = min(1000, max_sales) if min_sales < 1000 else min_sales
        
        sales_threshold = st.slider(
            "Filter sales greater than:",
            min_value=min_sales,
            max_value=max_sales,
            value=default_value,
            step=100
        )
    
    with col2:
        output_filename = st.text_input("Output filename:", "filtered_sales.xlsx")
        if not output_filename.endswith('.xlsx'):
            output_filename += '.xlsx'
    
    filtered_df = df[df['Sales'] > sales_threshold]
    
    st.subheader(f"Filtered Data (Sales > {sales_threshold})")
    if filtered_df.empty:
        st.warning("No data matches your filter criteria. Try lowering the sales threshold.")
    else:
        st.dataframe(filtered_df, use_container_width=True)
        st.success(f"✅ {len(filtered_df)} rows match your filter criteria")
        
        temp_dir = tempfile.gettempdir()
        output_path = os.path.join(temp_dir, output_filename)
        filtered_df.to_excel(output_path, index=False)
        
        st.success(f"✅ Filtered data saved as '{output_filename}'")
        
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label="Download Filtered Data",
                data=file,
                file_name=output_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        
        st.markdown("---")
        st.subheader("Email the Filtered Data")
        
        with st.form(key='email_form'):
            receiver_email = st.text_input("Recipient Email Address:", "mishrasujit409@gmail.com")
            email_subject = st.text_input("Email Subject:", f"Filtered Sales Data (>{sales_threshold})")
            email_body = st.text_area("Email Body:", "Please find the attached filtered sales data as requested.")
            
            submit_button = st.form_submit_button(label="Send Email")
            
            if submit_button:
                with st.spinner("Sending email..."):
                    success, message = send_email(receiver_email, email_subject, email_body, output_path)
                    
                    if success:
                        st.success(message)
                    else:
                        st.error(message)
else:
    if data_option == "Upload Excel file":
        st.info("👈 Please upload an Excel file with sales data using the sidebar")
    else:
        st.error("There was an error loading the sample data. Please try uploading your own file.")

st.markdown("---")
st.caption("Sales Data Filter and Email Automation | Internship Assignment")