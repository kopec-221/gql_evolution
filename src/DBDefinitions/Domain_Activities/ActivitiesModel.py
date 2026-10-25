from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.DBDefinitions.BaseModel import BaseDBModel, UUIDFKey, IDType

class ActivityTypeModel(BaseDBModel):
    __tablename__ = "activitytypes"

    name: Mapped[Optional[str]] = mapped_column(String, default=None, index=True, nullable=True)
    label: Mapped[Optional[str]] = mapped_column(String, default=None, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String, default=None, nullable=True)

class ActivityModel(BaseDBModel):
    __tablename__ = "activities"

    entity_id: Mapped[Optional[IDType]] = UUIDFKey(nullable=True)
    entity_type_id: Mapped[Optional[IDType]] = UUIDFKey(nullable=True)
    actor_id: Mapped[Optional[IDType]] = UUIDFKey(nullable=True)

    title: Mapped[Optional[str]] = mapped_column(String, default=None, nullable=True)
    content: Mapped[Optional[str]] = mapped_column(String, default=None, nullable=True)

    activity_type_id: Mapped[Optional[IDType]] = mapped_column(ForeignKey("activitytypes.id"), default=None, index=True, nullable=True)
    activity_type = relationship("ActivityTypeModel", viewonly=True)