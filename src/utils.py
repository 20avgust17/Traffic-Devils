from typing import Any

from fastapi import HTTPException


def raise_exception_if_true(
        item: Any,
        on_error_message: str,
        status_code: int,
        **kwargs,
) -> bool:
    if bool(item):
        raise HTTPException(
            detail=on_error_message,
            status_code=status_code,
            **kwargs
        )
    return True
