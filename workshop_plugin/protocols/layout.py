from canvas_sdk.events import EventType
from canvas_sdk.handlers.base import BaseHandler
from canvas_sdk.effects.patient_chart_summary_configuration import PatientChartSummaryConfiguration


class SummarySectionLayout(BaseHandler):
    RESPONDS_TO = EventType.Name(
        EventType.PATIENT_CHART_SUMMARY__SECTION_CONFIGURATION)

    def compute(self):
        layout = PatientChartSummaryConfiguration(sections=[
            PatientChartSummaryConfiguration.Section.CONDITIONS,
            PatientChartSummaryConfiguration.Section.ALLERGIES,
            PatientChartSummaryConfiguration.Section.GOALS,
            PatientChartSummaryConfiguration.Section.CARE_TEAMS,
            PatientChartSummaryConfiguration.Section.SOCIAL_DETERMINANTS,
            PatientChartSummaryConfiguration.Section.CODING_GAPS,
            PatientChartSummaryConfiguration.Section.MEDICATIONS,
            PatientChartSummaryConfiguration.Section.VITALS,
        ])

        return [layout.apply()]
