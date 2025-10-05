from pydantic import BaseModel
from report import Report
from typing import List, Optional


class SituationReporter(BaseModel):
    topic: str
    # detail_amount: float
    # account_list: List[str]
    # analytical_lens: str
    report: Optional[Report] = None

    def generate_report(self):
        report = Report(self.topic)
        self.report = report

    def print_report(self):
        if self.report:
            self.report.print()
        else:
            print("No report to generate")
