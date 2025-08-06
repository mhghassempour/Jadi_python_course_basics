dict_of_donations = {
    'jadi' : 20, 
    'sara' : 800, 
    'far' : 12,
    'hasan' : 9
    }


def donation_analysis(donations):
    count = 0
    total = 0 
    max_donater = ''
    max_donate_amount = -1
    
    for name, amount in donations.items():
        total += amount
        count += 1 
        if amount > max_donate_amount:
            max_donate_amount = amount
            max_donater = name 
    
    avg = total / count
    
    return avg, total, max_donater, max_donate_amount, count


avg, total, max_donater, max_donate_amount, count= donation_analysis(dict_of_donations) 
print(f'a toatal of {count} people donated')
print(f'total donation: {total}$')
print(f'average donation: {avg}$')
print(f'biggest donater was "{max_donater.upper()}" for donating {max_donate_amount}$')