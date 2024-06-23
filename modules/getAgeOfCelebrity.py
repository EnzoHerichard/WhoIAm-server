def get_age_of_celebrity(birth):
    import datetime
    birth = datetime.datetime.strptime(birth, '%Y-%m-%d')
    today = datetime.datetime.now()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    print(age)
    return age