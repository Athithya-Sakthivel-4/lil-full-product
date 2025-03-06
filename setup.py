#!/usr/bin/env python3

import os
import argparse

# Define the complete project structure
project_structure = [
    "child_recovery_platform/backend/",
    "child_recovery_platform/backend/main.py",
    "child_recovery_platform/backend/config.py",
    "child_recovery_platform/backend/database.py",
    "child_recovery_platform/backend/dependencies.py",
    "child_recovery_platform/backend/auth.py",
    "child_recovery_platform/backend/face_recognition.py",
    "child_recovery_platform/backend/background_tasks.py",
    "child_recovery_platform/backend/routes/",
    "child_recovery_platform/backend/routes/__init__.py",
    "child_recovery_platform/backend/routes/user_routes.py",
    "child_recovery_platform/backend/routes/report_routes.py",
    "child_recovery_platform/backend/routes/child_routes.py",
    "child_recovery_platform/backend/models/",
    "child_recovery_platform/backend/models/__init__.py",
    "child_recovery_platform/backend/models/user.py",
    "child_recovery_platform/backend/models/report.py",
    "child_recovery_platform/backend/models/missing_child.py",
    "child_recovery_platform/backend/services/",
    "child_recovery_platform/backend/services/user_service.py",
    "child_recovery_platform/backend/services/report_service.py",
    "child_recovery_platform/backend/services/face_service.py",
    "child_recovery_platform/backend/utils/",
    "child_recovery_platform/backend/utils/image_utils.py",
    "child_recovery_platform/backend/utils/geo_utils.py",
    "child_recovery_platform/backend/templates/",
    "child_recovery_platform/backend/templates/report_match.html",
    "child_recovery_platform/backend/static/",
    "child_recovery_platform/backend/uploads/",
    "child_recovery_platform/backend/database_images/",
    "child_recovery_platform/backend/requirements.txt",
    "child_recovery_platform/backend/Makefile",
    "child_recovery_platform/backend/wsgi.py",
    "child_recovery_platform/frontend/",
    "child_recovery_platform/frontend/public/",
    "child_recovery_platform/frontend/public/logo.png",
    "child_recovery_platform/frontend/src/",
    "child_recovery_platform/frontend/src/components/",
    "child_recovery_platform/frontend/src/components/CameraCapture.js",
    "child_recovery_platform/frontend/src/components/FileUpload.js",
    "child_recovery_platform/frontend/src/components/Login.js",
    "child_recovery_platform/frontend/src/components/ReportForm.js",
    "child_recovery_platform/frontend/src/components/Map.js",
    "child_recovery_platform/frontend/src/pages/",
    "child_recovery_platform/frontend/src/pages/index.js",
    "child_recovery_platform/frontend/src/pages/login.js",
    "child_recovery_platform/frontend/src/pages/report.js",
    "child_recovery_platform/frontend/src/pages/admin.js",
    "child_recovery_platform/frontend/src/services/",
    "child_recovery_platform/frontend/src/services/api.js",
    "child_recovery_platform/frontend/src/styles/",
    "child_recovery_platform/frontend/src/styles/global.css",
    "child_recovery_platform/frontend/src/App.js",
    "child_recovery_platform/frontend/src/index.js",
    "child_recovery_platform/frontend/package.json",
    "child_recovery_platform/frontend/tailwind.config.js",
    "child_recovery_platform/frontend/next.config.js",
    "child_recovery_platform/infrastructure/",
    "child_recovery_platform/infrastructure/Dockerfile",
    "child_recovery_platform/infrastructure/docker-compose.yml",
    "child_recovery_platform/infrastructure/nginx.conf",
    "child_recovery_platform/infrastructure/redis.conf",
    "child_recovery_platform/infrastructure/cloud_setup.md",
    "child_recovery_platform/infrastructure/terraform/",
    "child_recovery_platform/docs/",
    "child_recovery_platform/docs/README.md",
    "child_recovery_platform/docs/API_Documentation.md",
    "child_recovery_platform/docs/Database_Schema.md",
    "child_recovery_platform/tests/",
    "child_recovery_platform/tests/test_auth.py",
    "child_recovery_platform/tests/test_face_recognition.py",
    "child_recovery_platform/tests/test_routes.py",
    "child_recovery_platform/scripts/",
    "child_recovery_platform/scripts/populate_db.py",
    "child_recovery_platform/scripts/cleanup.py",
    "child_recovery_platform/.github/",
    "child_recovery_platform/.github/workflows/",
    "child_recovery_platform/.github/workflows/backend.yml",
    "child_recovery_platform/.github/workflows/frontend.yml",
    "child_recovery_platform/.env",
    "child_recovery_platform/.gitignore",
    "child_recovery_platform/LICENSE"
]

def create_project_structure():
    """Creates the project directory structure."""
    for path in project_structure:
        if path.endswith("/"):
            os.makedirs(path, exist_ok=True)  # Create directories
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure parent directories exist
            with open(path, "w") as f:
                pass  # Create empty files
    print("✅ Project structure created successfully!")

def main():
    parser = argparse.ArgumentParser(description="Setup project structure for Child Recovery Platform.")
    parser.add_argument("command", nargs="?", default="create", help="Command to execute (default: create).")
    args = parser.parse_args()

    if args.command == "create":
        create_project_structure()
    else:
        print("❌ Invalid command. Use create to generate the project structure.")

if __name__ == "__main__":
    main()
