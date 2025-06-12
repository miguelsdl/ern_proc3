from sqlalchemy import Column, Integer, String, Text, DateTime
from .base import Base

class Ern(Base):
    __tablename__ = 'erns'
    __table_args__ = {'schema': 'feed'}

    id_ern = Column(Integer, primary_key=True, autoincrement=True)
    sqs_message_id_ern = Column(String(255))
    sqs_receipt_handle_ern = Column(Text)
    sqs_md5_of_body_ern = Column(String(255))
    origin_ern = Column(String(255))
    bucket_ern = Column(String(255))
    key_path_ern = Column(Text)
    delivery_timestamp_ern = Column(DateTime)
    sqs_insert_timestamp_ern = Column(DateTime)
    batch_id_ern = Column(String(255))
    batch_timestamp_ern = Column(DateTime)
    upc_identifier_ern = Column(String(255))
    status_processed_resources_ern = Column(String(255), default='PENDING', nullable=False)
    sent_to_process_resources_qty_ern = Column(Integer, default=0, nullable=False)
    processed_resources_qty_ern = Column(Integer, default=0, nullable=False)
    status_loaded_to_catalog_ern = Column(String(255), default='PROCESSING', nullable=False)
    status_resources_copied_to_s3_ern = Column(String(255), default='PENDING', nullable=False)
    status_activated_message_ern = Column(String(255), default='PENDING', nullable=False)
    status_ack_sent_ern = Column(String(255), default='PENDING', nullable=False)