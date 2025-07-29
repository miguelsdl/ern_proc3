import isodate


def iso8601_to_mysql_time(iso_duration_str):
    duration = isodate.parse_duration(iso_duration_str)
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"