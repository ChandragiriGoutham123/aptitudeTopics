
value_to_find = input("select one among below to find:\n""1.Banker Discount\n""2.Bankers Gain\n""3.Present Worth\n"
                      "4.True Discount\n""5.Time\n""6.Rate\n""7.sum :")
if value_to_find == "1":
    print("Select what are inputs given from below:")
    inputs = input("1.inputs = Amount,True Discount\n""2.inputs = Present Worth,True discount\n"
                   "3.inputs = Time,Rate,Bankers Gain:")
    if inputs == "1":
        import when_true_discount_present_worth_or_amount_given

        print(when_true_discount_present_worth_or_amount_given.TdPwOrA)
    elif inputs == "2":
        import when_true_discount_present_worth_or_amount_given

        print(when_true_discount_present_worth_or_amount_given.TdPwOrA)
    elif inputs == "3":
        import when_time_rate_banker_gain_or_banker_discount_given

        print(when_time_rate_banker_gain_or_banker_discount_given.TrBgOrBd)

elif value_to_find == "2":
    print("Select what are inputs given from below:")
    inputs = input("1.inputs = present worth , True Discount :")
    if inputs == "1":
        import when_true_discount_present_worth_or_amount_given

        print(when_true_discount_present_worth_or_amount_given.TdPwOrA)

elif value_to_find == "3":
    print("Select what are inputs given from below:")
    inputs = input("1.inputs = Time,Rate,Bankers Gain:")
    if inputs == "1":
        import when_time_rate_banker_gain_or_banker_discount_given

        print(when_time_rate_banker_gain_or_banker_discount_given.TrBgOrBd)

elif value_to_find == "4":
    print("Select what are inputs given from below:")
    inputs = input("1.inputs = Time,Rate,Bankers Gain\n""2.inputs = Time,Rate,Bankers Discount\n"
                   "3.inputs = Present Worth,Bankers Gain:")
    if inputs == "1":
        import when_time_rate_banker_gain_or_banker_discount_given

        print(when_time_rate_banker_gain_or_banker_discount_given.TrBgOrBd)
    elif inputs == "2":
        import when_time_rate_banker_gain_or_banker_discount_given

        print(when_time_rate_banker_gain_or_banker_discount_given.TrBgOrBd)
    elif inputs == "3":
        import when_present_worth_and_banker_gain_given

        print(when_present_worth_and_banker_gain_given.PwBg)

elif value_to_find == "5":
    print("Select what are inputs given from below:")
    inputs = input("1.inputs = Banker Discount,True Discount,Same Time,Same Rate: ")
    if inputs == "1":
        import when_amount_time_rate_given

        print(when_amount_time_rate_given.AmountTimeRate)
elif value_to_find == "6":
    print("Select what are inputs given from below:")
    inputs = input("1.inputs = Bankers Discount,Time for Bankers discount,True Discount,Time for True Discount\n"
                   "2.inputs = Fraction of Banker Discount and True Discount,Time\n"
                   "3.inputs = Fraction of Banker Gain and Banker Discount,Time: ")
    if inputs == "1":
        import when_amount_time_rate_given

        print(when_amount_time_rate_given.AmountTimeRate)
    elif inputs == "2":
        import other_methods

        print(other_methods.OtherMethods)
    elif inputs == "3":
        import other_methods

        print(other_methods.OtherMethods)

elif value_to_find == "7":
    print("Select what are inputs given from below:")
    inputs = input("1.inputs = True Discount,Bankers Discount,Same Sum: ")
    if inputs == "1":
        import when_banker_discount_true_discount_given

        print(when_banker_discount_true_discount_given.BdTd)
