

def make_payment(customer_email, buyers_name, amount, phone_number):
    import requests
    import uuid

    # URL of the API endpoint
    url = "https://api.zeno.africa"
    # creating automatic order id
    order_id = str(uuid.uuid4())
    
    # Data to send for creating the order
    order_data = {
        'create_order': order_id,
        'buyer_email': customer_email,
        'buyer_name': buyers_name,
        'buyer_phone': phone_number,
        'amount': amount,
        'account_id': "zp82538",
        'api_key': "",
        'secret_key': ""
    }

    try:
        # Send POST request to create the order
        response = requests.post(url, data=order_data)
        
        # Print the response
        print(response)
        return response.json()
        

    except requests.RequestException as e:
        # Log errors to a file
        with open('error_log.txt', 'a') as log_file:
            log_file.write(f"Error: {e}\n")