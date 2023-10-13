from io import BytesIO
from celery import shared_task
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.core.mail import EmailMessage
from orders.models import Order


@shared_task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    template = get_template('orders/order/pdf.html')
    subject = f'The best phone shop - Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@the_best_phone_shop.com',
                         [order.email])
    html = template.render({'order': order})
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    email.attach(f'order_{order.id}.pdf',
                 result.getvalue(),
                 'application/pdf')
    email.send()
