

class QUEST_PROGRESS_BASE(object):
    VIEW_TYPE_TOP = 'top'
    VIEW_TYPE_TAB = 'tab'
    VIEW_TYPE_QUEST_AWARD = 'questAward'
    VIEW_TYPES = [VIEW_TYPE_TOP, VIEW_TYPE_TAB, VIEW_TYPE_QUEST_AWARD]
    MAIN_ORDER_TYPE = 'main'
    ADD_ORDER_TYPE = 'add'
    ICON_CONDITION_SIZE_90 = 90
    ICON_CONDITION_SIZE_128_DECOR = 128
    ORDER_TYPES = [MAIN_ORDER_TYPE, ADD_ORDER_TYPE]
    NOT_STARTED_STATE = 1
    IN_PROGRESS_STATE = 2
    FAILED_STATE = 3
    PRELIMINARY_FAILED_STATE = 4
    COMPLETED_STATE = 5
    QUEST_PROGRESS_STATES = [NOT_STARTED_STATE, IN_PROGRESS_STATE, FAILED_STATE, PRELIMINARY_FAILED_STATE, COMPLETED_STATE]
    QP_VIEW_RENDERER_TAB = 'QuestProgressItemRendererTabViewUI'
    QP_VIEW_RENDERER_TOP = 'QuestProgressItemRendererTopViewUI'
    QP_VIEW_RENDERER_QUEST_AWARD = 'QuestProgressItemRendererQuestAwardViewUI'
    QP_TAB_ALERT_LABEL = 'TabAlertLabelUI'
    QP_OR_CONDITION_ICON_TAB = 'QuestProgressOrConditionTabUI'
    QP_OR_CONDITION_ICON_TOP = 'QuestProgressOrConditionTopUI'
    QP_OR_CONDITION_ICON_AWARD = 'QuestProgressOrConditionAwardUI'
    QP_METRIC_TYPE_SIMPLE = 'metricSimple'
    QP_METRIC_TYPE_SIMPLE_VALUE = 'metricSimpleValue'
    QP_METRIC_TYPE_RANGE = 'metricRangeValues'
    QP_METRIC_TYPE_VEHICLES = 'metricVehiclesValue'
    QP_METRIC_TYPE_TIMER = 'metricTimer'
    QP_METRIC_TYPE_LIMITER = 'metricLimiter'
    QUEST_PROGRESS_METRICS_SKIP_TAB = [QP_METRIC_TYPE_LIMITER, QP_METRIC_TYPE_SIMPLE_VALUE, QP_METRIC_TYPE_SIMPLE]
    QP_METRIC_SIMPLE_CMP_TAB = 'QPMetricsSimpleCmpTabUI'
    QP_METRIC_SIMPLE_VALUE_CMP_TAB = 'QPMetricsSimpleValueCmpTabUI'
    QP_METRIC_RANGE_VALUES_CMP_TAB = 'QPMetricsRangeValuesCmpTabUI'
    QP_METRIC_VEHICLES_CMP_TAB = 'QPMetricsVehiclesCmpTabUI'
    QP_METRIC_TIMER_CMP_TAB = 'QPMetricsTimerCmpTabUI'
    QP_METRIC_LIMITER_CMP_TAB = 'QPMetricsLimiterCmpTabUI'
    QP_METRIC_SIMPLE_CMP_TOP = 'QPMetricsSimpleCmpTopUI'
    QP_METRIC_SIMPLE_VALUE_CMP_TOP = 'QPMetricsSimpleValueCmpTopUI'
    QP_METRIC_RANGE_VALUES_CMP_TOP = 'QPMetricsRangeValuesCmpTopUI'
    QP_METRIC_VEHICLES_CMP_TOP = 'QPMetricsVehiclesCmpTopUI'
    QP_METRIC_TIMER_CMP_TOP = 'QPMetricsTimerCmpTopUI'
    QP_METRIC_LIMITER_CMP_TOP = 'QPMetricsLimiterCmpTopUI'
    QUEST_PROGRESS_BAR_RADIAL_100 = 'RadialBar100UI'
    QUEST_PROGRESS_BAR_RADIAL_54 = 'RadialBar54UI'
    QUEST_PROGRESS_BAR_RADIAL_42 = 'RadialBar42UI'
    QUEST_PROGRESS_BAR_RHOMBUS_58 = 'RhombusBar58UI'
    QUEST_PROGRESS_BAR_RHOMBUS_42 = 'RhombusBar42UI'
    QUEST_PROGRESS_BAR_HEXAGON_100 = 'HexagonBar100UI'
    QUEST_PROGRESS_BAR_HEXAGON_94 = 'HexagonBar94UI'
    QUEST_PROGRESS_BAR_HEXAGON_40 = 'HexagonBar40UI'
    QUEST_PROGRESS_BAR_TYPE_REGULARE = 'regular'
    QUEST_PROGRESS_BAR_TYPE_CUMULATIVE = 'cumulative'
    QP_TEXT_COLOR_STATE_COMPLETED = 8034621
    QP_TEXT_COLOR_STATE_COMPLETED_VALUE = 13434726
    QP_TEXT_COLOR_STATE_IN_PROGRESS = 9211006
    QP_TEXT_COLOR_STATE_IN_PROGRESS_VALUE = 15327935
    QP_TEXT_COLOR_STATE_FAILD = 7938578
    QP_TEXT_COLOR_STATE_FAILD_VALUE = 16722432
    QP_TIMER_STATE_NORMAL = 'normal'
    QP_TIMER_STATE_WARNING = 'warning'
    QP_TIMER_STATE_CRITICAL = 'critical'
    QP_TIMER_STATE_WAS_COMPLETED = 'wasCompleted'
    HEADER_PROGRESS_TYPE_NONE = 'none'
    HEADER_PROGRESS_TYPE_COUNTER = 'counter'
    HEADER_PROGRESS_TYPE_BIATHLON = 'biathlon'
    HEADER_PROGRESS_TYPE_SERIES = 'iconDashed'
    HEADER_PROGRESS_TYPE_LIMITED = 'limited'
    HEADER_PROGRESS_TYPE_SIMPLE = 'simple'
    HEADER_PROGRESS_LINKAGE_NONE = 'HeaderProgressItemNoneUI'
    HEADER_PROGRESS_LINKAGE_COUNTER = 'HeaderProgressItemCounterUI'
    HEADER_PROGRESS_LINKAGE_BIATHLON = 'HeaderProgressItemBiathlonUI'
    HEADER_PROGRESS_LINKAGE_SERIES = 'HeaderProgressItemSeriesUI'
    HEADER_PROGRESS_LINKAGE_LIMITED = 'HeaderProgressItemLimitedUI'
    HEADER_PROGRESS_LINKAGE_SIMPLE = 'HeaderProgressItemSimpleUI'
    HEADER_PROGRESS_LINKAGE_BIG_COUNTER = 'HeaderProgressBigItemCounterUI'
    HEADER_PROGRESS_LINKAGE_BIG_BIATHLON = 'HeaderProgressBigItemBiathlonUI'
    HEADER_PROGRESS_LINKAGE_BIG_SERIES = 'HeaderProgressBigItemSeriesUI'
    HEADER_PROGRESS_BLOCK_NOT_STARTED = 0
    HEADER_PROGRESS_BLOCK_IN_PROGRESS = 1
    HEADER_PROGRESS_BLOCK_COMPLETED = 2
    HEADER_PROGRESS_BLOCK_FAILED = 3
    PROGRESS_SCOPE_BATTLE = 'battle'
    PROGRESS_SCOPE_HANGAR = 'hangar'
    HEADER_PROGRESS_BITMAP_FILL = 'header_progress_bm_fill'
    HEADER_PROGRESS_BITMAP_FILL_HEIGHT = 3
    HEADER_PROGRESS_BIG_BITMAP_FILL = 'header_progress_big_bm_fill'
    HEADER_PROGRESS_BIG_BITMAP_FILL_HEIGHT = 7
    PROGRESS_SOLID_SEPARATOR_CMPNT = 'ProgressSolidSeparatorUI'
    PROGRESS_SOLID_BIG_SEPARATOR_CMPNT = 'ProgressSolidBigSeparatorUI'
    PROGRESS_SOLID_POINT_STATE_PREV = 'pointPrev'
    PROGRESS_SOLID_POINT_STATE_NEXT = 'pointNext'
    PROGRESS_SOLID_POINT_STATE_CURRENT = 'pointCurrent'
    PROGRESS_DASHED_DASH_ICON = 'ProgressIconDashUI'
    PROGRESS_DASHED_BIG_DASH_ICON = 'ProgressBigIconDashUI'
    PROGRESS_DASHED_DASH = 'ProgressDashUI'
    PROGRESS_DASHED_BIG_DASH = 'ProgressBigDashUI'
    PROGRESS_DASHED_DASH_STATE_EMPTY = 'empty'
    PROGRESS_DASHED_DASH_STATE_SUCCESS = 'success'
    PROGRESS_DASHED_DASH_STATE_FAILED = 'failed'
    PROGRESS_DASHED_DASH_STATE_CURRENT = 'current'