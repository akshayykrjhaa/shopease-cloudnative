from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "<h1>ShopEase App - Running in Docker</h1><p>Automated deployment with CI/CD and monitoring.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
