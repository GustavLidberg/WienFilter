from __future__ import annotations
from typing import Any, Callable, TYPE_CHECKING
import logging

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, Q_ARG, QMetaObject, QRunnable

# import pythion._routines.routine_handler as rth
if TYPE_CHECKING:
    from pythion._routines.routine_handler import RoutineHandler

logger = logging.getLogger('pythion')


class Routine(QRunnable):
    tasks: list[tuple[Callable[..., None], list[Any], dict[str, Any]]]

    def __init__(self):
        super().__init__()
        self.setAutoDelete(False)
        self.handler = None
        self.tasks = []

    def update_widget(widget: QWidget, slot: str, *args: Any, block: bool = False) -> None:
        connection = Qt.BlockingQueuedConnection if block else Qt.QueuedConnection
        QMetaObject.invokeMethod(widget, slot, connection, *[Q_ARG(type(arg), arg) for arg in args])  # type: ignore

    def run(self) -> None:
        for task, args, kwargs in self.tasks:
            task(*args, **kwargs)

    def add_task(self, task, *args, **kwargs):
        self.tasks.append(task, args, kwargs)

    def set_handler(self, handler: RoutineHandler):
        self.handler = handler

    def run_on_main_thread(self, function: Callable[..., None], *args, block: bool = False, **kwargs):
        if self.context is None:
            logger.error('Routine:        Cannot execute on main thread: no RoutineHandler context available')
        self.context.set_function(function, *args, **kwargs)
        self.update_widget('main_thread_execute', block=block)
