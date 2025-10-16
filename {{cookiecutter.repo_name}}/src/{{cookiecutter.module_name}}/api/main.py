import uvicorn

from {{ cookiecutter.module_name }}.api import infer

def main():
    uvicorn.run(infer.app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()