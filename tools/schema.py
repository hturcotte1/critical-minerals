"""Shared schema for the supplier map. Used by validate.py and build.py.

Every research agent writes JSON Lines files (one JSON object per line) into
data/staging/<workstream>/. build.py merges them into the final CSV/XLSX files.
"""

SUPPLIER_FIELDS = [
    "supplier_id",
    "company_name",
    "parent_company",
    "ultimate_owner",
    "owner_country",
    "covered_country_tie",
    "tie_detail",
    "material_chain",
    "stage",
    "products",
    "facility_name",
    "city",
    "state_region",
    "country",
    "facility_status",
    "expected_production_date",
    "capacity_value",
    "capacity_unit",
    "capacity_year",
    "capacity_source",
    "feedstock_origin",
    "committed_offtakes",
    "government_awards",
    "rmi_rmap_status",
    "dfars_7052_assessment",
    "dfars_7052_reason",
    "capacity_availability",
    "broker_fit_score",
    "broker_fit_rationale",
    "commercial_contact_url",
    "sources",
    "date_accessed",
    "confidence",
    "notes",
    "gbd_capability",
]

OFFTAKE_FIELDS = [
    "offtake_id",
    "seller",
    "buyer",
    "material_chain",
    "material",
    "form",
    "volume",
    "term",
    "binding_status",
    "price_mechanism",
    "announcement_date",
    "source",
    "notes",
]

EXCLUDED_FIELDS = [
    "excluded_id",
    "company_name",
    "aliases",
    "parent_company",
    "ultimate_owner",
    "covered_country",
    "material_chain",
    "stage",
    "products",
    "facility_name",
    "city",
    "state_region",
    "rmi_smelter_id",
    "notes",
    "sources",
    "date_accessed",
]

SOURCE_FIELDS = [
    "source_id",
    "title",
    "publisher",
    "date",
    "url",
    "type",
    "date_accessed",
]

# Fixed stage vocabulary per material chain (documented in docs/scope.md).
STAGES = {
    "tungsten": ["mining_concentrate", "chemical_intermediate", "metal_powder",
                 "heavy_alloy_fabrication", "recycling"],
    "tantalum": ["mining_concentrate", "chemical_processing", "metal_powder_ingot",
                 "alloy_mill_products", "recycling"],
    "ndfeb": ["mining_concentrate", "separation", "metal_alloy", "magnet_sintered",
              "magnet_bonded", "recycling", "ancillary_inputs", "substitute"],
    "smco": ["mining_concentrate", "separation", "metal", "alloy", "magnet", "recycling"],
    "cobalt": ["mining_intermediate", "refining_metal", "powder", "recycling"],
    "molybdenum": ["mining_concentrate", "roasting_chemical", "metal_powder",
                   "mill_products_alloys", "recycling"],
    "gallium": ["primary_extraction", "refining_high_purity", "compounds_wafers", "recycling"],
    "germanium": ["primary_extraction", "refining_chemical", "metal_high_purity",
                  "products_optics_wafers", "recycling"],
    "trader": ["trader", "distributor", "stockholder", "government_stockpile"],
    "lab": ["assay_lab", "inspection_sampling", "provenance_lab", "audit_certification"],
}

MATERIAL_CHAINS = list(STAGES.keys())

ID_PREFIX = {
    "tungsten": "W", "tantalum": "TA", "ndfeb": "ND", "smco": "SM", "cobalt": "CO",
    "molybdenum": "MO", "gallium": "GA", "germanium": "GE", "trader": "TR", "lab": "LB",
}

TIE_VALUES = ["none", "ownership", "control", "financing", "feedstock", "unknown"]
FACILITY_STATUS = ["operating", "commissioning", "construction", "planned", "closed"]
ASSESSMENT = ["likely_compliant", "at_risk", "likely_noncompliant", "unknown"]
AVAILABILITY = ["uncommitted", "partially_committed", "fully_committed", "unknown"]
CONFIDENCE = ["high", "medium", "low"]
GBD = ["yes", "no", "planned", "unknown", "n/a", ""]
RMAP_PREFIXES = ["conformant", "active", "not_listed", "n/a", "unknown"]
BINDING = ["binding", "non-binding", "unknown"]
SOURCE_TYPES = ["primary filing", "government", "company release", "trade press", "other"]
COVERED_COUNTRIES = ["China", "Russia", "North Korea", "Iran"]
