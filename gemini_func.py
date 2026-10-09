from mobile_shop import *
from inventory_search import search_by_budget
def ask_gemini(question):
    if client is None:
        return "Gemini API key is not configured."

    inventory = str(mobiles)

    prompt = f"""
You are an AI assistant for a mobile phone shop.

Available mobile inventory:
{inventory}

Customer question:
{question}

Instructions:
- Recommend only phones available in the inventory.
- Consider price, RAM, storage, rating and stock.
- Do not invent specifications.
- Give a simple explanation.
- Use Indian Rupees.

Answer the customer.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text


def ai_recommendation(budget, usage):
    available = search_by_budget(budget)

    if not available:
        return "No mobile available within this budget."

    prompt = f"""
You are a mobile phone expert.

Customer budget:
₹{budget}

Customer usage:
{usage}

Available phones:
{available}

Select the best phone.

Explain:
1. Recommended phone
2. Why it is suitable
3. Alternative phone

Use only the supplied inventory.
"""

    if client is None:
        return "Gemini API key is not configured."

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text

def compare_mobiles(phone1, phone2):
    mobile1 = None
    mobile2 = None

    for mobile in mobiles:
        name = (
            mobile["brand"] + " " + mobile["model"]
        ).lower()

        if name == phone1.lower():
            mobile1 = mobile

        if name == phone2.lower():
            mobile2 = mobile

    if mobile1 is None:
        return "First mobile not found."

    if mobile2 is None:
        return "Second mobile not found."

    if client is None:
        return "Gemini API key is not configured."

    prompt = f"""
Compare these two mobile phones.

PHONE 1:
{mobile1}

PHONE 2:
{mobile2}

Compare:
- Price
- RAM
- Storage
- Rating
- Stock
- Value for money

Give a final recommendation.
Do not invent specifications.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text