from app.models import resources, sandwiches
from app.database import engine


# populations,
def index():
    resources.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
