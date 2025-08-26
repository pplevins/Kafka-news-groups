from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, BeforeValidator, Field, ConfigDict

PyObjectId = Annotated[str, BeforeValidator(str)]


class NewsModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    category: str = Field(...)
    text: str = Field(...)
    timestamp: datetime = Field(...)

    # A mapping dictionary for model representation in the API
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        use_enum_values=True,
        json_schema_extra={
            "example": {
                "category": "comp.windows.x",
                "text": "From: mahan@TGV.COM (Patrick L. Mahan)\nSubject: Re: Remote X across TCPIP & Decnet",
                "timestamp": datetime.now()
            }
        },
    )
