from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from tx_lens import __version__
from tx_lens.api.v1.router import v1_router
from tx_lens.settings import Settings

app = FastAPI(title="Transactions Lens", version=__version__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthcheck")
async def healthcheck() -> dict[str, Any]:
    return {"status": "OK", "version": __version__}


@app.get("/", include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    return RedirectResponse(url="/docs")


app.include_router(v1_router, prefix=Settings.BASE_PATH)
