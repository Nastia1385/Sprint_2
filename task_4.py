class EmployeeSalary:
    hourly_payment = 400
    name = None
    hours = None
    rest_days = 0
    email = None

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, hours):
        if hours is None:
            cls.hours = (7 - cls.rest_days) * 8
        return cls(cls.name, cls.hours, cls.rest_days, cls.email)

    @classmethod
    def get_email(cls):
        if cls.email is None:
            cls.email = f"{cls.name}@email.com"
        return cls(cls.name, cls.hours, cls.rest_days, cls.email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment
