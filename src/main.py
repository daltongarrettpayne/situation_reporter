from pydantic import BaseModel
from situation_reporter import SituationReporter


def main():
    topic = "Collide.ai"
    # account_list = ["Collin"]
    # analytical_lens: str = "Strategic"
    updater = SituationReporter(
        topic=topic,
        # detail_amount=0.1,
        # account_list=account_list,
        # analytical_lens=analytical_lens,
    )

    updater.generate_report()
    updater.print_report()


if __name__ == "__main__":
    main()
