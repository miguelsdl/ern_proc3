from sqlalchemy import Column, Integer, String, Text, DateTime
from .base import Base

class S3DeliveryData(Base):
    __tablename__ = 's3_delivery_data'
    __table_args__ = {'schema': 'feed'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    message_id = Column(String(255))
    receipt_handle = Column(Text)
    md5_of_body = Column(String(255))
    origin = Column(String(255))
    bucket = Column(String(255))
    key_path = Column(Text)
    delivery_timestamp = Column(DateTime)
    sqs_insert_timestamp = Column(DateTime)
    batch_id = Column(String(255))
    batch_timestamp = Column(DateTime)
    upc_or_grid = Column(String(255))
    status_processed_resources = Column(String(255), default='PENDING', nullable=False)
    sent_to_process_resources_qty = Column(Integer, default=0, nullable=False)
    processed_resources_qty = Column(Integer, default=0, nullable=False)
    status_loaded_to_catalog = Column(String(255), default='PROCESSING', nullable=False)
    status_resources_copied_to_s3 = Column(String(255), default='PENDING', nullable=False)
    status_activated_message = Column(String(255), default='PENDING', nullable=False)
    status_ack_sent = Column(String(255), default='PENDING', nullable=False)