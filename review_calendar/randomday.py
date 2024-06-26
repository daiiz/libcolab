# Note: This code was generated by Gemini-1.5-pro
# https://aistudio.google.com/app/prompts/1k5rNP_BUrwY0vZzkj2cMcGMzNs9uo5yG
import datetime
import random

def get_random_date_between(start_date, end_date=None):
    """開始日と終了日の間のランダムな日付を "YYYY-M-D" 形式で返す。

    Args:
        start_date: str。開始日。"YYYY-M-D" 形式。
        end_date: str。終了日。"YYYY-M-D" 形式。デフォルトは昨日。

    Returns:
        str。開始日と終了日の間のランダムな日付。"YYYY-M-D" 形式。
    """

    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    if end_date is None:
        end_date = datetime.date.today() - datetime.timedelta(days=1)
    else:
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    time_between_dates = (end_date - start_date).days
    random_days = random.randrange(time_between_dates)
    random_date = start_date + datetime.timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")
