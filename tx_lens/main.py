import uvicorn

from tx_lens.settings import Settings


def main() -> None:
    uvicorn.run(
        "tx_lens.api.app:app",
        host=Settings.HOST,
        port=Settings.PORT,
    )


if __name__ == "__main__":
    main()
