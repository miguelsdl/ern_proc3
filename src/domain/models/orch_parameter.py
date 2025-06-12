from sqlalchemy import Column, Integer, Text, DateTime, Boolean, DECIMAL
from .base import Base

class OrchParameter(Base):
    __tablename__ = 'orch_parameters'
    __table_args__ = {'schema': 'feed'}

    param_id = Column(Integer, primary_key=True, autoincrement=True)
    param_code = Column(Integer)
    param_name = Column(Text)
    param_long_name = Column(Text)
    param_numeric_value = Column(DECIMAL)
    param_boolean_value = Column(Boolean)
    param_string_value = Column(Text)
    param_deactivation_date = Column(DateTime)
    param_activation_date = Column(DateTime)
    param_order = Column(Integer)
    param_description = Column(Text)
    param_substitute_code = Column(Integer)