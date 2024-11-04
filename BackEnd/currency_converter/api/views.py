from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def convert_currency(request):
    try:
        from_currency = request.GET.get('from')
        to_currency = request.GET.get('to')
        amount = request.GET.get('amount')

        # Check if the parameters are valid
        if not from_currency or not to_currency or amount is None:
            return Response({"error": "Invalid parameters"}, status=status.HTTP_400_BAD_REQUEST)

        # Convert the 'amount' parameter to a float
        try:
            amount = float(amount)
        except ValueError:
            return Response({"error": "Amount must be a number"}, status=status.HTTP_400_BAD_REQUEST)

        # Mock exchange rate for testing
        exchange_rate = 0.85  # Example rate for USD to EUR
        converted_amount = amount * exchange_rate

        return Response({"convertedAmount": converted_amount})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
