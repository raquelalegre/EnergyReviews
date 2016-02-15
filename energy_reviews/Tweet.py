import datetime

class Tweet:
  def __init__(self):
    pass

  def set_id(self, id):
    self.id = id

  def set_author(self, author):
    self.author = author

  def set_location(self, location):
    self.location = location

  def set_since(self, since):
    self._assert_date_valid(since)
    self.since = since

  def set_until(self, until):
    self._assert_date_valid(until)
    self.until = until

  def _assert_date_valid(self, date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

  def __iter__(self):
    return iter(vars(self))

  def pretty_print(self):
      for member in self:
          print member
          print getattr(self, member)

  def pretty_str(self):
      tweet_str = ''
      for member in self:
          tweet_str += member + ':' + str(getattr(self, member))
          print tweet_str
      return tweet_str
