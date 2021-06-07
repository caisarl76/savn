from .basemodel import BaseModel
from .gcn import GCN
from .savn import SAVN, M_SAVN

__all__ = ["BaseModel", "GCN", "SAVN", "M_SAVN"]

variables = locals()
