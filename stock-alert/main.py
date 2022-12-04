from stock_alert_service import run_user_portfolio_analysis
from send_html_email_service import send_email
from prettytable import PrettyTable


def main():
    name = "tomergur@gmail.com"
    portfolio_analysis = run_user_portfolio_analysis(name)
    send_email(name, portfolio_analysis)

if __name__ == "__main__":
    main()
