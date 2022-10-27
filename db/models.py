from sqlalchemy import Boolean, Column, DateTime, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Raffle(Base):
    __tablename__ = "raffles"

    id = Column(Integer, primary_key=True)
    guild_id = Column(BigInteger, nullable=False)
    message_id = Column(BigInteger, nullable=False, unique=True)
    ended = Column(Boolean, nullable=False, default=False)
    end_time = Column(DateTime, nullable=True)

    entries = relationship("RaffleEntry", back_populates="raffle")

    def __repr__(self):
        return f"Raffle(id={self.id!r}, guild_id={self.guild_id!r}, message_id={self.message_id!r})"

class RaffleEntry(Base):
    __tablename__ = "raffle_entries"

    id = Column(Integer, primary_key=True)
    raffle_id = Column(Integer, ForeignKey("raffles.id"))
    user_id = Column(BigInteger, nullable=False)
    tickets = Column(BigInteger, nullable=False, default=0)
    winner = Column(Boolean, nullable=False, default=False)

    raffle = relationship("Raffle", back_populates="entries")

    def __repr__(self):
        return f"RaffleEntry(id={self.id!r}, raffle_id={self.raffle_id!r}, user_id={self.user_id!r}, tickets={self.tickets!r}, winner={self.winner!r})"

class RoleModifier(Base):
    __tablename__ = "role_modifiers"

    id = Column(Integer, primary_key=True)
    guild_id = Column(BigInteger, nullable=False)
    role_id = Column(BigInteger, nullable=True, unique=True)
    modifier = Column(BigInteger, nullable=False, default=0)

    def __repr__(self):
        return f"RoleModifier(id={self.id!r}, guild_id={self.guild_id!r}, role_id={self.role_id!r}, modifier={self.modifier!r})"