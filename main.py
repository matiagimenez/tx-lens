import uvicorn

from tx_lens.settings import Settings


def main():
    uvicorn.run(
        "tx_lens.app:app",
        host=Settings.HOST,
        port=Settings.PORT,
        reload=Settings.DEBUG,
    )


if __name__ == "__main__":
    main()
