from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, Boolean, ForeignKey, DateTime
from datetime import datetime
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)

    pedidos: Mapped[list["Pedido"]] = relationship(
        "Pedido",
        back_populates="usuario"
    )


class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    criado_em: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    status: Mapped[str] = mapped_column(
        String(50),
        default="pendente"
    )

    usuario: Mapped["Usuario"] = relationship(
        "Usuario",
        back_populates="pedidos"
    )

    itens: Mapped[list["PedidoItem"]] = relationship(
        "PedidoItem",
        back_populates="pedido"
    )


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    preco: Mapped[float] = mapped_column(Float)
    estoque: Mapped[int] = mapped_column(Integer)


class PedidoItem(Base):
    __tablename__ = "pedido_itens"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    pedido_id: Mapped[int] = mapped_column(
        ForeignKey("pedidos.id")
    )

    produto_id: Mapped[int] = mapped_column(
        ForeignKey("produtos.id")
    )

    quantidade: Mapped[int] = mapped_column(Integer)

    pedido: Mapped["Pedido"] = relationship(
        "Pedido",
        back_populates="itens"
    )

    produto: Mapped["Produto"] = relationship(
        "Produto"
    )