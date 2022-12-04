# app.py - application layer
import logging

from flask import Flask, render_template, request

from stock_alert_service import ServiceStockAlert

logger = logging.getLogger('stock_alert')
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("portfolio.html")


@app.route('/portfolio.html', methods=['GET', 'POST'])
def analysis():
    logger.info("*** Stock Alert *** ")

    if request.method == "POST":
        stock_select = request.form.get("stock", None)
        threshold_select = float(request.form.get("threshold", None))
        investment_select = float(request.form.get("investment", None))

        df = ServiceStockAlert().stock_analysis(stock_select, threshold_select, investment_select)

        buy_total = df['Buy cost'].sum()
        sell_total = df['Sell cost'].sum()
        balance = round((sell_total - buy_total))

        return render_template("portfolio.html", table_html=df.to_html(classes='table table-striped'),
                               stock=stock_select, threshold=threshold_select, balance=balance)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
