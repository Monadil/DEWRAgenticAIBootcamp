"""Mock Healthcare Workforce tool for the Ministerial Brief Agent (DEWR lab).

This is the single stubbed service the Statistics Agent calls. It is pre-registered
as a tool in watsonx Orchestrate for the lab, so attendees only need to *attach* it
to the Statistics Agent — they do not build or host anything.

All figures are ILLUSTRATIVE mock data, not real ABS/JSA numbers. Shortage types use
the Richardson typology (Longer Training Gap / Shorter Training Gap / Suitability Gap /
Retention Gap), consistent with the JSA framework used elsewhere in the course.

Replace this stub later with a real ABS/JSA feed without changing the agent wiring.
"""


def get_healthcare_workforce() -> dict:
    """Return current healthcare workforce roles and a sector summary.

    Mirrors: GET /api/v1/healthcare-workforce/current
    """
    return {
        "period": "April 2026",
        "sector": "Healthcare and Social Assistance",
        "source": "Illustrative mock data (DEWR bootcamp) — cite as 'JSA Occupation Shortage List 2025' in briefs",
        "roles": [
            {
                "occupation": "Registered Nurses",
                "employed_this_month": 312400,
                "change_from_last_month": -1200,
                "shortage_status": "National shortage",
                "shortage_type": "Retention gap",
            },
            {
                "occupation": "Aged and Disabled Carers",
                "employed_this_month": 198600,
                "change_from_last_month": -800,
                "shortage_status": "National shortage",
                "shortage_type": "Retention gap",
            },
            {
                "occupation": "General Practitioners",
                "employed_this_month": 42300,
                "change_from_last_month": -150,
                "shortage_status": "National shortage",
                "shortage_type": "Longer training gap",
            },
            {
                "occupation": "Mental Health Nurses",
                "employed_this_month": 28900,
                "change_from_last_month": -280,
                "shortage_status": "National shortage",
                "shortage_type": "Suitability gap",
            },
            {
                "occupation": "Midwives",
                "employed_this_month": 23800,
                "change_from_last_month": -320,
                "shortage_status": "National shortage",
                "shortage_type": "Retention gap",
            },
            {
                "occupation": "Radiographers",
                "employed_this_month": 18600,
                "change_from_last_month": -120,
                "shortage_status": "National shortage",
                "shortage_type": "Shorter training gap",
            },
            {
                "occupation": "Physiotherapists",
                "employed_this_month": 38200,
                "change_from_last_month": 420,
                "shortage_status": "Not in shortage",
                "shortage_type": None,
            },
        ],
        "sector_summary": {
            "pct_roles_in_shortage": 48,
            "primary_driver": "Retention gap",
            "regional_fill_rate": 62.9,
            "metro_fill_rate": 69.7,
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(get_healthcare_workforce(), indent=2))
