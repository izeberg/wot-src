from gui.filters.carousel_filter import RoleCriteriesGroup
from gui.shared.utils.requesters.ItemsRequester import RequestCriteria, PredicateCondition
FL_RENT = RequestCriteria(PredicateCondition(lambda item: item.name.endswith('_FL')))

class FLRentedCriteriaGroup(RoleCriteriesGroup):

    def update(self, filters):
        super(FLRentedCriteriaGroup, self).update(filters)
        if not filters['rented']:
            self._criteria |= ~FL_RENT

    @staticmethod
    def isApplicableFor(vehicle):
        return True