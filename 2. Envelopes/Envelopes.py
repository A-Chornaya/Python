class Envelope:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare_envelopes(self, env):
        if (((self.a <= env.a) and (self.b <= env.b))
                or ((self.a <= env.b) and (self.b <= env.a))):
            return True
        else:
            return False


def restart_program():
    answer = input('Do you want to continue? (enter "y" or "yes" if want):')
    if answer.lower() == 'y' or 'yes' == answer.lower():
        return True
    else:
        return False


while True:
    print('')
    print('=======Compare envelopes=======')
    try:
        a = float(input('Enter side a of Envelope 1:'))
        b = float(input('Enter side b of Envelope 1:'))
        c = float(input('Enter side a of Envelope 2:'))
        d = float(input('Enter side b of Envelope 2:'))
        if (a <= 0 or b <= 0 or c <= 0 or d <= 0):
            raise ValueError
    except ValueError:
        print('Error of value types. Sides of the envelopes must be '
              'positive numbers')
        if restart_program():
            continue
        else:
            break
    else:
        envelope1 = Envelope(a, b)
        envelope2 = Envelope(c, d)

        if envelope1.compare_envelopes(envelope2):
            print('Envelope 1 placed in Envelope 2')

        if envelope2.compare_envelopes(envelope1):
            print('Envelope 2 placed in Envelope 1')

        if restart_program():
            continue
        else:
            break
