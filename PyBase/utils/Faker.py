import numpy as num
from faker import Faker
from faker.providers import internet


class FakerHelper:
    def __init__(self):
        self.fake = Faker()

    def name(self, gender=None):
        if gender == 'F': return self.fake.name_female()
        if gender == 'M': return self.fake.name_male()
        return self.fake.name()

    def job(self):
        return self.fake.job()

    def address(self):
        return self.fake.address()

    def text(self):
        return self.fake.text()

    def ip4(self):
        self.fake.add_provider(internet)
        return self.fake.ipv4_private()

    def month(self):
        return self.fake.month()

    def year(self):
        return self.fake.year()

    # Return such as 09:25:30
    def time(self):
        return self.fake.time()

    def date_between(self):
        return self.fake.date_between(start_date="-3y", end_date="-1y")

    def timezone(self):
        return self.fake.timezone()

    def date_time_this_year(self):
        return self.fake.date_time_this_year()

    def month_name(self):
        return self.fake.month_name()

    # Datetime: 1988-01-24 09:16:09
    def date_time(self):
        return self.fake.date_time()

    def day_of_week(self):
        return self.fake.day_of_week()

    def time_object(self):
        return self.fake.time_object()

    # Create a fake basic profile with personal information such as name, gender, mail, and address.
    def simple_profile(self):
        return self.fake.simple_profile()

    # Create a fake basic profile with personal information
    def profile(self):
        return self.fake.profile()

    def profiles(self, no_of_data: 1):
        return [self.profile() for i in range(no_of_data)]

    def texts(self):
        return self.fake.texts()

    def sentence(self):
        return self.fake.sentence()

    def name_localized(self, locale='en_US'):
        fake_local = Faker(locale)
        return fake_local.name()

    def names_localized(self, locale='en_US', no_of_name=1):
        fake_local = Faker(locale)
        localed_names = [fake_local.name() for b in range(no_of_name)]
        return localed_names

    def city(self):
        return self.fake.city()

    def unique_names(self, no_of_name=1):
        unique_names = [self.fake.unique.name() for b in range(no_of_name)]
        return unique_names

    def currency(self):
        return self.fake.currency()

    def cryptocurrency(self):
        return self.fake.cryptocurrency()

    def array(self):
        return num.random.rand(5)

    def email(self):
        return self.fake.email()

    # return date such as 2022-10-25
    def date(self):
        return self.fake.date()

    def phone(self):
        return self.fake.phone_number()

    def sentenceByGivenList(self, listdata=[]):
        return self.fake.sentence(ext_word_list=listdata)

    def int(self):
        return self.fake.random_int()

    def int_in_range(self, start=1, end=10):
        return self.fake.random_int(start, end)

    def number(self, no_of_digit=1):
        return self.fake.random_number(digits=no_of_digit)

    def day_of_month(self):
        return self.fake.day_of_month()

    def day_of_week(self):
        return self.fake.day_of_week()

    def am_pm(self):
        return self.fake.am_pm()

    def first_name(self):
        return self.fake.first_name()

    def last_name(self):
        return self.fake.last_name()

    def currency_name(self):
        return self.fake.currency_name()

    def currency_code(self):
        return self.fake.currency_code()

    def word(self):
        return self.fake.word()

    def words(self, no_of_item=1):
        return self.fake.words(no_of_item)

    def random_digit(self):
        return self.fake.random_digit()

    def md5(self):
        return self.fake.md5()

    def sha1(self):
        return self.fake.sha1()

    def sha256(self):
        return self.fake.sha256()

    def uuid4(self):
        return self.fake.uuid4()

    def safe_email(self):
        return self.fake.safe_email()

    def free_email(self):
        return self.fake.free_email()

    def company_email(self):
        return self.fake.company_email()

    def hostname(self):
        return self.fake.hostname()

    def domain_name(self):
        return self.fake.domain_name()

    def ipv6(self):
        return self.fake.ipv6()

    def mac_address(self):
        return self.fake.mac_address()

    def url_image(self):
        return self.fake.image_url()

    def unix_time(self):
        return self.fake.unix_time()

    # iso8601: 2014-04-22T04:19:18
    def date_iso8601(self):
        return self.fake.iso8601()
