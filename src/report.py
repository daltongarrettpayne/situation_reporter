import datetime
from pydantic import BaseModel
from typing import Optional


class Report(BaseModel):
    llm_output: Optional[str] = None
    date_generated: Optional[datetime.datetime] = None

    # HELP: how to make a contructur, takes in a passed value "topic", calls generate(self, topic)
    def __init__(self, topic: str):
        super().__init__()  # Initialize BaseModel
        self.generate(topic)  # Call generate with the topic

    def generate(self, topic):
        self.llm_output = f"Things are going well in {topic}"
        self.date_generated = datetime.datetime.now()

    def print(self):
        print("This is the report:")
        print(self.llm_output)
        print(self.date_generated)
