from datetime import datetime


def get_today():
    return datetime.now()


def get_today_y_m_n_k(today = datetime.now()):
    y = today.year
    m = today.month
    k = today.weekday()  # 月曜日が0、日曜日が6

    # 月の第1日と今日の日付の差を計算し、週数を求める
    first_day_of_month = datetime(today.year, today.month, 1)
    days_since_first_day = (today - first_day_of_month).days
    n = days_since_first_day // 7 + 1  # その月の第n週

    return y, m, n, k
