import unittest
from unittest.mock import patch

# The payment gateway class that interacts with an external payment system
class PaymentGateway:
    def process_payment(self, amount):
        # Simulate calling an external payment API
        return f"Processed payment of {amount}"

# The payment processor that uses the payment gateway
class PaymentProcessor:
    def __init__(self, gateway):
        self.gateway = gateway

    def make_payment(self, amount):
        if amount <= 0:
            return "Invalid amount"
        # Call the payment gateway to process payment
        return self.gateway.process_payment(amount)

# Test the PaymentProcessor class using a mock PaymentGateway
class TestPaymentProcessor(unittest.TestCase):

    @patch('__main__.PaymentGateway')
    def test_successful_payment(self, MockPaymentGateway):
        print("\nRunning test_successful_payment...")
        # Create a mock gateway instance
        mock_gateway = MockPaymentGateway()
        mock_gateway.process_payment.return_value = "Processed payment of 100"

        # Inject the mock gateway into the PaymentProcessor
        processor = PaymentProcessor(mock_gateway)

        # Test the payment processing logic
        result = processor.make_payment(100)

        # Verify the result
        self.assertEqual(result, "Processed payment of 100")
        mock_gateway.process_payment.assert_called_once_with(100)

        print(f"Expected Result: 'Processed payment of 100', Actual Result: {result}")

    @patch('__main__.PaymentGateway')
    def test_invalid_payment(self, MockPaymentGateway):
        print("\nRunning test_invalid_payment...")
        # Create a mock gateway
        mock_gateway = MockPaymentGateway()

        # Inject the mock gateway into the processor
        processor = PaymentProcessor(mock_gateway)

        # Test invalid amount case
        result = processor.make_payment(-1)

        # Check that the gateway wasn't called
        self.assertEqual(result, "Invalid amount")
        mock_gateway.process_payment.assert_not_called()

        print(f"Expected Result: 'Invalid amount', Actual Result: {result}")

if __name__ == '__main__':
    unittest.main()
