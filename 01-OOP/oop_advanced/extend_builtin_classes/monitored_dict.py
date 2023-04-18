from datetime import datetime


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp("MonitoredDict created")

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp(f"value for key [{key}] retrieved")
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp(f"value for key [{key}] set")

    def log_timestamp(self, message):
        timestamp_str = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append(f"{timestamp_str} {message}")
