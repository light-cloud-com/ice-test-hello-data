"""ICE test data pipeline — reads env and prints structured output."""
import os, json, sys

def main():
    project = os.environ.get("GOOGLE_CLOUD_PROJECT", "unknown")
    print(json.dumps({
        "status": "ok",
        "service": "ice-test-hello-data",
        "project": project,
        "message": "Data pipeline executed successfully"
    }))
    sys.exit(0)

if __name__ == "__main__":
    main()
