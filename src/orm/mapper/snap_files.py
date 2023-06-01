import time
import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError

from src.orm.database.database_service import Base, session_scope
from src.tool.common_logger import CommonLogger

logger = CommonLogger().get_logger()


class SnapFiles(Base):
    __tablename__ = 'snap_files'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    file_id = Column(String, primary_key=False, nullable=False)
    file_name = Column(String, primary_key=False, nullable=False)
    created_time = Column(Integer, primary_key=False, nullable=False)
    updated_time = Column(Integer, primary_key=False, nullable=False)
    complete_path = Column(String, primary_key=False, nullable=False)
    watermark_path = Column(String, primary_key=False, nullable=False)

    def __repr__(self):
        return str(self.__dict__)

    def get_snap_file(self, file_id: str):
        with session_scope() as local_session:
            snap_file = None
            try:
                snap_file = local_session.query(SnapFiles.file_id,SnapFiles.complete_path).filter(SnapFiles.file_id == file_id).first()
            except SQLAlchemyError as e:
                local_session.rollback()
                logger.error("update snap files error", e)
            finally:
                local_session.close()
            return snap_file
    
    def update_snap_file_path(self, path: str, file_id: str):
        with session_scope() as local_session:
            try:
                new = local_session.query(SnapFiles).filter(SnapFiles.file_id == str(file_id)).first()
                new.complete_path = path
                local_session.commit()
            except SQLAlchemyError as e:
                local_session.rollback()
                logger.error("update snap files error", e)
            finally:
                local_session.close()

    def insert_snap_files(self, file_name: str,complete_path:str,watermark_path:str):
        with session_scope() as local_session:
            snap_files = None
            try:
                snap_files = SnapFiles(
                    file_id= uuid.uuid4(),
                    file_name= file_name,
                    created_time=int(time.time() * 1000),
                    updated_time=int(time.time() * 1000),
                    complete_path= complete_path,
                    watermark_path=watermark_path
                )
                local_session.add(snap_files)
                local_session.flush()
                local_session.commit()
                local_session.refresh(snap_files)
            except SQLAlchemyError as e:
                local_session.rollback()
                logger.error("save snap files error", e)
            finally:
                local_session.close()
            return snap_files
