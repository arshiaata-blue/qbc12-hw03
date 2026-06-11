from pydantic import BaseModel

class ListingFeatures(BaseModel):
    room_type: str
    property_type: str
    neighbourhood_name: str
    accommodates: int
    bedrooms: float = None
    beds: float = None
    bathrooms: float = None
    listing_price: float = None
    minimum_nights: int
    maximum_nights: int
    instant_bookable: bool
    host_is_superhost: bool
    host_listing_count: int
    total_reviews_before_cutoff: float = None
    unique_reviewers_before_cutoff: float = None
    avg_comment_len_before_cutoff: float = None
    max_comment_len_before_cutoff: float = None
    days_since_last_review: float = None
    available_days_last_90d: int
    available_rate_last_90d: float
    avg_minimum_nights_calendar_last_90d: float = None
    avg_maximum_nights_calendar_last_90d: float = None
    available_days_last_30d: int
    available_rate_last_30d: float
    avg_minimum_nights_calendar_last_30d: float = None
    avg_maximum_nights_calendar_last_30d: float = None

class PredictionResponse(BaseModel):
    listing_id: int = None
    prediction: int
    probability_high_demand: float
    model_run_id: str
