from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from tx_lens import __version__
from tx_lens.api.v1 import register_v1_exception_handlers, v1_router
from tx_lens.injections import configure_injections
from tx_lens.settings import Settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:  # pylint: disable=redefined-outer-name,unused-argument
    configure_injections()
    yield


app = FastAPI(title="Transactions Lens", version=__version__, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_v1_exception_handlers(app)


@app.get("/healthcheck")
async def healthcheck() -> dict[str, Any]:
    return {"status": "OK", "version": __version__}


@app.get("/", include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


app.include_router(v1_router, prefix=Settings.BASE_PATH)
