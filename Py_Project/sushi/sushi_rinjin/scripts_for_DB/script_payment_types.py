import django
#django.setup()

from sushi_rinjin.models.payment_method import PaymentMethod

pay1 = PaymentMethod(pay_method='cash')
pay2 = PaymentMethod(pay_method='credit card')
pay3 = PaymentMethod(pay_method='check')

pay1.save()
pay2.save()
pay3.save()
