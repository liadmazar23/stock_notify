from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        stock_symbol = request.form['stock_symbol']
        time_checked = 'checked' in request.form
        # Fetch stock data
        stock_data = yf.Ticker(stock_symbol)
        stock_info = stock_data.info
        return render_template('result.html', email=email, time_checked=time_checked, stock_info=stock_info)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
