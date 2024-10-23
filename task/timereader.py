class TimeReader:
    def __init__(self, hr, mn):
        self.hours = hr
        self.minutes = mn

    def daytime(self) -> str:
        return 'Time before dinner' if self.hours < 12 else 'Time after dinner'

    def __str__(self) -> str:
        if self.hours > 12:
            return f'{self.hours - 12}:{self.minutes:02} PM'
        elif self.hours == 12:
            return f'{self.hours}:{self.minutes:02} PM'
        elif self.hours == 0:
            return f'12:{self.minutes:02} AM'
        return f'{self.hours}:{self.minutes:02} AM'

    @staticmethod
    def read(str) -> 'TimeReader':
        try:
            hr, mn = map(int, str.split())
            if hr < 0 or hr > 23 or mn < 0 or mn > 59:
                return None
            return TimeReader(hr, mn)
        except:
            return None
