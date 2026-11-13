"""
Service Package
"""
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
app.config.from_object("config")

# Initialize Talisman with CSP settings
csp = {
    'default-src': '\'self\'',
    'object-src': '\'none\''
}
talisman = Talisman(
    app,
    content_security_policy=csp,
    force_https=False
)

# Initialize CORS
CORS(app)

from service import routes, models
from service.common import log_handlers
log_handlers.init_app(app)

app.logger.info(70 * "*")
app.logger.info("  C U S T O M E R   A C C O U N T S   S E R V I C E  ".center(70, "*"))
app.logger.info(70 * "*")
