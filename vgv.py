def make_amount(total_amount,available_1,available_5):
    five_needed=4
    one_needed=1
    if(available_5>five_needed and available_1>one_needed):
        five_needed=total_amount//5
        one_needed=total_amount%5
        print("no.of Five needed:", five_needed)
        print("no.of One needed:", one_needed)
    else:
        print(-1)
    make_amount(21,20,10)
