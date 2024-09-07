from flask import Blueprint, jsonify, request
from sarufi.zenopay import make_payment

name = "sarufi_middleware"
sarufi_middleware = Blueprint(name, __name__)


@sarufi_middleware.route("/", methods=["POST"])
def sarufi_payment_middleware():
    # Get the request data
    data = request.get_json()
    print(data)

    # making actuall payment with zenopay
    make_payment(
        data["customer_email"],
        data["buyers_name"],
        data["amount"],
        data["phone_number"],
    )
    return jsonify({"message": "Payment successful!"})
