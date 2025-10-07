from pydantic import BaseModel
from pydantic_ai import Agent
from report import Report
from typing import List, Optional


class SituationReporter(BaseModel):
    topic: str
    # detail_amount: float
    # account_list: List[str]
    # analytical_lens: str
    report: Optional[Report] = None
    agent: Agent

    def __init__(self, topic: str):
        super().__init__()  # Initialize BaseModel
        self.agent = Agent(
            "openai:gpt-4.1-mini",
            instructions=f"You are a situation reporter on {topic}.",
        )

    def generate(self):
        report = Report(self.topic)
        self.report = report

    def print(self):
        if self.report:
            self.report.print()
        else:
            print("No report to generate")
