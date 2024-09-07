import requests
import uuid
from config import ZENOPAY_ACCOUNT_ID, ZENOPAY_API_KEY, ZENOPAY_API_SECRET

# URL of the API endpoint
url = "https://api.zeno.africa"

def make_payment(customer_email, buyers_name, amount, phone_number):
    
    # creating automatic order id
    order_id = str(uuid.uuid4())
    
    # Data to send for creating the order
    order_data = {
        'create_order': order_id,
        'buyer_email': customer_email,
        'buyer_name': buyers_name,
        'buyer_phone': phone_number,
        'amount': amount,
        'account_id': ZENOPAY_ACCOUNT_ID,
        'api_key': ZENOPAY_API_KEY,
        'secret_key': ZENOPAY_API_SECRET
    }

    try:
        # Send POST request to create the order
        response = requests.post(url, data=order_data)
        
        # Print the response
        print(response.text)

    except requests.RequestException as e:
        # Log errors to a file
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f"Error: {e}\n")