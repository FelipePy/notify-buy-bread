# iniciar projeto fastapi

def main():
    import uvicorn

    uvicorn.run("src.bootstrap.server:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()