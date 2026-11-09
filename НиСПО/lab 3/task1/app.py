from flask import Flask
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource

# Настройка провайдера трассировки
resource = Resource(attributes={"service.name": "my-flask-app"})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route('/')
def hello():
    return "Hello, OpenTelemetry!"

@app.route('/heavy')
def heavy():
    time.sleep(1)
    return "Heavy request finished!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)