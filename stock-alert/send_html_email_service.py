import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from prettytable import PrettyTable, MSWORD_FRIENDLY


def build_stock_html_table(portfolio_analysis):
    tabular_fields = ["Stock symbol", "Buy price", "quantinity", "PNL"]
    tabular_table = PrettyTable()
    tabular_table.field_names = tabular_fields
    for stock_dic in portfolio_analysis:
        tabular_table.add_row(
            [stock_dic["stock symbol"], stock_dic["buy price"], stock_dic["quantinity"], stock_dic["PNL"]])
    tabular_table.set_style(MSWORD_FRIENDLY)
    return tabular_table.get_html_string()


def send_email(user_name, portfolio_analysis):
    gmail_user = 'tomergur@gmail.com'
    gmail_password = 'hwlhbvkmnsdgtygs'

    message = MIMEMultipart('alternative')
    message['subject'] = 'Stock market portfolio daily info'
    message['To'] = user_name
    message['From'] = gmail_user
    message.preamble = """
    This message is in HTML only, which your mail reader doesn't seem to support!
    """

    html_content = """\
        <html>
            <head>
                <meta content="Tomer Gur" name="author">
                <title>Stock Portfolio Tracker</title>
                <style>
                    table, th, td {
                        border: 1px solid black;
                        border-collapse: collapse;
                    }
                    th, td {
                        padding: 5px;
                        text-align: center;
                    }
                </style>
            </head>
        <body >
        <strong>Welcome to Stock Portfolio Tracker</strong><br>
           Here is you portfolio details:<br>
           %s
        </body>
        </html>
        """ % (build_stock_html_table(portfolio_analysis))
    # Record the MIME type text/html.

    html_body = MIMEText(html_content, 'html')
    message.attach(html_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, user_name, message.as_string())
        server.close()

        print('Email sent!')
    except Exception as ex:
        print("Something went wrong….", ex)


class SendEmail:
    pass
