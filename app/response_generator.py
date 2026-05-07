def generate_response(data, result):

    return f"""
Hi {data['name']},

Thank you for contacting us regarding AI automation.

Based on your requirements, our team would love to discuss solutions for {data['company']}.

Lead Priority: {result['lead_type']}

We will contact you shortly.

Best Regards,
KeaBuilder AI Team
"""