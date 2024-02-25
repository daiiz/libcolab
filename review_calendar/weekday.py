

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


# find_nth_weekday_of_specific_year_extended
def find_nth_weekday_of_specific_year(y, m, n, k):
    """
    Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
    If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
    This function extends the capability to handle edge cases where the nth weekday might not be present,
    by providing the closest previous weekday in such cases.

    Parameters:
    - y (int): The year for which the date is to be calculated.
    - m (int): The month for which the date is to be calculated, where January is 1 and December is 12.
    - n (int): The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
    - k (int): The weekday, where Monday is 0 and Sunday is 6.

    Returns:
    - datetime.datetime: The calculated date of the nth occurrence of the weekday in the given month and year.
      If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    """

    first_day_of_month = datetime(y, m, 1)
    day_difference = (k - first_day_of_month.weekday() + 7) % 7
    first_k_weekday_of_month = first_day_of_month + timedelta(days=day_difference)
    nth_k_weekday_of_month = first_k_weekday_of_month + timedelta(weeks=n-1)

    # その月の最終日を計算するために、次の月の第1日を取得し、1日引く
    if m == 12:
        next_month_first_day = datetime(y + 1, 1, 1)
    else:
        next_month_first_day = datetime(y, m + 1, 1)
    last_day_of_month = next_month_first_day - timedelta(days=1)

    # その月を超える場合は、その月の最終日を返す
    if nth_k_weekday_of_month > last_day_of_month:
        # その月の最終k曜日を見つけるために逆算する
        last_k_weekday_of_month = last_day_of_month - timedelta(days=(last_day_of_month.weekday() - k + 7) % 7)
        return last_k_weekday_of_month

    return nth_k_weekday_of_month


def find_nth_weekday_delta_months_ago(delta_m, n, k, reference_date=None):
    """
    Calculates the date of the nth occurrence of a specific weekday (k) in the month delta_m months before a reference date.
    If the nth occurrence does not exist within that month, it returns the last occurrence of that weekday in the month.
    This function handles cases where the nth weekday might not be present, by providing the closest previous weekday in such cases.
    If no reference date is provided, the current date is used as the reference.

    Parameters:
    - delta_m (int): The number of months before the reference date for which to calculate the weekday's occurrence.
    - n (int): The nth occurrence of the weekday to be calculated. For example, 1 for the first occurrence, 2 for the second, etc.
    - k (int): The weekday, where Monday is 0 and Sunday is 6.
    - reference_date (datetime.datetime, optional): The reference date from which to count back delta_m months. If not provided, today's date is used.

    Returns:
    - datetime.datetime: The calculated date of the nth occurrence of the weekday in the specified month.
      If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    """

    # 参照日が指定されていない場合は、今日の日付を使用
    if reference_date is None:
        reference_date = datetime.now()

    # delta_mヶ月前の日付を計算
    target_date = reference_date - relativedelta(months=delta_m)
    y, m = target_date.year, target_date.month

    # 指定された年月の第n週のk曜日を計算
    nth_k_weekday = find_nth_weekday_of_specific_year(y, m, n, k)
    return nth_k_weekday


def get_past_k_weekdays_list(range_m, k, reference_date=None):
    """
    Generates a list of dates representing the occurrences of a specific weekday (k) over the past range_m months from a reference date.
    This function finds all occurrences of the specified weekday in each month within the range, including cases where the month might not have a fifth occurrence.
    The function returns a list of dates without future dates or duplicates, sorted in descending order.

    Parameters:
    - rangeM (int): The range in months before the reference date from which to generate the list of weekdays.
    - k (int): The weekday for which to generate the list, where Monday is 0 and Sunday is 6.
    - reference_date (datetime.datetime, optional): The reference date from which to calculate the past range. If not provided, today's date is used.

    Returns:
    - list of datetime.datetime: A list of dates for the specified weekday, covering the past range_m months from the reference date,
      excluding future dates and duplicates, sorted in descending order. Each date represents an occurrence of the specified weekday within the range.
    """

    if reference_date is None:
        reference_date = datetime.now()

    k_weekdays_set = set()

    for month_delta in range(range_m):
        target_date = reference_date - relativedelta(months=month_delta)
        y, m = target_date.year, target_date.month
        for week_n in range(1, 6):
            nth_k_weekday = find_nth_weekday_of_specific_year(y, m, week_n, k)
            if nth_k_weekday is not None and nth_k_weekday <= reference_date:
                k_weekdays_set.add(nth_k_weekday)

    k_weekdays_list = sorted(list(k_weekdays_set), reverse=True)
    return k_weekdays_list
