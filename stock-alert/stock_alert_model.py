import csv


def load_user_portfolio_from_csv(name):
    with open('data\portfolio.csv', 'r') as f:
        portfolio = list(csv.DictReader(f))
        user_portfolio = [row for row in portfolio if row['name'] == name]
    print(f"user portfolio for  {name} is {user_portfolio} ")
    return user_portfolio


def load_user_portfolio_from_dynamo_db(name):
    raise Exception("Function not implemented yet")


class UserProtfolioModel:
    pass
