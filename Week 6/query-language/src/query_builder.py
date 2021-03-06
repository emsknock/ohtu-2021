from matchers import (
    All,
    And,
    Or,
    PlaysIn,
    HasAtLeast,
    HasFewerThan
)

class QueryBuilder:
    def __init__(self):
        self._matcher = All()

    def _and(self, matcher):
        self._matcher = And(self._matcher, matcher)

    def _or(self, *matchers):
        self._matcher = Or(self._matcher, *matchers)

    def build(self):
        return self._matcher

    def matches(self, player):
        return self._matcher.matches(player)

    def playsIn(self, team):
        self._and(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._and(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._and(HasFewerThan(value, attr))
        return self

    def oneOf(self, *matchers):
        self._or(*matchers)
        return self