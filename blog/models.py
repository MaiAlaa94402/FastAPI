from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
# from .database import Base


class Base (DeclarativeBase):
    pass
class Blog(Base):
    
    __tablename__ = "blogs"    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()

    # id = Column(Integer, primary_key=True, index=True)
    # title = Column(String)
    # body = Column(String)
    # user_id = Column(Integer, ForeignKey('users.id'))
    
    # creator = relationship('User', back_populates='blogs')
    user_id = mapped_column(ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")    
    
    
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    
    # blogs = relationship('Blog', back_populates='creator')
    blogs = relationship("Blog", back_populates="creator")