from flask import Blueprint, jsonify, request
from sarufi.zenopay import make_payment

name = "sarufi_middleware"
sarufi_middleware = Blueprint(name, __name__)

@sarufi_middleware.route("/pay", methods=["POST"])
def sarufi_payment():
    # Get the request data
    data = request.get_json()
    print(data)
    
    res = make_payment(
        customer_email=data["customer_email"],
        buyers_name=data["buyers_name"],
        amount=data["amount"],
        phone_number=data["phone_number"],
    )
    response = jsonify(res)
    return response


@sarufi_middleware.route("/huduma_zilizopo", methods=["POST"])
def huduma_zilizopo():
    # Get the request data
    data = request.get_json()

    print(data)
    
    huduma_zilizopo = [
        {
            "1": "Customized Design",
            "2": "Cut & Fades",
            "3": "Trimming",
            "4": "Haircuts",
        }
    ]

    huduma = {
        "Huduma_zetu": {
            "message": [
                ["Hello, Karibu kwenye huduma zetu"],
                ["Huduma gani kati ya hizi zifuatazo unayo hitaji?"],
            ],
            "type": "interactive",
            "next_state": "username",
            "buttons": huduma_zilizopo,
            "images": [
                {
                    "link": "https://sarufi-media.s3.amazonaws.com/d265fce7-3f73-4a40-b03f-f68ddbee6ebc.jpg",
                    "caption": "welcome to Pizza bot",
                }
            ],
        },
        "choice_confirmation": {
            "1": "confirms",
            "2": "does_not_confirm",
            "fallback_message": [
                "Tafadhari chagua huduma moja wapo kati ya zilizo tajwa"
            ],
        },
        "does_not_confirm": {
            "message": [
                "You are welcome at our pizza service.",
                "",
                "We are always happy to serve  you",
            ],
            "type": "text",
            "next_state": "end",
        },
        "confirms": {
            "message": [
                "Thank you for ordering with us. Your order number is @order_number"
            ],
            "type": "text",
            "next_state": "end",
        },
    }
    return jsonify(huduma)
